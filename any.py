# # 1919 애너그램 만들기
# word1 = list(input())
# word2 = list(input())
#
# last = []
# for idx in word1:
#     try:
#         word2.remove(idx)
#         last.append(idx)
#     except:
#         pass
#
# for idx in last:
#     word1.remove(idx)
#
# print(len(word1 + word2))
#
# # 10989 수 정렬하기3
# # 모두 담지 않고, 해당 인덱스를 수처럼 생각해서 활용
# import sys
# N = int(sys.stdin.readline())
# number_list = [0]*10001
#
# for _ in range(N):
#     idx = int(sys.stdin.readline())
#     number_list[idx] += 1
#
# for e, i in enumerate(number_list):
#     if i >= 1:
#         for _ in range(i):
#             print(e)