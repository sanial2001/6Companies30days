def solve(word):
    cnt = 1
    stack = []
    res = ''
    for char in word:
        if char == 'D':
            stack.append(cnt)
            cnt += 1
        elif char == 'I':
            stack.append(cnt)
            cnt += 1
            while len(stack) > 0:
                res += str(stack.pop())
    stack.append(cnt)
    while len(stack) > 0:
        res += str(stack.pop())
    return res


if __name__ == '__main__':
    print(solve('IIDDD'))
