menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "saugage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])

for meal in menu:
    if not "spam" in meal:
        for ingredient in meal:
            print(ingredient)
