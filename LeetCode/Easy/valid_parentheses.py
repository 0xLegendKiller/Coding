def isValid(s):
    stack = []
    for i in range(len(s)):
        stack_len = len(stack)
        if stack_len == 0:
            print(s[i])
            stack.append(s[i])
        elif s[i] == ")" and stack[stack_len - 1] == "(":
            print(s[i])
            stack.pop(stack_len - 1)
        elif s[i] == "}" and stack[stack_len - 1] == "{":
            print(s[i])
            stack.pop(stack_len - 1)
        elif s[i] == "]" and stack[stack_len - 1] == "[":
            print(s[i])
            stack.pop(stack_len - 1)
        else:
            print(s[i])
            stack.append(s[i])
    return len(stack) == 0


# strHere = "([((()))([][])])"

# print(isValid(strHere))
