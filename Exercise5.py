a=10
b=10
c='*'
d='float'
def calculator(a, b):
    if c=="*":
        return a*b

    if c=="+" or c=="":
        return a+b

    if c=="/":
        return a/b

    if c=="-":
        return a-b
if d=="int":
    print(int(calculator(a, b)))
if d=="float":
    print(float(calculator(a, b)))
