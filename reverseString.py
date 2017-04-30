def reverseString1(str):
    return str[::-1]

# use stack to solve problem
def reverseString2(str):
    stack = []
    for ch in str:
        stack.append(ch)

    result = ""
    while len(stack) > 0:
        result += stack.pop()

    return result