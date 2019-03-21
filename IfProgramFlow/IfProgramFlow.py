age = int(input("How old are you? "))

# Python uses English words and, or
# if age >= 16 and age <= 65:
#     print("Have a good day at work!")


# Python allows ranges to be expressed in this condensed format
if 16 <= age <= 65:
    print("Have a good day at work!")

# Python does not have a boolean data type, but it has two constants "True" and "False"
# The function bool coerces to the appropriate value
if False or True:
    print("Okay")

print("""False: {}
None: {}
0: {}
0.0: {}
empty List []: {}
empty tuple (): {}
empty string '': {}
empty string "": {}
empty mapping: {}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# Negation is performed using the not keyword
print("not False is {}".format(not False))
