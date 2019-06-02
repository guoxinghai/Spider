import pymysql


class MysqlUtil(object):
    def __init__(self):
        # 获取数据库连接
        try:
            self.mysqlCon = pymysql.Connect(host='localhost', port=3306, db='zldb', user='root', passwd='root', charset='utf8')
        except Exception as e:
            print("Connection Error"+e)
        # 获取数据库游标
        self.mysqlCur = self.mysqlCon.cursor()

    # 写入数据
    def insert(self, data):
        sql = "insert into recruit (id,salary,occupation,position,degree,skill,workingExp) values (null,%s,%s,%s,%s,%s,%s)"
        ans = self.mysqlCur.execute(sql, data)
        if ans == 0:
            print("插入数据出错!")

    # 将事务提交
    def commit(self):
        self.mysqlCon.commit()
