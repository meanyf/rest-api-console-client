
import clients.aam2407.st15.main


MENU = [

    ["[2407-15] Самедов", clients.aam2407.st15.main.main],

]


def menu():
    print("------------------------------")
    for i, item in enumerate(sorted(MENU)):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())

try:
    while True:
        sorted(MENU)[menu()][1]()
except Exception as ex:
    print(ex, "\nbye")
