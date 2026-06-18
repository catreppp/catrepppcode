# # outline = ['a', ['b', ['c', 'd'], 'e'], 'f']
# # def indent(level):
# #     return ' ' * level
# # def print_outline_rec(outline, level):
# #     for item in outline:
# #         if isinstance(item, list):
# #             print_outline_rec(item, level + 1)
# #         else:
# #             print(indent(level) + item)
# #     print(1)

# # print_outline_rec(outline, 0)

# # class MyDate():
# #     def __init__(self, d, m, y):
# #         self.dd = d
# #         self.mm = m
# #         self.yyyy = y
# #     def check_legit(self):
# #         maxday = -1
# #         match self.mm:
# #             case 1|3|5|7|8|10|12:
# #                 maxday = 31
# #             case 4|6|9|11:
# #                 maxday = 30
# #             case 2:
# #                 if (self.yyyy % 4 == 0 and self.yyyy % 100 != 0) or (self.yyyy % 400 == 0):
# #                     maxday = 29
# #                 else:
# #                     maxday = 28
# #         return 1 <= self.dd <= maxday and self.yyyy > 0
# #     def getNextDay(self):
# #         if(self.check_legit()):
# #             day1 = MyDate(self.dd + 1, self.mm, self.yyyy)
# #             if day1.check_legit():
# #                 return day1
# #             day1 = MyDate(1, self.mm + 1, self.yyyy)
# #             if day1.check_legit():
# #                 return day1
# #             return MyDate(1, 1, self.yyyy + 1)
# #     def __str__(self):
# #         return f'{self.dd:02d}/{self.mm:02d}/{self.yyyy}'

# # d, m, y = map(int, input().split('/'))
# # d1 = MyDate(d, m, y)
# # print(d1.getNextDay())

# # def selection_sort(arr):
# #     print(arr)
# #     n = len(arr)
# #     for i in range(n):
# #         min_idx = i
# #         for j in range(i+1, n):
# #             if arr[j] < arr[min_idx]:
# #                 min_idx = j # Update min_idx
# #                 print(j)
# #             print(arr)
# #         arr[i], arr[min_idx] = arr[min_idx], arr[i] # Swap

# # selection_sort(input().split())

# # def insertion_sort(arr):
# #     for i in range(1, len(arr)):
# #         key = arr[i] # Current element to be sorted
# #         j = i - 1
# #         print(key)
# #         while j >= 0 and arr[j] > key:
# #             arr[j+1] = arr[j] # Shift element > key to the right
# #             j -= 1
# #             print(arr)
# #             print(j)
# #         arr[j+1] = key # Insert key at the correct position
# #         print(key)
# #         print(arr)
# #         print("end")

# # insertion_sort(list(map(int, input().split())))

# # def merge(left, right):
# #     res = []
# #     i = j = 0
# #     while i < len(left) and j < len(right):
# #         print(left[i], right[j])
# #         if left[i] < right[j]:
# #             res.append(left[i])
# #             i += 1
# #         else:
# #             res.append(right[j])
# #             j += 1
# #         print(res)
# #     res.extend(left[i:])
# #     res.extend(right[j:])
# #     print("end")
# #     return res

# # def merge_sort(arr):
# #     if len(arr) <= 1:
# #         return arr

# #     mid = len(arr) // 2
# #     left = arr[:mid]
# #     right = arr[mid:]
# #     print(mid)
# #     print(left)
# #     print(right)

# #     sorted_left = merge_sort(left)
# #     sorted_right = merge_sort(right)

# #     return merge(sorted_left, sorted_right)

# # print(merge_sort([39, 25, 40, 7]))

# import os.path
# FILENAME = "Raven.txt "
# def main ():
#     "Print lines from file, keeping a count."
#     if not os.path.isfile(FILENAME):
#         print("File does not exist")
#         return
#     # Open file for input
#     ravenFile = open(FILENAME, "r")
#     line = ravenFile.readline()
#     lineCount = 0
#     while line: # line is not empty string
#         lineCount += 1
#         print(format(lineCount , "3d" ) , ": " , \
#         line.strip(), sep = "" )
#         line = ravenFile.readline()
#     print("\nFound ", lineCount, " lines.")
#     ravenFile.close()
# main ()

# def HelloWorld():
#     try:
#         # a, b = map(int ,input().split())
#         # res = a/b
#         lst = [1, 2, 3]
#         print(lst[10])
#     except (ValueError, FileNotFoundError, TypeError):
#         print("404")
#     except IndexError as i:
#         print(i)
#     except ZeroDivisionError:
#         print("Divided to zero")
#     except Exception:
#         print("Unknown Error")
#     else:
#         print(res)
#     finally:
#         print("The End")

import os.path
FILENAME = "input.txt "
def main ():
    #"Print lines from file, keeping a count."
    if not os.path.isfile(FILENAME):
        print("File does not exist")
        return
    # Open file for input
    ravenFile = open(FILENAME, "r")
    line = ravenFile.readline()
    lineCount = 0
    while line: # line is not empty string
        lineCount += 1
        print(format(lineCount , "3d" ) , ": " , \
        line.strip(), sep = "" )
        line = ravenFile.readline()
    print("\nFound ", lineCount, " lines.")
    ravenFile.close()
main ()
