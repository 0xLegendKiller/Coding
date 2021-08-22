s = int(input())
lister = []
for i in range(1, s + 1):
    if s % i == 0:
        lister.append(i)
    else:
        continue
print(len(lister))
for ele in lister:
    print(ele, end=" ")
