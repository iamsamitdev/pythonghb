import pymysql
from connectdb import connectmysql as con

# ฟังก์ชันสำหรับลบข้อมูลในตาราง person
def deleteperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สำหรับลบข้อมูล
    sql = """
        DELETE FROM person WHERE id='3'
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print('ลบข้อมูลเรียบร้อยแล้ว')
    except pymysql.Error:
        print(pymysql.Error)

# เรียกใช้งานฟังก์ชัน
deleteperson()