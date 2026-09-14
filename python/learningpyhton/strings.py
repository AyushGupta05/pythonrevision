
name = str(input("wat name: "))

print ((len(name)))

result = name.find("a")

if not(result == -1):
    print(f"character is at {result}")
else:
    print("character isnt there")