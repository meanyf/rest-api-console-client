# from flask import redirect, url_for
# from flask import g
# from app.aam2407.st15.Student import Student
# from app.aam2407.st15.group import group

# from app.aam2407.st15 import bp

# def GetBook():
#     if 'samedovgroup' not in g:
#         g.samedovgroup = group()
#     return g.samedovgroup

# @bp.route("/")
# def bookindex():
# 	return GetBook().ShowBook()


# @bp.route("/showform/<int:id>")
# def showform_basic(id):
#     return GetBook().ShowForm(id)

# @bp.route("/showform/<int:id>/<string:role>", methods=["GET"])
# def showform(id, role):
#     item = None

#     if role == 'student':
#         item = Student()  
#     # elif role == 'leader':
#     #     print("Head")
#     #     item = HeadStudent()  
#     else:
#         return "Unknown role", 400  # Обработка ошибок

#     # Возвращаем форму
#     return item.ShowForm(GetBook().io)  # Вызов метода ShowForm для соответствующего типа

# @bp.route("/delete/<int:id>")
# def deleteitem(id):
#     GetBook().Delete(id)
#     return redirect(url_for("st0715.bookindex"))

# @bp.route("/clear", methods=['POST'])
# def clear():
#     GetBook().clear()
#     return redirect(url_for("st0715.bookindex"))


# @bp.route("/add", methods=['POST'])
# def add():
#     GetBook().Add()
#     return redirect(url_for("st0715.bookindex"))  # Перенаправляем пользователя на главную страницу

# @bp.teardown_app_request
# def teardown_book(ctx):
#     GetBook().storage.Store()