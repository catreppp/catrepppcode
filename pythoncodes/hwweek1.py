# Bài 1
# n = int(input())
# print(2*n)

# Bài 2
# a = int(input(""))
# b = int(input(""))
# s = a*b - 3.14*(a / 2)**2
# print(s)

# Bài 3
# c = input("type: ")
# if(c.isupper() == True):
#     print(c.lower())
# else:
#     print(c.upper())

# Bài 4
# c = input("type: ")
# if c.isdigit():
#     print(f'{c} ko phải là kí tự alphabet')
# else:
#     print(f'{c} là kí tự alphabet')

# Bài 5
# alphabet = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
# # print(alphabet)
# def p_alpha(kitu):
#     if(kitu == alphabet[0].upper()):
#         print("Secial case")
#     else:
#         for i in range(0, len(alphabet)):
#             if(kitu == alphabet[i].upper()):
#                 print(alphabet[i - 1])
#     return

# c = input("put sth here: ")
# p_alpha(c)

# Bài 6
# a, b, c = map(int, input("3 canh tam giac la: ").split())
# def xet_tam_giac(x, y, z):
#     p = (x + y + z)/2
#     S = (p * (p-x) * (p-y) * (p-z)) ** 0.5
#     if((x + y > z) == True):
#         if((y + z > x) == True):
#             if((x + z > y) == True):
#                 print(S)
#     else:
#         print("Khong phai 3 canh cua tam giac")
#     return

# xet_tam_giac(a, b, c)

# Bài 7
# a = list(input("nhap chuoi: "))
# print(a[4], a[8])

# Bài 8
# a = input("ten chu ho: ")
# b = int(input("thang truoc: "))
# c = int(input("thang nay: "))
# def tien_dien(x, y):
#     s = y - x
#     if(s <= 50):
#         print(f'Tien phai tra la: {round((s * 1984) * 108/100)}')
#     elif(50 < s <= 100):
#         print(f'Tien phai tra la: {round((50 * 1984 + (s - 50) * 2050) * 108/100)}')
#     elif(100 < s <= 200):
#         print(f'Tien phai tra la: {round((50 * 1984 + 50 * 2050 + (s - 100) * 2380) * 108/100)}')
#     elif(200 < s <= 300):
#         print(f'Tien phai tra la: {round((50 * 1984 + 50 * 2050 + 100 * 2380 + (s - 200) * 2998) * 108/100)}')
#     elif(300 < s <= 400):
#         print(f'Tien phai tra la: {round((50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + (s - 300) * 3350) * 108/100)}')
#     else:
#         print(f'Tien phai tra la: {round((50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + 100 * 3350 + (s - 400) * 3460) * 108/100)}')
    
#     return

# print(f'Ho va ten: {a}')
# tien_dien(b, c)

# 1
# a = int(input("nhap mot so: "))
# if(a % 2 == 0):
#     print(f'{a} la so chan')
# else:
#     print(f'{a} la so le')    

# 2
# a = list(input("nhap mot so: "))
# if(int(a[-1]) == 5):
#     print(int(a[-1]) == 5)
# else:
#     print(False)

# 3
# a = int(input("nhap mot so: "))
# if(a % 5 == 0):
#     if(a %3 == 0):
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

# 4
# a = int(input("Nhap nam sinh: "))
# b = 2026 - a
# if(b >= 18):
#     print("Du tuoi bau cu")
# else:
#     print("Chua du tuoi bau cu")

# 5
# a, b = map(int, input("Nhap 2 so: ").split())
# if(a > b):
#     print(a)
# elif(b > a):
#     print(b)
# else:
#     print("Hai so bang nhau")

# 6
# a = input("nhap mot ki tu: ")
# if(a.isalpha() == True):
#     print(f'{a} la chu')
# else:
#     print(f'{a} la so')

# 7
# a = int(input("nhap diem so: "))
# if(a >= 8):
#     print("Gioi")
# elif(6.5 <= a < 8):
#     print("Kha")
# elif(5 <= a < 6.5):
#     print("Trung binh")
# else:
#     print("Yeu")

# 8
# a = int(input("Nhap nam: "))
# if(a % 400 == 0):
#     print(f'{a} la nam nhuan')
# elif(a % 4 == 0):
#     if(a % 100 != 0):
#         print(f'{a} la nam nhuan')
#     else:
#         print(f'{a} khong la nam nhuan')
# else:
#     print(f'{a} khong la nam nhuan')

# 9
# n = int(input("Nhap so: "))
# match n:
#     case 0:
#         print("Khong")
#     case 1:
#         print("Mot")
#     case 2:
#         print("Hai")
#     case 3:
#         print("Ba")
#     case 4:
#         print("Bon")
#     case 5:
#         print("Nam")
#     case 6:
#         print("Sau")
#     case 7:
#         print("Bay")
#     case 8:
#         print("Tam")
#     case 9:
#         print("Chin")
#     case _:
#         print("So khong hop le")

# 10
# a = int(input("Nhap diem thi: "))
# if(a >= 4):
#     print("Qua mon")
# else:
#     print("Hoc lai")

# 11
# a = int(input("Nhap nam sinh: "))
# if(2025 - a >= 18):
#     print("Da du 18 tuoi")
# else:
#     print("Chua du 18 tuoi")
