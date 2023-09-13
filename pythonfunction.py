# การเขียนฟังก์ชันในภาษา Python
# แบบที่ 1 ฟังก์ชันที่ไม่มีการรับค่าพารามิเตอร์
# สร้างฟังก์ชัน
def hello():
    print("Hello Python")


# เรียกใช้งานฟังก์ชัน
hello()


# แบบที่ 2 ฟังก์ชันที่มีการรับค่าพารามิเตอร์
# สร้างฟังก์ชัน
def area(width=0, height=0): # default parameter
    total = width * height
    return total


# เรียกใช้งานฟังก์ชัน
print("Area is", area())
print("Area is", area(5))
print("Area is", area(5,10))