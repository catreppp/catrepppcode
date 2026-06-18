# n = int(input("Type a number: "))
# c = "Weird"
# b = "Not Weird"

# def bruh(a):
#     if(a % 2 != 0):
#         print(c)
#     elif(a % 2 == 0):
#         if(2 <= a <= 5):
#             print(b)
#         elif(6 <= a <= 20):
#             print(c)
#         elif(a > 20):
#             print(b)
# bruh(n)

# y = input()

# def is_leap(year):
#     leap = False
#     if(year % 4 == 0):
#         print("True")
#     else:
#         print(leap)
#     return leap

# print(is_leap(y))

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

put = input("type: ")
b = [x for x in put if x !=" "]
print(b)
c = int(b[len(b)-1])
b.remove(b[len(b)-1])
for i in range(1, c+1):
    a = list(combinations(b, i))
    for j in range(1, len(a)):
        print(a[j])
        for k in range(1, len(a[j]+1)):
            print(a[j][k])
# for i in range(1, len(put) - 1):
#     a = list(combinations(put, i))