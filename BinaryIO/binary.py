# We can manually read and write binaries using the b mode

# with open("./BinaryIO/binary", "bw") as bin_file:
#     for i in range(17):
#         # We can't pass an integer to the bytes function because that allocated a zeros out bytes with that length
#         # This is why we wrap the integer in a list
#         bin_file.write(bytes([i]))

#  This is more Pythonic
# with open("./BinaryIO/binary", "bw") as bin_file:
#     bin_file.write(bytes(range(17)))

# with open("./BinaryIO/binary", "br") as binFile.read:
#     for b in binFile.read:
#         print(b)


a = 65534    # FF FE
b = 65535    # FF FF
c = 65536    # 00 01 00 00
d = 2998302  # 00 2D C0 1E

# Directly writing bytes in Big-Endian and Little-Endian
with open("./BinaryIO/binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'little'))


with open("./BinaryIO/binary2", "br") as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile.read(4), 'big')
    print(g)
    h = int.from_bytes(binFile.read(4), 'big')
    print(h)
    # This will result in an Endian problem!
    i = int.from_bytes(binFile.read(4), 'big')
    print(i)
