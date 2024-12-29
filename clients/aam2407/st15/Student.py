from dataclasses import dataclass
try:
    from .ConsoleIO import ConsoleIO
except ImportError:
    from ConsoleIO import ConsoleIO

@dataclass
class Student:
    id: int = 0
    name: str = ""
    age: int = 0
    grade: str = ""

    
    # def __post_init__(self):
    #     self.io = ConsoleIO()
        
    @property
    def json(self):
        # Преобразование в JSON-совместимый формат
        return {
            'id': 0,
            'name': self.name,
            'age': self.age,
            'grade' : self.grade,
            'role' : "student"
        }
    
    def read(self, io):
        self.name = io.Input('Имя')
        self.age = int(io.Input('Возраст'))
        self.grade = io.Input('Класс/Группа')

    def write(self, io):
        io.Output('ID', self.id)
        io.Output('Имя', self.name)
        io.Output('Возраст', self.age)
        io.Output('Класс/Группа', self.grade)

        
