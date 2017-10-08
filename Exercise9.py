num= 20
x=list(range(0, 101))
x.reverse()
f=x.index(num)
print(x.index(num))
g=x[f:]
print(x[f:])
for i in g:
    print(i)
