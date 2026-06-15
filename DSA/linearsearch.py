def linear_search(listtosort, target):
    for i,items in enumerate(listtosort):
        if items == target:
            return i
    return -1




tests = [
    {"input": {
        "listtosort" : [2,5,3,6,8],
        "target" : 3
    }
    ,"output" : 2}
]

tests.append ({
    "input": {
        "listtosort" : [2,5,3,6,8],
        "target" : 9
    }
    ,"output" : -1
})

for test in tests:
    print(linear_search(**test["input"]) == test["output"])






































test = [{ "input" : {
    listtosort = [1,3,6,9,10],
    target = 5
},
"output" = 5



}]