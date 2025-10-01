try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("age cannot be zero!!")

