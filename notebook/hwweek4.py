#W4A1
# n = int(input())
# a = 0
# for i in range (1, n + 1):
#     a = a + i
# print(a)

#W4A2
# while True:
#     a = int(input())
#     if a > 0:
#         break

# c = True
# if a <= 1:
#     c = False
# for i in range(2, a):
#     if a % i == 0:
#         c = False
#         break

# if c:
#     print("La so nguyen to")
# else:
#     print("Khong la so nguyen to")

#W4A3
# n = int(input())
# for i in range (1, n):
#     n = n * i
# print(n)

#W4A4
# n = list(input())
# if n[0] == '-':
#     n.remove('-')
#     print(len(n))
# else:
#     print(len(n))

#W4A5
# n = int(input())
# a = input().split()
# truth = True
# while len(a) != n:
#     a = input().split()
# if len(a) == n:
#     for i in range(len(a)):
#         if a[i] == '42':
#             print("I've found the meaning of life!")
#             truth = False
#             break
# if truth:
#     print("It's a joke!")

#W4A6
# a, b = map(int, input().split())
# d = 0
# for i in range(a, b + 1):
#     c = True
#     for j in range(2, i):
#         if i % j == 0:
#             c = False
#             break
#     if c:
#         d = d + i
# print(d)

#W4A7
# n = int(input())
# a = []
# if n < 2:
#     while n < 2:
#         n = int(input())
# else:
#     for i in range(1, n):
#         if n % i == 0:
#             a. append(i)
# print(a[-1])

#W4A8
# a = list(input())
# while a[::-1] != a:
#     a = str(int(''.join(a)) + int(''.join(a[::-1])))
# print(a)

#W4A9
# n = int(input())
# m = []
# for i in range(2, n):
#     if (i**0.5) // 1 == i**0.5:
#         a = list(str(i))
#         truth = True
#         for j in range(len(a)):
#             for k in range(j+1, len(a)):
#                 if a[j] == a[k]:
#                     truth = False
#                     break
#         if truth:
#             m.append(i)

# print(*m)
                    
#W4A10
# n = int(input())
# m = []
# for i in range(1, n + 1):
#     a = []
#     m.append(i)
#     while i != 1:
#         if i % 2 == 0:
#             i = i / 2
#         else:
#             i = 3*i + 1
#         a.append(i)
#     m.append(len(a))
# b = m[0]
# for i in range(1, len(m), 2):
#     if m[i] > b:
#         b = m[i]
# print(m[m.index(b) - 1])

#W4A11
# n = int(input())
# m = []
# if n < 10**6:
#     for i in range(2, n+1):
#         if n % i == 0:
#             if i % 2 == 0:
#                 m.append(i)
#     print(len(m))
# else:
#     print('Cannot calculate')

#W4A12
# X = int(input('Deposit: '))
# n = int(input('Month: '))
# print((X*((1+7*10**-3)**n)) // 1)

#W4A13
# m = int(input())
# n = int(input())
# um = []
# un = []
# for i in range(1, m):
#     if m % i == 0:
#         um.append(i)
# for i in range(1, n):
#     if n % i == 0:
#         un.append(i)
# if sum(um) == n and sum(un) == m:
#     print('Yes')
# else:
#     print('No')

#W4A14
# m, n = map(int, input().split())
# a = []
# for i in range(1, max([m, n])):
#     if m % i == 0 and n % i == 0:
#         a.append(i)
# print(a[-1])

#W4A15
# m = int(input('Population: '))
# n = int(input('Legs: '))
# a = (n-2*m)/2
# b = m - a
# if a // 1 != a or b // 1 != b or a < 0 or b < 0 or int(a) != a or int(b) != b:
#     print('Invalid')
# else:
#     print(f'Dogs: {a}, Chickens: {b}')
