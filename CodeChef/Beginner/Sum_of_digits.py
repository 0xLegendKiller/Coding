total = int(input())
lists = []
res = 0
for i in range(0, total):
    tmp = int(input())
    lists.append(tmp)
for c in lists:
    for digit in range(0, len(str(c))):
        res = res + int(str(c)[digit])
        # print(str(c)[l])
    print(res)
    res = 0
