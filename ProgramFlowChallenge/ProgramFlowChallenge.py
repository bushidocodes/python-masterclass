ipAddress = input("Please enter an IP Address: ")

numberOfSegments = 0
positionOfLastDot = 0
lengthOfSegments = []

for i in range(0, len(ipAddress)):
    if ipAddress[i] == "." or i == len(ipAddress) - 1:
        lengthOfSegments.append(i - positionOfLastDot + 1)
        positionOfLastDot = i
print("{} segments of length: ".format(
    len(lengthOfSegments)), end="")
# for segmentLength in lengthOfSegments:
print(lengthOfSegments, sep=", ", end="")
