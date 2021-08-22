i = int(input())
if (i % 5 == 0 and i % 11 != 0) or (i % 5 != 0 and i % 11 == 0):
    print("ONE")
elif i % 5 == 0 and i % 11 == 0:
    print("BOTH")
else:
    print("NONE")
