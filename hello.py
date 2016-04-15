import os
from flask import Flask
from flask import Response
from flask import request
from executor import net, parser
import json

app = Flask(__name__)


@app.route('/')
def index():
    uri = request.args.get("uri", "")
    if uri == "":
        url = "http://www.k165.com/movies"
    else:
        url = "http://www.k165.com" + uri
    html = net.get_html_content(url)
    page = parser.parse_index(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


@app.route('/content')
def content():
    uri = request.args.get("uri", "")
    if uri == "":
        url = "http://www.k165.com/movies/1536.html"
    else:
        url = "http://www.k165.com" + uri
    html = net.get_html_content(url)
    page = parser.parse_content(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


#app.run(host='127.0.0.1', debug=True)
