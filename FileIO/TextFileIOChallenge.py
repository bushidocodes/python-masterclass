with open("./FileIO/sample.txt", 'a') as jabberwock:
    for i in range(0, 13, 1):
        print("{:>2} time 2 is {}".format(i, i*2), file=jabberwock)
