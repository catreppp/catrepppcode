# W3A1
# a = int(input())
# if 100 <= a <= 999:
#     tram = a // 100
#     chuc = (a % 100) // 10
#     dv = (a % 100) % 10
#     b = [dv, chuc, tram]
#     c = dv*100 + chuc*10 + tram
#     print(c)
# else:
#     print("cannot proccess")

#W3A2
# a, b = map(int, input().split())
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a, b)

#W3A3
# n = int(input())
# if n & (n-1) == 0:
#     print(f'{n} la luy thua cua 2')
# else:
#     print(f'{n} ko la luy thua cua 2')

#W3A4
# m, n = map(float, input().split())
# print(m // n)

#W3A5
# m, n = map(int, input().split())
# if m % n == 0:
#     print(m / n)
# else:
#     print(m // n + 1)

#W3A6
# n = int(input())
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#W3A7
# a, b = map(float, input().split())
# if a < 0 and b < 0:
#     print("Yes")
# else:
#     print("No")

#W3A8
# a = list(input())
# b = list("".join(input().split()))
# print(a, b)
# if len(a) > len(b):
#     print(True)
# else:
#     print(False)

#W3A9
# a, b, c = map(float, input().split())
# if a + b > c and a + c > b and b + c > a:
#     print("Yes")
# else:
#     print("No")

#W3A10
# a, b, c, d = map(float, input().split())
# if a > b and a > c and a > d:
#     print(a)
# elif b > a and b > c and b > d:
#     print(b)
# elif c > a and c > b and c > d:
#     print(c)
# elif d > a and d > b and d > c:
#     print(d)
# else:
#     print("Khong co so nao lon nhat")

#W3A11
# a, b, c = map(float, input().split())
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("tam giac deu")
#     elif a == b or b == c or a == c:
#         print("tam giac can")
#     elif a**2 + b**2 == c**2 or a**2 + c**2 == c**2 or b**2 + c**2 == a**2:
#         print("tam giac vuong")
#     else:
#         print("Tam giac thuong")
# else:
#     print("Khong phai tam giac")

#W3A12
# a = int(input())
# if a % 400 == 0:
#     print("Nam nhuan")
# elif a % 4 == 0 and a % 100 != 0:
#     print("Nam nhuan")
# else:
#     print("Nam khong nhuan")

#W3A14
# a, b = map(int,input().split())
# print(round(-b/a, 2))

#W3A15
# a = float(input())
# if a >= 8:
#     print("gioi")
# elif 6.5 <= a <= 8:
#     print("Kha")
# elif 5 <= a <= 6.5:
#     print("Trung binh")
# else:
#     print("Yeu")

#W3A16
# a = float(input())
# if a - a // 1 >= 0.5:
#     b = a // 1 + 1
# else:
#     b = a // 1
# print(a // 1 + 1, a // 1, b)

#W3A17
# a, b, c, d = map(float, input().split())
# q = b / a
# if b * q == c and c * q == d:
#     print("Cap so nhan")
# else:
#     print("Khong phai cap so nhan")