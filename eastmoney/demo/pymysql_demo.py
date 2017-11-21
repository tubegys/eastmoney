import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123',
                       db='db_gys')
# 创建游标
cursor = conn.cursor()

sql = 'insert into tb_eastmoney (title,url) values(%s,%s)'
cursor.execute(sql, ('test_title2', 'www.eastmoney.com'))
conn.commit()


