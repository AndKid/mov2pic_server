# -*- coding: utf-8 -*-
from lxml import etree
from parse_index import get_movie_list_title, get_movie_sort, get_movie_list
from parse_content import get_movie_title, get_movie_summary, get_movie_content
from parse_common import get_navigation, get_next_page


def parse_index(html):
    page = dict()
    selector = etree.HTML(html)
    page.update({"nav": get_navigation(selector)})
    page.update({"category": get_movie_list_title(selector)})
    page.update({"sort": get_movie_sort(selector)})
    page.update(get_movie_list(selector))  # movie_url movie_img movie_title movie_des
    page.update({"next": get_next_page(selector)})
    return page


def parse_content(html):
    page = dict()
    selector = etree.HTML(html)
    page.update({"nav": get_navigation(selector)})
    page.update({"title": get_movie_title(selector)})
    page.update({"summary": get_movie_summary(selector)})
    page.update({"content": get_movie_content(selector)})
    page.update({"next": get_next_page(selector)})
    return page

