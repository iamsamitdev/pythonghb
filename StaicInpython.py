class Person:

    # Static properties
    total_persons = 0
    name = ""
    age = 0

    # Static method
    @staticmethod
    def get_total_persons():
        return Person.total_persons

# Call the static method
Person.total_persons = 12
print(Person.get_total_persons())