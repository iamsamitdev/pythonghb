import pymysql
from connectdb import connectmysql as con

# ฟังก์ชันสำหรับแก้ไขข้อมูลในตาราง person
def updateperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สำหรับแก้ไขข้อมูล
    sql = """
        UPDATE person SET fullname='สมศักดิ์', age='40' 
        WHERE id='3'
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print('แก้ไขข้อมูลเรียบร้อยแล้ว')
    except pymysql.Error:
        print(pymysql.Error)

# เรียกใช้งานฟังก์ชัน
updateperson()