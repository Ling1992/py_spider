# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class ToutiaoPipeline(object):
    db = None
    cursor = None

    def __init__(self, dbpool):
        print 'ToutiaoPipeline', __name__
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        print 'ToutiaoPipeline', __name__
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        print 'ToutiaoPipeline', __name__
        self.dbpool.runInteraction(self.insert_article, item, spider)
        return item

    def close_spider(self, spider):
        print 'close spider --->>> close_spider <<<--- >>> close db link <<< '
        self.dbpool.close()

    def insert_article(self, conn, item, spider):
        print 'ToutiaoPipeline ', __name__
        print item.get('group_id')
        conn.execute('select * from article_list where group_id = %s ' % item.get('group_id'))
        res = conn.fetchall()
        print res
        if res:
            print '数据重复 ！！！'
        else:
            print '新增数据 @ @ @'
            conn.execute("insert into article_list(title, abstract, tag, group_id, original_time) VALUES ('%s', '%s', '%s', '%s', '%s')"
                         %
                         (item.get('title', default=""), item.get('abstract', default=""), item.get('tag', default=""), item.get('group_id', default=""), item.get('behot_time', default="0")))
            conn.execute("INSERT INTO article(article_id, title, article) VALUES ('%s', '%s', '%s')" % (item.get('group_id'), item.get('header'), item.get('article')))

