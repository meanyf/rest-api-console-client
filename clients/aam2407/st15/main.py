if __name__ == '__main__':
    from group import Group
else:
    from .group import Group



def main():
    print("hi")
    group = Group()

    def switch_to_pickle():
        group.send_storage_type('pickle')

    def switch_to_db():
        group.send_storage_type('db')
        

    menu = [
        ["Добавить студента", group.addStudent],
        ["Добавить старосту", group.addHeadStudent],
        ["Редактировать студента", group.editStudent],
        ["Удалить студента", group.delete],
        ["Показать студентов", group.write],
        ["Сохранить данные", group.store],
        ["Загрузить данные", group.load],
        ["Очистить группу", group.clearAll],
        ["Сменить на PickleStorage", switch_to_pickle],
        ["Сменить на DBStorage", switch_to_db]
    ]


    while True:
        for i, menuItem in enumerate(menu, 1):
            print(f"{i}. {menuItem[0]}")
        try:
            m = int(input())
            menu[m - 1][1]()
            group.write()
        except (ValueError, IndexError):
            print("Неверный выбор, попробуйте снова.")
            
if __name__ == '__main__':
    print('callmain')
    main()


