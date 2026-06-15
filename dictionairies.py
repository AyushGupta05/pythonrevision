# a collection of key value pairs. ordered and changeable, no duplicates
# id:name, item:price, country:capital

capitals = {"USA" : "Washington DC", "India" : "New Dehli", "China": "Beijing", "Russia":"Moscow"}

print(capitals.get("USA"))


#get all keys
keys = capitals.keys()

print (keys)

for key in capitals.keys():
    print(key)

## get all values

for values in capitals.values():
    print (values)


## returns a 2d list of tuples

for key, values in capitals.items():
    print(key,values)

capitals.update({"Germany" : "Berlin"})
capitals.update({"USA" : "Detroid"})
capitals.pop ("China")
capitals.popitem() 
capitals.clear()
