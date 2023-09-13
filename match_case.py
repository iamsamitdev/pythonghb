lang = input("Please enter your language: ")

match lang.strip().lower():
    case "java":
        print("Your language is Java")
    case "python":
        print("Your language is Python")
    case "php":
        print("Your language is PHP")
    case _:
        print("Your language is not in our system")
