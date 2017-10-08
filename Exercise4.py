def astaga():
    try:
        num=float(input("Input number: "))
        x=list(range(1, 101))
        x.reverse()
        product=1
        f=x.index(num)
        print(x.index(num))
        g=x[f:]
        print(x[f:])
        for i in g:
            if i >1:
                print(i, end="*")
            if i==1:
                print(i)
        for i in g:
            product *=i
        print(product)

    except ValueError:
            print("sorry ur too dumb")
astaga()
