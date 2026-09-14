#doubles = []

#for x in range(1,11):
    #doubles.append( x*2)
#prin t (doubles)


doubles = [x*2 for x in range(1,100) if x % 3 == 0]

fruits = "apple" 
fruits = fruits.upper()



numbers = [1,2,3,-3,-2,3,-4]

posnumbers = [-1 * x for x in numbers if x < 0]
print (posnumbers)