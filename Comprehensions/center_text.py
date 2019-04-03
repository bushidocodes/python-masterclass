def centerText(*args, sep=" "):
    text = sep.join([str(arg) for arg in args])
    width = 80
    leftMargin = (width - len(text)) // 2
    print(" " * leftMargin + text)


centerText("spam and eggssss")
centerText("Spam and EGGS")
centerText("spam, spam, spam, and spam")
centerText(999999)
centerText("one", "Two", "THREE", sep=":")
