#!/usr/bin/env python
# encoding: utf-8


import psycopg2


# cur.execute('SELECT * FROM "Customer"')
# res = cur.fetchall()
# for user in res:
#     print(user)


# 连接数据库
def connect_pgsql():
    # 连接数据库
    conn = psycopg2.connect(database='proj1part2', user='wz2500', password='4111', host='34.74.165.156')
    
   # 创建游标
    cur = conn.cursor()
    return conn, cur


# 关闭数据库
def close_pgsql(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


# 查询
def execute_select(sql):
    conn, cur = connect_pgsql()
    cur.execute(sql)
    res = cur.fetchall()
    close_pgsql(conn, cur)
    return res


# 添加, 修改， 删除
def execute_add_mod_del(sql, return_id=False):
    conn, cur = connect_pgsql()
    try:
        cur.execute(sql)
        if return_id:
            insert_id = cur.fetchone()[0]
            close_pgsql(conn, cur)
            return insert_id
        else:
            close_pgsql(conn, cur)
            return True
    except:
        close_pgsql(conn, cur)
        return False
