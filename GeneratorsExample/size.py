import sys

# Example of using a Generator to express an arithmetic sequence
# This shows that generators are massively more memory efficient
def my_range(n: int):
    print("my_range starts")
    start: int = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


big_range = my_range(5)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))  # 120 bytes

big_list = []
for val in big_range:
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))  # 87624 bytes

# For arithmetic sequences, we can just use the Range datatype


print(big_range)
print(big_list)
