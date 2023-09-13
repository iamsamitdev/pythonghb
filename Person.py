class Person:

    # Properties
    __name = ""  # Private property
    __age = 0  # Private property

    # Constructor
    def __init__(self, name="", age=0):
        self.__name = name
        self.__age = age

    # Getters and Setters
    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    # Methods
    def get_profile(self):
        return self.__name + " is " + str(self.__age) + " years old."

    # Destructor
    def __del__(self):
        return True


# Create an object
person1 = Person("John", 36)
print(person1.getage())
print(person1.get_profile())

person2 = Person("Jane", 29)
print(person2.getage())
print(person2.get_profile())
