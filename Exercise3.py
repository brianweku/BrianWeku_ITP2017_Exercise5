def hypotenuse(a, b):
   try:
        return ((a**2+ b**2)**(1/2))
   except TypeError:
       return None

print(hypotenuse(3, 4))
print(hypotenuse("so", 'lo'))
print(hypotenuse('da',  6))
