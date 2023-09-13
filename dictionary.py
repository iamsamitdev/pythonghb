numbers = {1: "One", 2: "Two", 3: "Three"}

print(numbers)
print(type(numbers))
print(numbers[3])

people = {
    1: {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    2: {
        "name": "Jane",
        "age": 25,
        "city": "London"
    }
}

print(people[1]["name"])
print(people[2]["name"])

# การอ่าน key ทั้งหมดใน dictionary
print(numbers.keys())
print(people[1].keys())

# การอ่าน value ทั้งหมดใน dictionary
print(numbers.values())
print(people[1].values())

# loop อ่าน key และ value ใน dictionary
for key, value in numbers.items():
    print(key, value)

print("------------------")

row = 1
for key, value in people.items():
    print('row', row)
    for k, v in value.items():
        print(k, v)
    print("------------------")
    row += 1