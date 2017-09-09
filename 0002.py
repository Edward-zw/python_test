import random
import pymysql

conn = pymysql.connect(user="root", database="test")
cursor = conn.cursor()
cursor.execute('create table tickets (id varchar(20) PRIMARY KEY, tic varchar(30))')

n = 200
while n:
    tic = ''
    i = 4
    while i:
        tic = tic + ''.join(random.sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', 4)) + '-'
        i = i - 1
    tic = tic.rstrip('-')
    x = 201 - n
    cursor.execute('insert into tickets (id, tic) values (%s, %s)', [str(x), tic])
    print(tic)
    n = n -1
conn.commit()
cursor.close()
conn.close()
