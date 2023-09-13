print("Login System")

# การรับค่าจากผู้ใช้ใน python
username = input("Username: ")
password = input("Password: ")
# print(type(username))
# print(username + 10)

# ตรวจเงื่อนไขการ login
if username.strip().lower() == "admin" and password.strip().lower() == "1234":
    print("Login Success")
else:
    print("Login Failed")


