menu = {"burger": 10, "apple": 3, "wrap" : 2}

menu.update({"fries" : 2})
for key, values in menu.items():
    print(f"{key}:{values}")

total = 0
print (" ")

order = input ("what would you like. ")

while order != "":
    if order in menu:
        total += menu.get(order)
        print (order)
    else:
        print("item not on menu")

    order = input ("what would you like.")

print(f"your total is {total}")