# -*- coding: utf-8 -*-
import re

url_prefix = "http://www.wufafuwu.com"


def get_header_background(selector):
    backgrounds = selector.xpath('//div[@class="photo-pic"]/a/img/@src')
    for index in range(0, 8):
        backgrounds[index] = url_prefix + backgrounds[index]
    return backgrounds[0:8]


def get_header_foreground_url(selector):
    urls = selector.xpath('//div[@class="photo-pic"]/a[1]/@href')
    for index in range(0, 8):
        urls[index] = url_prefix + urls[index]
    return urls[0:8]


def get_header_name(selector):
    names = selector.xpath('//div[@class="photo-pic"]/a/img/@alt')
    for index in range(0, 8):
        if '&' in names[index]:
            result = re.search(r' (.+)&', names[index])
            names[index] = result.group(1)
            # print names[index]
        else:
            strs = str.split(names[index].encode('utf-8'), " ")
            if len(strs) == 4:
                names[index] = strs[1]
            else:
                result = re.search(r' (.+) ', names[index])
                if result is None:
                    strs = str.split(names[index].encode('utf-8'), " ")
                    names[index] = strs[1]
                    # print names[index]
                else:
                    names[index] = result.group(1)
                    # print names[index]
    return names[0:8]
