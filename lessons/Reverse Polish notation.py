def reverse_polish_notation(a:list):
    stack = []

    for token in a:
        print(stack)
        if type(token) is int:
            stack.append(token)
            print(stack)
        else:
            arg2 = stack.pop()
            arg1 = stack.pop()
            if token == '+':     # could be done as dictionary
                z = arg1 + arg2
            elif token == '-':
                z = arg1 - arg2
            elif token == '*':
                z = arg1 * arg2
            else: #token == '/'
                z = arg1 / arg2
            stack.append(z)
            print(stack)
    return stack.pop()


reverse_polish_notation([2, 5, 7, '*', '+'])
