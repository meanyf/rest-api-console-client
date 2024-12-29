from dataclasses import dataclass
try:
    from .Student import Student
except ImportError:
    from Student import Student

@dataclass
class HeadStudent(Student):
    scholarship_bonus: float = 0.0  # Надбавка к стипендии

    @property
    def json(self):
        # Преобразование в JSON-совместимый формат
        return {
            'id': 0,
            'name': self.name,
            'age': self.age,
            'grade' : self.grade,
            'scholarship_bonus' : self.scholarship_bonus,
            'role' : "leader"
        }
    def read(self, io):
        super().read(io)
        self.scholarship_bonus = float(io.Input('Надбавка к стипендии'))

    def write(self, io):
        super().write(io)
        io.Output('Надбавка к стипендии', f'{self.scholarship_bonus} руб.')