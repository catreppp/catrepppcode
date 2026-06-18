# 1
# a, b = map(float, input().split())
# print((a + b)*2)
# print(a*b)

# 2
# r = int(input())
# print(3.14*r**2)
# print(2*3.14*r)

# 3
# a, b, c = map(float, input().split())
# if (a + b > c) and (a + c > b) and (b + c > a):
#     if a == b == c:
#         print("Tam giac deu")
#     elif a == b or a == c or b == c:
#         print("Tam giac can")
#     elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
#         print("Tam giac vuong")
#     else:
#         print("Tam giac thuong")
# else:
#     print("Khong phai la ba canh tam giac")

# 4
# a, b = map(float, input().split())
# print(-b/a)

# 5
# a, b, c = map(float, input().split())
# delta = b**2 - 4*a*c
# x1 = (-b + delta**0.5) / (2*a)
# x2 = (-b - delta**0.5) / (2*a)
# print(x1, x2)

# 6
# a, b, c, d = map(float, input().split())
# if a > b and a > c and a > d:
#     print(f'{a} la so lon nhat')
# elif b > a and b > c and b > d:
#     print(f'{b} la so lon nhat')
# elif c > a and c > b and c > d:
#     print(f'{c} la so lon nhat')
# else:
#     print(f'{d} la so lon nhat}')

# 7
# a, b, c, d = map(float, input().split())
# if a < b and a < c and a < d:
#     print(f'{a} la so nho nhat')
# elif b < a and b < c and b < d:
#     print(f'{b} la so nho nhat')
# elif c < a and c < b and c < d:
#     print(f'{c} la so nho nhat')
# else:
#     print(f'{d} la so nho nhat')

# 8
# a, b, c, d, m, n = map(float, input().split())
# y = (m - a*n/c) / (b - a*d/c)
# x = (m - b*y) / a
# print(x, y)

# 9
# a = int(input())
# if 0 <= a <= 60:
#     print(f'{a} giây')
# elif 60 < a <= 3600:
#     print(f'{a//60} phút {a%60} giây')
# else:
#     print(f'{a//3600} giờ {(a%3600)//60} phút {a%60} giây')

# 10
# x, y, r = map(float, input().split())
# xA, yA = map(float, input().split())
# if (xA - x)**2 + (yA - y)**2 <= r**2:
#     print('A thuoc duong tron')

# 11
# x, y = map(float, input().split())
# print(x**y)