# -*- coding: utf-8 -*-
url_prefix = "http://www.wufafuwu.com"


def get_header_foreground(selector):
    foreground = selector.xpath('//div[@class="one-imagen"]/img/@src')
    return url_prefix + foreground[0]
