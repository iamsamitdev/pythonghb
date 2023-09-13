numbers = [-1, 2, 3, 4, 5]

print(numbers)
print(numbers[3])
print(numbers[-1]) # last index
print(numbers[-2]) # last index - 1
print(numbers[1:3]) 
print(numbers[:3]) # 0-2
print(numbers[1:]) # 1-last index
print(numbers[:]) # all
print(numbers[::2]) # 0,2,4
print(numbers[::-1]) # reverse

persons = ['John', 'Jane', 'Joe', 'Jack']

# loop persons
for person in persons:
    print(person)

# เพิ่มสมาชิกเข้าไปใน list persons ด้วย append()
persons.append('Jim')
print(persons)

# การเปลี่ยนแปลงสมาชิกใน list
persons[0] = 'Johny'
print(persons)

# การลบสมาชิกใน list
persons.remove('Johny')
persons.pop(1)
print(persons)

# นับจำนวนสมาชิกใน list
print(len(persons))