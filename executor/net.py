import requests


def get_html_content(url):
    html = requests.get(url)
    return html.content
