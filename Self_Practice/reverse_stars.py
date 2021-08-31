# Enter reverse starts numbers : - 5
#     *
#    **
#   ***
#  ****
# *****


n = int(input("Enter reverse starts numbers : - "))
for o in range(1, n+1):
    print(" " * (n-o) + "*" * o)
