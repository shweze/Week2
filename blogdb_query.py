import pymysql

#在users表中查询注册时间最早的十条会员信息。
def displayUsers(num):
    sql = "select * from users order by cdate asc limit %s"%num
    cursor.execute(sql)
    users = cursor.fetchall()
    print(sql)
    print("输出结果为：")
    for i in users:
        print(i)

#从两个表中查询点赞数最高的5条博客信息，要求显示字段：（博文id，标题，点赞数，会员名）
def displayFavoriteBlogs(num):
    sql = "select b.id, b.title, b.pcount, u.name from blog b left join users u on b.uid = u.id order by pcount desc limit %s"%num
    cursor.execute(sql)
    blogdb.commit()
    users = cursor.fetchall()
    print(sql)
    print("输出结果为：")
    for i in users:
        print(i)

#统计每个会员的发表博文数量（降序），要求显示字段（会员id号，姓名，博文数量）
def displayUsersSummary():
    sql = "select u.id, u.name, count(b.id) from users u left join blog b on u.id = b.uid group by u.id, u.name order by count(b.id) desc, u.name asc"
    cursor.execute(sql)
    users = cursor.fetchall()
    print(sql)
    print("输出结果为：")
    for i in users:
        print(i)

#获取会员的博文平均点赞数量最高的三位。显示字段（会员id，姓名，平均点赞数）
def displayPolularUsers(num):
    sql = "select u.id, u.name, avg(b.pcount) from users u left join blog b on u.id = b.uid group by u.id, u.name order by avg(b.pcount) desc, u.name asc limit %s"%num
    cursor.execute(sql)
    users = cursor.fetchall()
    print(sql)
    print("输出结果为：")
    for i in users:
        print(i)

#删除没有发表博文的所有会员信息
def removeNoBlogUsers():
    sql = "delete from users where id not in (select uid from blog)"
    cursor.execute(sql)
    cursor.execute("select * from users")
    users = cursor.fetchall()
    print(sql)
    print("当前剩余用户信息为：")
    for i in users:
        print(i)


try:
    #数据库初始化
    blogdb = pymysql.connect(host="localhost",user="root",password="P@ssword1",db="blogdb",charset="utf8")
    cursor = blogdb.cursor()
    print("数据库初始化完成...")

    print("在users表中查询注册时间最早的十条会员信息, SQL脚本如下：")
    displayUsers(10)

    print("="*100)

    print("从两个表中查询点赞数最高的5条博客信息, SQL脚本如下：")
    displayFavoriteBlogs(5)

    print("="*100)

    print("统计每个会员的发表博文数量（降序）信息, SQL脚本如下：")
    displayUsersSummary()

    print("="*100)

    print("统计获取会员的博文平均点赞数量最高的三位信息, SQL脚本如下：")
    displayPolularUsers(3)

    print("="*100)

    print("删除没有发表博文的所有会员信息, SQL脚本如下：")
    removeNoBlogUsers()



except Exception as err:
    print (err)

finally:
    blogdb.close()

