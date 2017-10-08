def calculator(*args):
    a=args[0]
    b=args[1:]
    c="/"
    try:
        for i in args[1:]:
            if c == '+':
                a+=i
            elif c == '-':
                a-=i
            elif c == '*':
                a*=i
            elif c == '/':
                a/=i
        return a
    except TypeError:
        print("This is not right")

print(calculator(5, 3, 's'))


