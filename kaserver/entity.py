from flaskapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username



class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typename = db.Column(db.String(6))

    def __init__(self, typename):
        self.typename = typename

    def __repr__(self):
        return '<Type %r>' % self.typename

#feilei = Type(typename='国内')
#db.session.add(feilei)
#db.session.commit()

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.Text)
    img = db.Column(db.String(50))
    typeid = db.Column(db.Integer)

    def __init__(self, title, content, img, typeid):
        self.title = title
        self.content = content
        self.img = img
        self.typeid = typeid

    def __repr__(self):
        return '<News %r>' % self.title


#xinwen = News("1", "ewgfdgdfhggfd顶顶顶顶顶就看了较高规范和各地方哈根达斯", "hhtp://32432.dsf.jpg", 1)
#db.session.add(xinwen)
#db.session.commit()

class User_type(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    typeid = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)

    def __init__(self, userid, typeid, num):
        self.userid = userid
        self.typeid = typeid
        self.num = num

    def __repr__(self):
        return '<User_type %r>' % (self.userid+self.typeid)



def add(user, password):
    user = User(user=user, password=password)
    db.session.add(user)
    db.session.commit()

def query(user):
    usero = User.query.filter_by(username=user).first()
    return usero

def delete(user):
    usero = User.query.filter_by(username=user).first()
    db.session.delete(usero)
    db.session.commit()


def update(user, password)
    User.query.filter_by(user='name').update({'password': password})
    db.session.commit()
