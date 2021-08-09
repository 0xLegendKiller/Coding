try:
    n = int(input())
    a = []
    for j in range(0, n):
        ele = input()
        a = ele.split(" ")

        if int(a[0]) + int(a[1]) + int(a[2]) > int(a[3]) + int(a[4]) + int(a[5]):
            print("1")
        else:
            print("2")

except: 
    pass
    
