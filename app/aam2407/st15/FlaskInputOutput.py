from flask import render_template
from flask import request

class FlaskInputOutput:
    def __init__(self, request):
        self.form = request.form

    def Input(self, field):
        return self.form.get(field)

    def Output(self, item, string):
        return render_template(string, it=item, selfurl='/'+request.url_rule.rule.split('/')[1])
