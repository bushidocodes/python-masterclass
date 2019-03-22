for i in range(1, 20):
    print("i is now {}".format(i))

number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end="\t")

cleaned_number = ''
for char in number:
    if char in '0123456789':
        cleaned_number += char
print(cleaned_number)

states = ["not pinin'", "no more", "a stiff", "bereft of life"]

for state in states:
    print("The parrot is", state)
