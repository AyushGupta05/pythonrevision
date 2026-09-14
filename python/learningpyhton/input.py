
value = int(input ("value of temp  "))
temperature = input ("whats the temperature. 0 for c and 1 for k  ")

if temperature == "0":
    print(int(temperature) + 273.15)
elif temperature == "1":
    print(int(temperature) - 273.15)
else:
    print("wrong value inputted")