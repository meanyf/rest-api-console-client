import datetime, requests, json
from .Student import Student
from .HeadStudent import HeadStudent




def dateconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

class RestStorage:
    def __init__(self, name):
        self.name = name
        self.url = f'http://127.0.0.1:5000/{self.name}/api/'

    def doRequest(self, method, cmd="", data=""):
        try:
            url = f'http://127.0.0.1:5000/{self.name}/api/'
            header = None
            if (len(data)):
                header = {"Content-type": 'application/json'}
            res = method(url + cmd, headers=header, data=json.dumps(data, default=dateconverter))
            if res.status_code == 200:
                if res.content:
                    return json.loads(res.content)
                else:
                    return None
        except Exception as ex:
            print(ex)

    def Load(self):
        pass

    def Store(self):
        pass

    def Clear(self):
        self.doRequest(requests.delete)

    def GetItem(self, id):
        item = Student()
        if int(id) > 0:
            res = self.doRequest(requests.get, str(id))
            if res is None:
                item = None
            else:
                if len(res) == 5:  # Проверяем, есть ли 4-й элемент (scholarship_bonus)
                    item = HeadStudent(id=res['id'], name=res['name'], age =res['age'], grade=res['grade'], scholarship_bonus=res['scholarship_bonus'])
                else:
                    item = Student(id=res['id'], name=res['name'], age =res['age'], grade=res['grade'])
        return item

    def Add(self, item):
        print(int(item.id))
        print(str(item.id))

        if int(item.id) <= 0:
            print('POST')
            self.doRequest(requests.post, data=item.json) #item.getData
        else:
            print('PUT')
            gg = self.url+f"{item.id}"
            h = item.json
            h['id'] = item.id
            print(h)
          #  requests.put(gg, data=h)
            self.doRequest(requests.put, str(item.id), h) # str(item.id), item.json ???

    def Delete(self, id):
        self.doRequest(requests.delete, str(id))

    def GetItems(self):
        res = self.doRequest(requests.get)
        for id in res['ids']:
            yield self.GetItem(id[0])
