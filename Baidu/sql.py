import pymysql.cursors
from Baidu import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
MYSQL_CHARACTERS = settings.MYSQL_CHARACTERS

# 获取游标
connect = pymysql.Connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB,charset=MYSQL_CHARACTERS)
cur = connect.cursor()
class Sql:
    @classmethod
    def insert(cls,name, en_name,level,brief,province,address,phone,web,lon,lat,url1,url2,url3,url4):
        print("---------------------------------------------------------------")
        sql = "INSERT INTO `resort` (id, name, en_name,level,brief,province,address,phone,web,lon,lat,url1,url2,url3,url4) VALUES ( '%s', '%s', '%s' ,'%s','%s', '%s', '%s' ,'%s','%s','%s', '%s' ,'%s','%s','%s','%s')"
        value = ('0', name, en_name,level,brief,province,address,phone,web,lon,lat,url1,url2,url3,url4)
        cur.execute(sql % value)
        print(sql % value)
        connect.commit()