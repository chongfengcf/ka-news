from flask import request, jsonify, Response

from flaskapp import app
from service import news_get, typenews_get, contentnews_get, login, register, usertype_add, history_get


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/news', methods=['GET','POST'])
def news():
    pages = int(request.values.get("pages"))
    type = int(request.values.get("type"))
    res = None
    if type==0:
        res = news_get(pages)
    else:
        res = typenews_get(pages, type)

    return jsonify(res)

@app.route("/image/<imagename>")
def displayimg(imagename):
    with open("img/{}".format(imagename), 'rb') as f:
        image = f.read()
    resp = Response(image, mimetype="image/jpeg")
    return resp

@app.route("/content/<int:id>")
def newscontent(id):
    userid = request.values.get("userid")
    type = request.values.get("type")
    content = contentnews_get(id)
    if userid!="null":
        usertype_add(userid, type)
    return jsonify(content)

@app.route("/login", methods=['POST'])
def delu():
    user = request.values.get("user")
    password = request.values.get("password")
    return str(login(user, password))

@app.route("/register", methods=['POST'])
def zhuce():
    user = request.values.get("user")
    password = request.values.get("password")
    return str(register(user, password))

@app.route("/history/<int:id>")
def history(id):
    return jsonify(history_get(id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)