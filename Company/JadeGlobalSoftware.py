def verfication(num1, num2):
    if num2 % num1 == 0:
        print("Yes")
    else:
        print("No")


n = input("Input the number of test cases \n")

for i in range(0, int(n)):
    s = input()
    list_str = []
    list_str = s.split(" ")

    verfication(int(list_str[0]), int(list_str[1]))
