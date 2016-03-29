import os
from flask import Flask
from flask import Response
from executor import net, parser
import json

app = Flask(__name__)


@app.route('/')
def index():
    url = "http://www.k165.com/movies.html"
    html = net.get_html_content(url)
    page = parser.parse_index(html)
    return Response(json.dumps(page, encoding="UTF-8", ensure_ascii=False, sort_keys=True))


#app.run(debug=True)