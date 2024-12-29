try:
    from .PickleStorage import PickleStorage
    from .RestStorage import RestStorage
    from .Student import Student
    from .HeadStudent import HeadStudent
    from .ConsoleIO import ConsoleIO
except ImportError:
    from PickleStorage import PickleStorage
    from RestStorage import RestStorage
    from Student import Student
    from HeadStudent import HeadStudent
    from ConsoleIO import ConsoleIO


import requests
import json

def DoRequest(method, st="", cmd="", data=""):
       # print(f"Method: {method.__name__}")  # Имя функции
        print(f"st: {st}")  # Аргумент st
        try:
            if not isinstance(st, str):
                raise TypeError(f"Expected st to be a string, but got {type(st)}")
            url = 'http://127.0.0.1:5000/'+st+'api/'
            print(url+cmd)
            header = None
            if(len(data)):
                header = {"Content-type": 'application/json'}
            res = method(url+cmd, headers=header, data=json.dumps(data))
            if res.status_code == 200:
                return json.loads(res.content)
        except requests.exceptions.RequestException as e:
            # Логируем ошибку запроса (например, проблемы с сетью)
            print(f"Request error: {e}")
            raise Exception(f"Request failed: {str(e)}")
        except Exception as e:
            # Логируем другие ошибки
            print(f"An error occurred: {e}")
            raise Exception(f"An error occurred: {str(e)}")

def getlist():
    res = DoRequest(requests.get)
    target_title = "[2407-15]"
    found_id = None  # Переменная для хранения найденного id
    
    for i, title in res['sts']:
        if target_title in title:  # Проверяем, содержится ли подстрока в title
            found_id = i  # Сохраняем найденный id
            print(f"Found: id = {i}, title = {title}")
            break  # Прерываем цикл, если нашли
    
    return found_id  # Возвращаем найденный id, если он был найден

# st = f'st{getlist()}/'
# url = 'http://127.0.0.1:5000/'+ st +'api/'




class Group:
    def __init__(self):
    #    self.maxID = 0
        self.st =  f'st{getlist()}/'
        self.url = 'http://127.0.0.1:5000/'+ self.st +'api/'
        self.io = ConsoleIO()
        # ]self.storage = PickleStorage(self)
        self.storage = RestStorage(self.st)
        self.write()

    def addStudent(self):
        group = Student()
        group.read(self.io)
        self.storage.Add(group)
                
    def addHeadStudent(self):       
        group = HeadStudent()
        group.read(self.io)
        self.storage.Add(group)
        
    def editStudent(self):
        id = int(input("Введите ID студента, которого хотите изменить: "))
        group = self.storage.GetItem(id)
        if group is None:
                print("Такого ID нет")
                return
        print(group)
        group.read(self.io)
        print(group.id)
        self.storage.Add(group)


    def write(self):
        pass
        for group in self.storage.GetItems():         
                group.write(self.io)
                print('')
            

    def store(self):
        self.storage.Store()

    def load(self):
        self.storage.Load()

    def delete(self):
        id = int(input("id: "))
        group = self.storage.GetItem(id)
        if group is None:
                print("Такого ID нет")
                return
        self.storage.Delete(id)
            
    def clearAll(self):
      #  requests.delete(self.url)
        self.storage.Clear()
        print("Все студенты удалены.")

    def send_storage_type(self, storage_type):

        gg = 'http://127.0.0.1:5000/' + self.st + 'switch'

        if storage_type not in ['db', 'pickle']:
            raise ValueError("Invalid storage_type. Choose 'db' or 'pickle'.")
        
        data = {
            'storage_type': storage_type
        }
        
        requests.post(gg, data=data)


