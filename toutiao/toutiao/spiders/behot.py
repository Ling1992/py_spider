# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from bs4 import BeautifulSoup
import json
import re
import time
from ..items import ToutiaoItem

import sys
reload(sys)
sys.setdefaultencoding("utf8")


class BehotSpider(Spider):
    name = "behot"
    domain = 'http://www.toutiao.com'
    start_urls = ['http://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=false']
    headers = {}

    def parse(self, response):
        print response.headers
        print response.request.headers
        result = json.loads(response.body)
        for data in result['data']:
            item = ToutiaoItem()
            print data
            if data.get('has_gallery'):
                continue
            if data.get('has_video'):
                continue
            if data.get('source_url') == '':
                continue
            if not data.get('middle_mode'):
                continue
            article_url = ''.join([self.domain, data.get('source_url')])
            print article_url
            item['group_id'] = data.get('group_id')
            item['title'] = data.get('title')
            item['abstract'] = data.get('abstract')
            item['tag'] = data.get('tag')
            item['behot_time'] = data.get('behot_time')
            try:
                yield Request(article_url, callback=self.article, dont_filter=True, meta={'item': item})
            except Exception, e:
                print 'out 1'
                print e.message
                continue
        time.sleep(1)
        # try:
        #     yield Request(self.start_urls[0], callback=self.parse, dont_filter=True)
        # except Exception, e:
        #     print 'out 2'
        #     print e.message
        print '111'

    def article(self, response):
        item = response.meta['item']
        print 'get_article'
        """
             bs4 html 操作
        """
        soup = BeautifulSoup(response.body, 'html.parser')
        header = soup.select('header > h1')
        if not header or not len(header):
            print 'header if 1'
            header = soup.find('h1', class_='article-title')
        else:
            header = header[0]
        if not header or not len(header):
            print 'header if 2'
            header = soup.find('h1')
        if not header or not len(header):
            raise Exception('header is none or []')
        header, number = re.subn("'", "\\'", str(header))
        item['header'] = header

        article = soup.find('article')
        if not article or not len(article):
            print 'article if 1'
            figure = soup.find_all('figure')
            article = ''
            for i in figure:
                article = ''.join([article, str(i)])
        if not article or not len(article):
            print 'article if 2'
            article = soup.find('div', class_='article-content')
        if not article or not len(article):
            print 'article if 3'
            div = soup.find('div', class_='text')
            p = div.find_all('p')
            article = ''
            for i in p:
                article = ''.join([article, str(i)])
        if not article or not len(article):
            raise Exception('article is none or []')
        article, number = re.subn("'", "\\'", str(article))
        item['article'] = article

        return item

