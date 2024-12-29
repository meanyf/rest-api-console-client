import datetime, requests, json
from .Student import Student

def dateconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

class RestStorage:
	def __init__(self, name):
		self.name = name

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
			if res:
				item.setData(res)
			else:
				item = None
		return item

	def Add(self, item):
		if int(item.id) <= 0:
			self.doRequest(requests.post, data=item.getData())
		else:
			self.doRequest(requests.put, str(item.id), item.getData())

	def Delete(self, id):
		self.doRequest(requests.delete, str(id))

	def GetItems(self):
		res = self.doRequest(requests.get)
		for (id, title) in res['ids']:
			yield self.getItem(id)
