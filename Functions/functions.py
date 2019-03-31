def centerText(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    width = 80
    leftMargin = (width - len(text)) // 2
    return " " * leftMargin + text


def centerPrint(*args, sep=' ', end='\n', file=None, flush=False):
    print(centerText(*args, sep), end=end, file=file, flush=flush)


with open("./Functions/report.txt", "w") as report:
    centerPrint("spam and eggssss", file=report)
    print(centerText("Spam and EGGS"))
    centerPrint("spam, spam, spam, and spam", file=report)
    centerPrint(999999, file=report)
    centerPrint("one", "Two", "THREE", sep=":", file=report)
