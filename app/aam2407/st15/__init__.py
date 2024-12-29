from flask import Blueprint
from flask import redirect, url_for, request
from flask import g
from .Student import Student
from .HeadStudent import HeadStudent
from flask import jsonify

# Изменить на свой код

bp = Blueprint('st0715', __name__)

s = 'db'
from .group import group


def GetBook():
    global s
    if 'samedovgroup' not in g:
        g.samedovgroup = group(s)
    # g.samedovgroup.storage_type
    # g.samedovgroup.switch()
    # if s == "db":
    #      g.samedovgroup.storage = DBStorage()
    # elif s == "pickle":
    #      g.samedovgroup.storage = PickleStorage(g.samedovgroup)
    
    return g.samedovgroup


@bp.route("/")
def bookindex():
    return GetBook().ShowBook()


@bp.route("/showform/<int:id>")
def showform_basic(id):

    return GetBook().ShowForm(id)

@bp.route("/showform/<int:id>/<string:role>", methods=["GET"])
def showform(id, role):
    item = None
    print(role)
    if role == 'student':
        item = Student()  
    elif role == 'leader':
        print("Head")
        item = HeadStudent()  
    else:
        return "Unknown role", 400  # Обработка ошибок

    # Возвращаем форму
    return item.ShowForm(GetBook().io)  # Вызов метода ShowForm для соответствующего типа

@bp.route("/delete/<int:id>")
def deleteitem(id):
    GetBook().Delete(id)
    return redirect(url_for("st0715.bookindex"))

@bp.route("/clear", methods=['POST'])
def clear():
    GetBook().clear()
    return redirect(url_for("st0715.bookindex"))


@bp.route("/add", methods=['POST'])
def add():
    GetBook().Add()
    return redirect(url_for("st0715.bookindex"))  # Перенаправляем пользователя на главную страницу

@bp.route("/switch", methods=['POST'])
def switch():
    global s
    s = request.form.get('storage_type')
    # GetBook().switch()
    return redirect(url_for("st0715.bookindex"))  # Перенаправляем пользователя на главную страницу

@bp.route("/api/", methods=['GET'])
def apibook():
	return GetBook().APIBook()

@bp.route("/api/", methods=['POST'])
def apiadd():
	return GetBook().APIAdd()

@bp.route("/api/", methods=['DELETE'])
def apiclear():
	return GetBook().APIClear()
	
@bp.route("/api/<int:id>", methods=['GET'])
def apiget(id):
	return GetBook().APIGet(id)

@bp.route("/api/<int:id>", methods=['PUT'])
def apiset(id):
	return GetBook().APISet(id) 

@bp.route("/api/<int:id>", methods=['DELETE'])
def apidelete(id):
	return GetBook().APIDelete(id)


@bp.teardown_app_request
def teardown_book(ctx):
    GetBook().storage.Store()


