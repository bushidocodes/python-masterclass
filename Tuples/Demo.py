a = b = c = d = 12
print(c)

a, b = 12, 13
print("a is {}".format(a))
print("b is {}".format(b))
print("="*50)
a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))
