from dataclasses import dataclass


@dataclass
class Student:
    id: int = 0
    name: str = ""
    age: int = 0
    grade: str = ""

    def Show(self):
        return "StudentItem Edit"

    def SetFormData(self, io):
        self.id = int(io.Input('id'))
        self.name = io.Input('name')
        self.age = io.Input('age')
        self.grade = io.Input('grade')
     #   print("StudentForm data:", io.form)

    def ShowForm(self, io):
        return io.Output(self, 'aam2407/st15/form.tpl')
    
    def DBLoad(self, r):
        self.id = r['id']
        self.name = r['name']
        self.age = r['age']
        self.grade = r['grade']
    
    def DBStore(self, db):
        print("dbstore")
        print(self.id)
        
        try:
            # Пробуем выполнить запрос
            existing_record = db.execute("SELECT * FROM book WHERE id=?", (self.id,)).fetchone()
            if not existing_record:
                print("insert")
                try:
                    db.execute("insert into book values(NULL, ?, ?, ?, NULL)", (self.name, self.age, self.grade))
                except Exception as e:
                    print(f"Ошибка при выполнении INSERT запроса: {e}")
            else:
                print("update")
                try:
                    db.execute("update book set name=?, age=?, grade=? where id=?", (self.name, self.age, self.grade, self.id))
                except Exception as e:
                    print(f"Ошибка при выполнении UPDATE запроса: {e}")
        except Exception as e:
            print(f"Произошла ошибка при сохранении данных в базу данных: {e}")



