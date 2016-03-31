import os
from flask import Flask
from flask import Response
from executor import net, parser
import json

app = Flask(__name__)


@app.route('/')
def index():
    url = "http://www.k165.com/movies/tag/4"
    html = net.get_html_content(url)
    page = parser.parse_index(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


@app.route('/content')
def content():
    url = "http://www.k165.com/movies/866.html"
    html = net.get_html_content(url)
    page = parser.parse_content(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


#app.run(host='127.0.0.1', debug=True)
