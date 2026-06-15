
a = int(input("input a number: "))
b = int(input("input a number: "))

max_num = a if a > b else b
min_num = min(a,b)

print (max_num if a > 18 else "not adult")
print (max_num)
print (min_num)