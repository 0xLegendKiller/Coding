n = int(input())
i = input()
lister = i.split(" ")
for i in range(1, len(lister)+1):
    print(lister[-i], end=" ")
    
