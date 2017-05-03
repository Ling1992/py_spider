# -*- coding: utf-8 -*-

# Scrapy settings for toutiao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'toutiao'

SPIDER_MODULES = ['toutiao.spiders']
NEWSPIDER_MODULE = 'toutiao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# log
# LOG_FILE = 'log.txt'
# LOG_ENABLED = True
# LOG_ENCODING = 'utf-8'
# LOG_LEVEL = 'DEBUG'
# LOG_STDOUT = True

# pipelines 设置
ITEM_PIPELINES = {
   'toutiao.pipelines.ToutiaoPipeline': 300,
}
# 设置爬虫爬取的最大深度
DEPTH_LIMIT = 100

# MYSQL
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'ling_python_test1'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'


