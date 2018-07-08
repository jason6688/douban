#!/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql

class QueryBuild(object):
    # cstring for Mysql"""
    def __init__(self, host, user, password, db, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.charset = charset

    def connect(self):
        self.con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db, port=self.port, charset=self.charset)

        cur = self.con.cursor()

        return cur

    def getAll(self, sql):
        try:
            cur = self.connect()
            cur.execute(sql)
            results = cur.fetchall()

            # for row in results:
            # 	lists[] = list(row)
            # 	print(list(row))

            # lists = list(results)
            # print(lists)
            return results

        except Exception as e:
            raise e
        else:
            pass
        finally:
            self.con.close()
            pass

    def query(self, sql):
        try:
            cur = self.connect()
            cur.execute(sql)
            self.con.commit()
        except Exception as e:
            raise e
        else:
            pass
        finally:
            self.con.close()
            pass

