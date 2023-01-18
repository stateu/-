# # 3003 킹 퀸 룩 비숏 나이트 폰
# def check_cnt(origin, target):
#     plus = 0
#     if origin == target:
#         return plus
#
#     if origin > target:
#         while True:
#             plus += 1
#             origin -= 1
#
#             if origin == target:
#                 return -plus
#                 # break
#
#     if origin < target:
#         while True:
#             plus += 1
#             origin += 1
#
#             if origin == target:
#                 return plus
#                 # break
#
#
# List = list(map(int, input().split(' ')))
#
# targetList = [1, 1, 2, 2, 2, 8]
# for origin, target in zip(List, targetList):
#     print(check_cnt(origin, target), end=' ')

# # 2588 곱셈
# a = int(input())
# b = input()
#
# for i in b[::-1]:
#     print(a*int(i))
# print(a*int(b))

# # 10172 개
# print('''|\\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\\__|''')

