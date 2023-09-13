import pymysql
from connectdb import connectmysql as con
from tabulate import tabulate

# ฟังก์ชันสำหรับอ่านข้อมูลจากตาราง person
def readperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL อ่านข้อมูล
    sql = """
        SELECT * FROM person
    """

    try:
        cursor.execute(sql)
        connection.commit()
        # ดึงข้อมูลทั้งหมด
        # result = cursor.fetchall()
        # for row in result:
        #     print(row['fullname'], row['email'], row['age'])
        headers = {
            "id":"ID", "fullname":"Full Name", "email":"Email", "age":"Age"
        }
        print(tabulate(cursor,headers=headers, tablefmt="pretty")) # plain, simple, pretty, github
    except pymysql.Error:
        print(pymysql.Error)

# เรียกใช้งานฟังก์ชัน
readperson()