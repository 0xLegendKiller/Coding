# cook your dish here
try:
    a = []
    n = int(input())
    for i in range(0, n):
        ele = int(input())
        a.append(ele)
    
    b = (sorted(a))
    for element in b:
        print(element)
except:
    pass
