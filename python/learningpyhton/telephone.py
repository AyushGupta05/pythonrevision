number = input("what number: ")


if number.isdigit():
    print(number)
else:
    print(number.replace("-", "").replace("+", ""))