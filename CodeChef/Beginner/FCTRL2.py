try:
    a = int(input())
    result = 1
    for i in range(1, a + 1):
        inputs = int(input())
        for j in range(1, inputs + 1):
            result = result * j
        print(result)
        result = 1

except:
    pass
