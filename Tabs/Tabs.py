# In python, white space matters. It defines blocks

for i in range(1, 12):
    print("Yo {}".format(i))

name = input("Please enter your name >")
age = int(input("How old are you, {}? >".format(name)))
print(age)

hasFakeID = False

if age >= 21:
    print("You are old enough to buy beer")
elif hasFakeID:
    print("Here you go. You sure do look young")
else:
    print("You are too young! Please come back in {} years".format(21 - age))
