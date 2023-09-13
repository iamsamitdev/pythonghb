# การ import module ทั้งหมด
# import module

# print(module.calculator.plus(3,5)) # 3 + 5 = 8
# print(module.number.factorial(5)) # 5! = 5 * 4 * 3 * 2 * 1 = 120

# การ import บางส่วนของ module ที่เราสร้างขึ้นมา
# from module import calculator, number

# print(calculator.plus(3,5)) # 3 + 5 = 8
# print(number.factorial(5)) # 5! = 5 * 4 * 3 * 2 * 1 = 120

# การ import บางส่วนของ module ที่เราสร้างขึ้นมา และเปลี่ยนชื่อ
from module import calculator as cal, number as num
print(cal.plus(3,5)) # 3 + 5 = 8
print(num.factorial(5)) # 5! = 5 * 4 * 3 * 2 * 1 = 120
