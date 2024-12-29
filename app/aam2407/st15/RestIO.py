from flask import request
from flask import jsonify


class RestIO:
	def defaultOutput(self, book):
		return ""

	def output(self, getItems):
		ids = []
		for item in getItems:
			ids.append(item.getInfo())
		return jsonify({'ids': ids})

	def Input(self, field, title=None, default=None):
		return request.json.get(field, default)

	def outputItem(self, item):
		if item:
			return jsonify(item.getData())
		return ""

	def editItem(self, item):
		pass

