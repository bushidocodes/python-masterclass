# To read text files, you just need to open the file, interact with it as a list of lines, and then close it

jabber = open("./FileIO/sample.txt", "r")

for line in jabber:
    # end is automatically a newline, which causes extra lines because files already have newlines
    print(line, end='')

jabber.close()


# Alternatively, there is a with more Pythonic syntax that automatically closes the file
# It makes manual error handling unneccesary
print("="*40)
with open("./FileIO/sample.txt", "r") as jabber:
    for line in jabber:
        if ("JAB" in line.upper()):
            print(line, end='')


# Less Pythonic way similar to other programming languages
print("="*40)
with open("./FileIO/sample.txt", "r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

# And here is a way to directly read an entire file into memory at once and then close the file
print("="*40)
with open("./FileIO/sample.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines, end='')

# Print backwards for fun
for line in lines:
    print(line[::-1], end="")
