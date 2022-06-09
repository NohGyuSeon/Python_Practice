# import sys

# n = sys.stdin.readline()

n = input()

n_length = len(n)
encoded_str = ""

for i in n:
    str = ord(i) + 10
    encoded_str += chr(str)

# count_k = 0
# count_r = 0

# for i in range(0, n_length):
#     if (encoded_str[i] == 'k' or encoded_str[i] == 'K'):
#         count_k += 1
#     if (encoded_str[i] == 'r' or encoded_str[i] == 'R'):
#         count_r += 1

upper_text = encoded_str.upper()

# print("Total:", n_length, "/ K:", count_k, "/ R:", count_r, "/ Encoded:", encoded_str, end=' ')
print("Total:", n_length, "/ K:", upper_text.count("K"), "/ R:", upper_text.count("R"), "/ Encoded:", encoded_str, end=' ')
