x = 15
if (type(x) is int):
    print("True")
else:
    print("False") # type: ignore
x = 5.0
if (type(x) is float):
    print("True")
else:
    print("False") # type: ignore

y = 75
z = 75
if (y is z):
    print("y and z have same IDENTITY")
y = 30

if not (y is z):
    print("y and z have different IDENTITY")





##BiteWize pt2

a = 155
b = -13
c = 9937333
d = 0
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

print("c << 1 =", c << 1)
print("d << 1 =", d << 1)