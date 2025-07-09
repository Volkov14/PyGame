lst = [1, 3, 5, 8, 10, 13, 27, 86, 99]

# num = 99
# left = 0
# right = len(lst) - 1
#
# def b_search(lst, num, left, right):
#
#     while left <= right:
#         midlle = (right + left) // 2
#         if lst[midlle] != num and lst[midlle] > num:
#             right = midlle - 1
#         elif lst[midlle] != num and lst[midlle] < num:
#             left = midlle + 1
#         else:
#             return midlle
#     return -1
#
# print(b_search(lst, 86, 0, len(lst) - 1))


# def buble_sort(lst):
#     for j in range(0, len(lst) - 1):
#         for i in range(0, len(lst) - 1 - j):
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#     return lst
#
# lst = [4, 99, 5, 1, 10, 13, 11]
# print(buble_sort(lst))

