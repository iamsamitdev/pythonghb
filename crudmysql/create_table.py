import pymysql
from module import connectmysql as con

# ฟังก์ชันสำหรับสร้างตาราง
def createtable():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สร้างตาราง
    sql = """
        CREATE TABLE person(
            id INT PRIMARY KEY AUTO_INCREMENT,
            fullname VARCHAR(128) NOT NULL,
            email VARCHAR(64) NOT NULL,
            age INT NOT NULL
        )
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print('สร้างตารางเรียบร้อยแล้ว')
    except pymysql.Error:
        print(pymysql.Error)

# เรียกใช้งานฟังก์ชัน
createtable()