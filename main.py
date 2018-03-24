from flask import Flask, request
#los py files del handler folder
from handler.messages import MsgHandler

app = Flask(__name__)


@app.route("/MessagingApp")
def home():
    return "Welcome to the social messaging application!"

@app.route("/MessagingApp/login")
def login():
    return "Login successful"

#get all of the messages
@app.route("/MessagingApp/msg")
def msg():
    handler = MsgHandler()
    return handler.getAllMsg()

@app.route("/MessagingApp/msg/<int:msg_id>")
def getMsgById(msg_id):
    return MsgHandler().getMsgById(msg_id)

#@app.route("/MessagingApp/msg/author/")
#Get all auhors... doesn't make much sense anyway so I'll leave it empty for now

@app.route("/MessagingApp/msg/author/<int:msg_id>")
def getAuthorByMsgId(msg_id):
    return MsgHandler().getAuthorByMsgId(msg_id)

@app.route("/MessagingApp/msg/text/<int:msg_id>")
def getTextByMsgId(msg_id):
    return MsgHandler().getTextByMsgId(msg_id)

@app.route("/MessagingApp/msg/likes/<int:msg_id>")
def getLikesByMsgId(msg_id):
    return MsgHandler().getLikesByMsgId(msg_id)

@app.route("/MessagingApp/msg/dislikes/<int:msg_id>")
def getDislikesByMsgId(msg_id):
    return MsgHandler().getDislikesByMsgId(msg_id)

if __name__ == '__main__':
    app.run()

#######################################################################
#Lo del profe
# @app.route('/PartApp/parts')
# def parts():
#     if request.args:
#         return PartHandelr().searchParts(request.args)
#     else:
#         handler = PartHandelr()
#         return handler.getAllParts()
#
# @app.route('/PartApp/parts/<int:pid>')
# def getPartById(pid):
#     return PartHandelr().getPartById(pid)
#
# @app.route('/PartApp/parts/<int:pid>/suppliers')
# def getSuppliersPartById(pid):
#     return PartHandelr().getSuppliersByPartId(pid)
#
# if __name__ == '__main__':
#     app.run()