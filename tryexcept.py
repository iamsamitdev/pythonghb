# ValueError
# ZeroDivisionError
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"{num1} / {num2} = {num1/num2}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:
    print("Something went wrong", Exception)