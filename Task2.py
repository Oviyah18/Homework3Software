def num_in_seq(n):
    if n == 1:
        return 8
    else:
        return num_in_seq(n-1) + 7
print(num_in_seq(1))  # Output: 8
print(num_in_seq(3))  # Output: 22
print(num_in_seq(10)) # Output: 71
