
n = 4
total_rows = (n*2)-1

for i in range(1,total_rows+1):
    for j in range (1,total_rows+1):
        if i == 1 or i == total_rows:
            print(n, end ="")
        else:
            if j == 1 or j == total_rows:
                print(n,end ="")
            else:
                print(, end = "")
    print ()

