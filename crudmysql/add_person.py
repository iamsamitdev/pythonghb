import pymysql
from connectdb import connectmysql as con

# ฟังก์ชันสำหรับเพิ่มข้อมูลเข้าตาราง person
def addperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สำหรับเพิ่มข้อมูล
    sql = """
        INSERT INTO person (fullname, email, age) 
        VALUES ('วินัย', 'winai@email.com', '42')
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print('เพิ่มข้อมูลเรียบร้อยแล้ว')
    except pymysql.Error:
        print(pymysql.Error)

# เรียกใช้งานฟังก์ชัน
addperson()