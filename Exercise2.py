def hypotenuse(a, b):
   try:
        return ((a**2+ b**2)**(1/2))
   except TypeError:
       return None

print(hypotenuse(5.4, 6.7))
print(hypotenuse(5.0, 6))
print(hypotenuse(5.5, 6.2))
