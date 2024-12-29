from dataclasses import dataclass
import os, sys, re, codecs, binascii, cgi, cgitb, datetime, pickle, sqlite3



from .Student import Student
from .HeadStudent import HeadStudent

selfpath = 'data/aam2407/st15/'

class DBStorage:
	def __init__ (self):
		self.Load()
		
	def Load(self):
		if not os.path.exists(selfpath):
			os.mkdir(selfpath)
		self.db = sqlite3.connect(selfpath+'book.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
		self.db.execute("""
			CREATE TABLE IF NOT EXISTS book(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT,
				age TEXT,
				grade TEXT,
				scholarship_bonus REAL  -- Добавлено поле для стипендии
			)
		""")
		self.db.row_factory = sqlite3.Row
		self.dbc = self.db.cursor()

		
	def Store(self):
		self.db.commit()
		self.db.close()

	def GetItem(self, id):
		item = None  # Изначально item равен None
		if id > 0:
			self.dbc.execute("select * from book where id=?", (id,))
			row = self.dbc.fetchone()  # Получаем строку из БД
			print("row:", dict(row))  # Преобразуем Row в словарь для лучшего восприятия
			if row:  # Если строка найдена
				# print(f"scholarship_bonus type: {type(row['scholarship_bonus'])}")
				# print(row['scholarship_bonus'])
				# Проверим наличие поля 'scholarship_bonus' в строке
				if row['scholarship_bonus'] is not None:
					# Если scholarship_bonus существует и не пусто, создаем HeadStudent
					print("Head")
					item = HeadStudent()
					item.DBLoad(row)
				else:
					# Если scholarship_bonus отсутствует или пусто, создаем обычного студента
					print("Student")
					item = Student()
					item.DBLoad(row)
		if item is None:
			item = Student()
		return item

	def Add(self, item):
		print(item)
		item.DBStore(self.db)
			
	def Delete(self, id):
		self.db.execute("delete from book where id=?", (id,))
		
	def GetItems(self):
		self.dbc.execute("select * from book order by id desc")
		for r in self.dbc:
			# Проверяем, есть ли значение в поле scholarship_bonus
			if r['scholarship_bonus'] is not None:  # Если поле заполнено, это староста
				item = HeadStudent()  # Создаем объект Leader
		#		item.scholarship_bonus = r['scholarship_bonus']
			else:
				item = Student()  # Создаем обычного студента
			
			item.DBLoad(r)  # Загружаем общие данные из записи
			yield(item)
			
	def Clear(self):
		self.db.execute("DELETE FROM book")
		print("Все записи удалены")