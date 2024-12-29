class ConsoleIO:
    def Input(self, field, defvalue=None):
        return input(f"{field}: ")
    
    def Output(self, title, field):
        print(f"{title}: {field}")