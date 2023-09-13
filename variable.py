# สร้างตัวแปรเก็บข้อมูลชนิดต่างๆ
a = 10
b = 3.14
c = "Hello"

print(a)
print(b)
print(c)

# แสดงชนิดข้อมูล
print(type(a))
print(type(b))
print(type(c))

# ข้อมูลต่างชนิดกันสามารถบวกกันได้หรือไม่
print(a + b)  # ได้
# print(b + c)  # ไม่ได้

# การแปลงชนิดข้อมูล
print(int(b))
print(float(a))

# ตัวแปรแบบ boolean
status = True
msg = False

print(status)
print(msg)
print(type(status))

# True == 1 and False == 0
print(status == 1)
print(msg == 0)

# การแสดงผลตัวร่วมกับข้อความ
price = 200.50
qty = 5

# ตัวอย่างการแสดงผลร่วมกัน
# แบบที่ 1
print("ราคาสินค้า", "{:.2f}".format(price), "บาท จำนวน", qty, "ชิ้น")

# แบบที่ 2
print("ราคาสินค้า %.2f บาท จำนวน %d ชิ้น" % (price, qty))

# แบบที่ 3
print(f"ราคาสินค้า {price:.2f} บาท จำนวน {qty} ชิ้น")