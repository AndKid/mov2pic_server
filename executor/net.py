import requests
from parserme import parse_background


def get_html_content(url):
    html = requests.get(url)
    return html.content


# parse_background(get_html_content("http://www.wufafuwu.com/a/ONE_tupian/list_11_80.html"))
