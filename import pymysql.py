import pymysql

# Connection
connection = pymysql.connect(host='rds.chzi0a331csg.ap-south-1.rds.amazonaws.com',
                             user='admin',
                             password='rootroot',
                             database='rds_sql')


def handler():
    cursor = connection.cursor()
    cursor.execute('SELECT * from user_data')
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2} {3} {4} {5} ".format(row[0], row[1], row[2], row[3], row[4], row[5]))


handler()
