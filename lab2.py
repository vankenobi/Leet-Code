a = [1,2,3,4,5,6,7,8,9]

count = 0
circle = 0
while(count <= 9):
    print(a[count])
    count += 1
    if(count == 9):
        count = 0
        circle += 1
        print(circle)