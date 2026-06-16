 


tests = [{
    "input" : [3, 6, 9, 15, 18, 21],
    "output" : 12
},
{
    "input" : [2, 6, 8, 10,12],
    "output" : 4
},
{
    "input" : [1, 2, 3, 4, 6],
    "output" : 5
}

]

for test in tests:
    print(missing_number(test["input"]) == test["output"])