def missing_number(arthimetic_list):
    difference = min(
        arthimetic_list[1] - arthimetic_list[0],
        arthimetic_list[2] - arthimetic_list[1]
    )


    beg = 0 
    end = len(arthimetic_list) - 1

    while end >= beg:
        
        mid = (beg + end)//2

        if mid > 0 and arthimetic_list[mid] - arthimetic_list[mid - 1] != difference:
            return arthimetic_list[mid - 1] + difference

        if mid < len(arthimetic_list) - 1 and arthimetic_list[mid + 1] - arthimetic_list[mid] != difference: 
            return arthimetic_list[mid] + difference
        
        if (arthimetic_list [mid] - arthimetic_list [beg]) > ((mid - beg) * difference):
            end = mid - 1
        else:
            beg = mid + 1
    
    return -1






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