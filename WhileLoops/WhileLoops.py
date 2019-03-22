available_exits = ["east", "north east", "south"]

chosen_exit = ""

while chosen_exit not in available_exits:
    print("You are blocked and can go east, north east, and")
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break
else:
    print("aren't you glad you got out of there!")
