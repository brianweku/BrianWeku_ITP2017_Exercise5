z=lambda a:a**2
x=lambda a, b:(a**2+b**2)**(.5)
c=lambda *args: sum(args)/len(args)
v=lambda a: "".join(set(a))

def aa(a):
    return a**2
def bb(a, b):
    return (a**2+b**2)**(.5)
def cc(*args):
    return sum(args)/len(args)
def dd(a):
    return "".join(set(a))

print(z(7))
print(x(7, 8))
print(c(7, 8, 9))
print(v('iloveusomuch'))
print(aa(7))
print(bb(7, 8))
print(cc(7, 8, 9))
print(dd('iloveusomuch'))
