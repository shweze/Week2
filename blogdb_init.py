import pymysql
import os

#构造数据表方法
def generateTable(tablename, **columns):
    i = 0
    script = "create table if not exists {0} (".format(tablename)
    count = len(columns)
    for k,v in columns.items():
        i = i + 1
        if i == count:
            script = script + k + " " + v + ")"
        else:
            script = script + k + " " + v + ", "
    return script

#初始化数据（users）
def initUsersData(*user):
    sql = "insert into users (name, email, cdate) values {0}".format(user)
    cursor.execute(sql)
    blogdb.commit()

#初始化数据（blog）
def initBlogData(*blog):
    sql = "insert into blog (title, abstract, content, uid, pcount, flag, cdate) values {0}".format(blog)
    cursor.execute(sql)
    blogdb.commit()

#清理数据
def truncateTable():
    cursor.execute("truncate table users")
    cursor.execute("truncate table blog")
    blogdb.commit()

try:
    #数据库初始化
    blogdb = pymysql.connect(host="localhost",user="root",password="P@ssword1",db="mysql",charset="utf8")
    cursor = blogdb.cursor()

    cursor.execute("drop database if exists blogdb")
    cursor.execute("create database if not exists blogdb default character set utf8 ")
    blogdb.select_db("blogdb")
    print("数据库初始化完成...")

    #创建会员信息表（users）
    #定义表结构
    columns_users = {
        "id" : "int unsigned not null auto_increment PRIMARY KEY",
        "name" : "varchar(32) not null unique",
        "email" : "varchar(100)", 
        "cdate" : "datetime"
    }

    sql_create_table_users = generateTable("users", **columns_users)
    print (sql_create_table_users)
    cursor.execute(sql_create_table_users)
    print("会员信息表生成成功...")

    #创建博客信息表（blog）
    #定义表结构
    columns_blog = {
        "id" : "int unsigned not null auto_increment PRIMARY KEY",
        "title" : "varchar(100) not null",
        "abstract" : "varchar(200) not null", 
        "content" : "text not null",
        "uid" : "int unsigned",
        "pcount" : "int unsigned default 0",
        "flag" : "tinyint unsigned default 0",
        "cdate" : "datetime"
    }
    sql_create_table_blog = generateTable("blog", **columns_blog)
    print(sql_create_table_blog)
    cursor.execute(sql_create_table_blog)
    print("博客信息表生成成功...")

    #清理数据，使程序可多次执行
    truncateTable()
    print("历史数据初始化成功...")

    #初始化会员信息表数据
    initUsersData("John","john@163.com","2018-5-16 17:23:32")
    initUsersData("Abby","abby@163.com","2018-5-20 12:20:13")
    initUsersData("Barry","barry@163.com","2018-4-26 15:12:32")
    initUsersData("Lily","lily@163.com","2018-3-16 10:13:22")
    initUsersData("George","george@163.com","2018-5-26 07:20:32")
    initUsersData("Thomas","thomas@163.com","2018-1-2 10:23:12")
    print("会员信息数据初始化成功...")

    #初始化博客信息表数据
    initBlogData("人生苦短 我学python", "人生苦短 我学python - abstract", "人生苦短 我学python - content", 1, 100, 1, "2018-5-20 10:22:41")
    initBlogData("人生苦短 我学python1", "人生苦短 我学python - abstract1", "人生苦短 我学python - content1", 2, 500, 1, "2018-5-21 10:22:41")
    initBlogData("人生苦短 我学python2", "人生苦短 我学python - abstract2", "人生苦短 我学python - content2", 3, 20, 2, "2018-5-22 10:22:41")
    initBlogData("人生苦短 我学python3", "人生苦短 我学python - abstract3", "人生苦短 我学python - content3", 1, 850, 1, "2018-5-23 10:22:41")
    initBlogData("人生苦短 我学python4", "人生苦短 我学python - abstract4", "人生苦短 我学python - content4", 5, 300, 1, "2018-5-24 10:22:41")
    initBlogData("人生苦短 我学python5", "人生苦短 我学python - abstract5", "人生苦短 我学python - content5", 1, 0, 0, "2018-5-22 12:22:41")
    initBlogData("人生苦短 我学python6", "人生苦短 我学python - abstract6", "人生苦短 我学python - content6", 2, 130, 1, "2018-5-21 10:22:41")
    initBlogData("人生苦短 我学python7", "人生苦短 我学python - abstract7", "人生苦短 我学python - content7", 6, 10, 1, "2018-5-22 10:22:41")
    initBlogData("人生苦短 我学python8", "人生苦短 我学python - abstract8", "人生苦短 我学python - content8", 1, 800, 0, "2018-5-23 10:22:41")
    initBlogData("人生苦短 我学python9", "人生苦短 我学python - abstract9", "人生苦短 我学python - content9", 3, 80, 1, "2018-5-25 10:22:41")
    initBlogData("人生苦短 我学python10", "人生苦短 我学python - abstract10", "人生苦短 我学python - content10", 1, 300, 1, "2018-5-21 10:22:41")
    initBlogData("人生苦短 我学python11", "人生苦短 我学python - abstract11", "人生苦短 我学python - content11", 2, 600, 1, "2018-5-20 10:22:41")
    initBlogData("人生苦短 我学python12", "人生苦短 我学python - abstract12", "人生苦短 我学python - content12", 5, 400, 1, "2018-5-22 10:22:41")
    initBlogData("人生苦短 我学python13", "人生苦短 我学python - abstract13", "人生苦短 我学python - content13", 6, 100, 2, "2018-5-24 10:22:41")
    initBlogData("人生苦短 我学python14", "人生苦短 我学python - abstract14", "人生苦短 我学python - content14", 1, 900, 1, "2018-5-25 10:22:41")
    print("博客信息数据初始化成功...")

    #导出文件
    os.system('/Applications/XAMPP/xamppfiles/bin/mysqldump -u root -pP@ssword1 blogdb > blogdb.sql')
    print("数据库导出成功...")

except Exception as err:
    print (err)

finally:
    blogdb.close()