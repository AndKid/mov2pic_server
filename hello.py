import os
from flask import Flask
from flask import Response
from flask import request
from executor import net, parserme
import json
import random

app = Flask(__name__)


@app.route('/')
def index():
    uri = request.args.get("uri", "")
    if uri == "":
        url = "http://www.k165.com/movies"
    else:
        url = "http://www.k165.com" + uri
    html = net.get_html_content(url)
    page = parserme.parse_index(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


@app.route('/content')
def content():
    uri = request.args.get("uri", "")
    if uri == "":
        url = "http://www.k165.com/movies/1536.html"
    else:
        url = "http://www.k165.com" + uri
    html = net.get_html_content(url)
    page = parserme.parse_content(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


@app.route('/background')
def background():
    number = random.randint(1, 107)
    url_prefix = "http://www.wufafuwu.com/a/ONE_tupian/list_11_"
    url_suffix = ".html"
    url = url_prefix + str(number) + url_suffix
    html = net.get_html_content(url)
    page = parserme.parse_background(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


@app.route('/foreground')
def foreground():
    url = request.args.get("url", "")
    html = net.get_html_content(url)
    page = parserme.parse_foreground(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


# app.run(host='127.0.0.1', debug=True)
