# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py
# 40 40 100
# YES
# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py
# 12 14 254
# NO
# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py
# 0 5 175
# NO
# PS D:\Machines\Languages\VSC> 
  
a,b,c = map(int,input().split(" "))
if 1 <= a <= 180 and 1 <= b <= 180 and 1 <= c <= 180:
    if (a+b+c) == 180:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
