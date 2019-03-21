name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if (18 < age < 31):
    print("Welcome to the holiday!")
else:
    print("Sorry {}! {} is not the right age for this trip!".format(name, age))
