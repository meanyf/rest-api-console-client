from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

from app.aam2407.st15 import bp as bp0715


# добавить пункт меню для вызова своего модуля по шаблону:
bps = [
    ["[2407-15] Самедов", bp0715],
]

for i, (title, bp) in enumerate(sorted(bps), start=1):
    app.register_blueprint(bp, url_prefix=f"/st{i}")


@app.route("/")
def index():
    return render_template("index.tpl", bps=sorted(bps))


@app.route("/api/", methods=['GET'])
def api():
    sts = []
    for i, (title, bp) in enumerate(sorted(bps), start=1):
        sts.append([i, title])
    return jsonify({'sts': sts})
