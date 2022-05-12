from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)
def waf(s):
    no=['flag','eval','os','system']
    for i in no:
        if i in s:
            return 'Hacker'
    return s
@app.route("/")
def index():
    name = request.args.get('name', 'guest')
    name=waf(name)
    t = Template("Hello " + name+" And your name?")
    return t.render()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
