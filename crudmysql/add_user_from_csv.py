import pymysql
from connectdb import connectmysql as con
import csv

# ฟังก์ชันสำหรับอ่านข้อมูลจากไฟล์ CSV และเพิ่มข้อมูลลงในตาราง users aaaa
def readcsvandinsertusers():

    connection = con.connectdb()
    cursor = connection.cursor()

    # อ่านข้อมูลจากไฟล์ CSV
    with open('filedata/users.csv', 'r', encoding="UTF8") as csv_file:
        # สร้าง reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        # ข้าม header
        header = next(csv_reader)

        # วนลูปอ่านข้อมูลจากไฟล์ CSV และเพิ่มข้อมูลลงในตาราง users
        for row in csv_reader:
            # สร้าง SQL query สำหรับเพิ่มข้อมูล
            sql = "INSERT INTO users (name, email, mobile) VALUES (%s, %s, %s)"
            cursor.execute(sql, tuple(row))
            
    print("เพิ่มข้อมูลเรียบร้อยแล้ว")
    connection.commit()
    connection.close()

# เรียกใช้งานฟังก์ชัน
readcsvandinsertusers()