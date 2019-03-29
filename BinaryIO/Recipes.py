import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beansOnToast = ["beans", "bread"]
# scrambledEggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "chesse"]

with shelve.open("./BinaryIO/recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beansOnToast"] = beansOnToast
    # recipes["scrambledEggs"] = scrambledEggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta

    # You can only directly append to the shelf when writeback=True when opening the file
    recipes["blt"].append("butter")
    recipes["pasta"].append("tomato")

    # Otherwise, you have to update an in-memory copy and then explicitly reassign it to the shelf
    # bltBuffer = recipes["blt"]
    # bltBuffer.append("butter")
    # recipes["blt"] = bltBuffer

    # When writeback is true, the changes are written to the shelf when the file closes or when sync is called
    recipes.sync()

    for snack in recipes:
        print(snack, recipes[snack])
