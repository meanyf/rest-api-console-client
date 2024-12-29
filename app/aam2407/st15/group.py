from flask import render_template
from flask import request
from .PickleStorage import PickleStorage
from .DBStorage import DBStorage
from .FlaskInputOutput import FlaskInputOutput
from .Student import Student
from .HeadStudent import HeadStudent
from .RestIO import RestIO
from flask import jsonify
from collections import OrderedDict
import json
from flask import Response


class group:

    def __init__(self, storage_type="db"):
        self.restio = RestIO()
        # Условие для выбора типа хранилища
        if storage_type == "db":
            self.storage = DBStorage()  # Используем DBStorage
        elif storage_type == "pickle":
            self.storage = PickleStorage(self)  # Используем PickleStorage
        else:
            raise ValueError("Invalid storage type")
        
        self.io = FlaskInputOutput(request)  # Инициализация IO
        self.storage_type = storage_type  #

    def ShowBook(self):
        print("Storage : " +type(self.storage).__name__)  # Выведет 'DBStorage' или 'PickleStorage'
        return render_template('aam2407/st15/group.tpl', selfurl='/'+request.url_rule.rule.split('/')[1], items=self.storage.GetItems())

    def f(self):
        return render_template("aam2407/st15/index.tpl", s="aam2407.st15.group.f()", selfurl='/'+request.url_rule.rule.split('/')[1])

    def clear(self):
        self.storage.Clear()
        # self.storage.items.clear()
        # self.storage.maxid = 0  # Сбрасываем maxID на 0 после очистки
        print("Все студенты удалены.")
        return self.ShowBook()
      
    def Add(self):
        print("forma : ")
        print(self.io.form)  # Это выведет все данные, отправленные из формы
        role = self.io.Input('role')  # Получаем роль из формы
        print("Role:", role)  # Выводим роль
        item = None
        id = int(self.io.Input('id'))
        print(list(self.storage.GetItems()))
        if id in [item.id for item in self.storage.GetItems()]:
            # Ключ существует
            print("Меняем существующий")
            item = self.storage.GetItem(id)
        else:
            # Ключ не существует
            print("Добавляем новый" + str(id))
            item = None
        # Создаем экземпляр нужного класса в зависимости от роли
        if item is None:
            if role == 'leader':  # Если это староста
                item = HeadStudent()  # Создаем объект HeadStudent
            else:  # По умолчанию создаем студента
                item = Student()  # Создаем объект Student
        item.SetFormData(self.io)
        print(item)
        self.storage.Add(item);
        return self.ShowBook()

    def Delete(self, id):
        self.storage.Delete(id)
        return self.ShowBook()
        
    def ShowForm(self, id):
        return self.storage.GetItem(id).ShowForm(self.io)
    
    def APIBook(self):
        ids = []
        for item in self.storage.GetItems():
            # Проверяем наличие атрибута scholarship_bonus
            if hasattr(item, 'scholarship_bonus'):
                ids.append([item.id, item.name, item.age, item.grade, item.scholarship_bonus])
            else:
                ids.append([item.id, item.name, item.age, item.grade])
        return jsonify({'ids': ids})
        
    def APIAdd(self):
        # self.io = RestIO()
        print('**********************')
        print(request.json)
        item = None
      #  item = self.storage.GetItem(0)
       # Извлекаем данные из JSON
        role = request.json.get('role')  # Получаем значение 'role' из JSON
        print ()
        # В зависимости от значения 'role', создаем соответствующий объект
        if role == 'student':
            item = Student()  # Если роль 'student', создаем объект Student
        elif role == 'leader':
            item = HeadStudent()  # Если роль 'leader', создаем объект HeadStudent
        print(item)
        try:
            item.SetFormData(self.restio)
        except Exception as e:
            # Логируем или выводим ошибку
            print(f"Произошла ошибка при вызове SetFormData: {e}")
        print(item)
        try:
            print("adding to storage")
            self.storage.Add(item)
        except Exception as e:
            print(f"Произошла ошибка при добавлении элемента: {e}")

        return ''
        
    def APIGet(self, id):
        item = self.storage.GetItem(id)
        print(item.__dict__)
        item = self.storage.GetItem(id)
        
        # Собираем данные в нужном порядке
        response_data = {
            'id': item.id,
            'name': item.name,
            'age': item.age,
            'grade': item.grade
        }
        
        # Если объект HeadStudent, добавляем scholarship_bonus
        if isinstance(item, HeadStudent):
            response_data['scholarship_bonus'] = item.scholarship_bonus
        
        # Ручная сериализация с гарантированным порядком
        json_response = json.dumps(response_data, indent=4)
        
        # Возвращаем Response с сериализованным JSON
        return Response(json_response, mimetype='application/json')
        
    def APISet(self, id):
        item = self.storage.GetItem(id)
        print("APISet")
        print(item)
        item.SetFormData(self.restio)
        self.storage.Add(item);
        return ''
        
    def APIDelete(self, id):
        self.storage.Delete(id)
        return ''
    
    def APIClear(self):
        self.storage.Clear()
        return ''

    