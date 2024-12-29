from dataclasses import dataclass
from .Student import Student

@dataclass
class HeadStudent(Student):
    scholarship_bonus: float = 1.0  # Надбавка к стипендии

    def Show(self):
        return "HeadItem Edit"

    def SetFormData(self, io):
        super().SetFormData(io)
        self.scholarship_bonus = float(io.Input('scholarship_bonus'))

     #   print("HeadStudentForm data:", io.form)

    def ShowForm(self, io):
        return io.Output(self, 'aam2407/st15/form2.tpl')
    
    def DBLoad(self, r):
        super().DBLoad(r)
        self.scholarship_bonus = r['scholarship_bonus']

    def DBStore(self, db):
        existing_record = db.execute("SELECT * FROM book WHERE id=?", (self.id,)).fetchone()
        if not existing_record:
            db.execute("insert into book values(NULL, ?, ?, ?, ?)", (self.name, self.age, self.grade, self.scholarship_bonus))
        else:
            db.execute("update book set name=?, age=?, grade=?, scholarship_bonus=? where id=?", (self.name, self.age, self.grade, self.scholarship_bonus, self.id));
