import cmath

x = complex(input("enter the complex number: "))

y = abs(x)
z = cmath.phase(x)

print(round(y, 3))
print(round(z, 3))