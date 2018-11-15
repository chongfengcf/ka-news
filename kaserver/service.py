from sqlalchemy.exc import IntegrityError
from entity import User, News, User_type
from flaskapp import db


def login(user, password):
    user = User.query.filter_by(user=user).first()
    if user == None:
        return False


    if user.password == password:
        return user.id
    else:
        return False

def register(user, password):
    user = User(user=user, password=password)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return False
    return True

def news_get(page):
    pagination = db.session.query(News.id, News.title, News.img, News.typeid).order_by(News.id.desc()).paginate(page, per_page=5, error_out=False)
    list = pagination.items
    res = {}
    res['list'] = list
    res['next'] = pagination.has_next
    return res

def typenews_get(page, type):
    pagination = db.session.query(News.id, News.title, News.img, News.typeid).filter_by(typeid=type).order_by(News.id.desc()).paginate(page, per_page=5, error_out=False)
    list = pagination.items
    res = {}
    res['list'] = list
    res['next'] = pagination.has_next
    return res

def contentnews_get(id):
    news = News.query.get(id)
    content = news.content
    return content

def usertype_add(userid, type):
    ut = User_type.query.filter_by(userid=userid, typeid =type).first()
    if ut == None:
        ut = User_type(userid=userid, typeid=type, num=1)
        db.session.add(ut)
        db.session.commit()
    else:
        num = ut.num + 1
        ut.num = num
        db.session.commit()


def history_get(id):
    history = User_type.query.filter_by(userid=id)
    res = [0] * 4
    for i in history:
        res[i.typeid-1] = i.num
    return res