import pickle
import os
from .Student import Student

selfpath = 'data/aam2407/st15/'

class PickleStorage:
    def __init__(self, group):
        self.group = group
        self.items = dict()
        self.maxid = 0
        try:
            self.Load()
        except:
            self.items = dict()
            self.maxid = 0
    
    def Load(self):
        if not os.path.exists(selfpath):
            os.mkdir(selfpath)
        try:
            print("Попытка открыть файл...")
            with open(selfpath+'book.db', 'rb') as f:
                (self.maxid, self.items) = pickle.load(f)
            print("Файл успешно открыт и загружен.")
            print("maxid:", self.maxid)
        except FileNotFoundError:
            # Если файл не существует, просто пропускаем загрузку
            print("Файл 'book.db' не найден, создается новый.")
        except (pickle.UnpicklingError, EOFError) as e:
            # Обработка ошибок при распаковке данных
            print("Ошибка при загрузке данных из файла:", e)
        except Exception as e:
            # Общая обработка других возможных ошибок
            print("Произошла ошибка при открытии файла:", e)

    def Store(self):
        with open(selfpath+'book.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def GetItem(self, id):
        if id <= 0:
            return Student()
        else:
            return self.items[id]

    def Add(self, item):
        if item.id <= 0:
            self.maxid += 1;
            item.id = self.maxid
            self.items[item.id] = item

    def Delete(self, id):
        del self.items[id]

    def GetItems(self):
        for (id, item) in self.items.items():
            yield (item)

    def Clear(self):
        self.items.clear()
        self.maxid = 0  # Сбрасываем maxID на 0 после очистки