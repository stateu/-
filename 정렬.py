# # 2750 수 정렬하기
# T = int(input())
# l = []
# for _ in range(T):
#     l.append(int(input()))
#
# for idx in sorted(l):
#     print(idx)

# # 2587 대푯값2
# import sys
# import statistics
# l = []
#
# for _ in range(5):
#     l.append(int(sys.stdin.readline()))
#
# print(statistics.mean(l))
# print(statistics.median(l))

# # 25305 커트라인
# import sys
# N, k = map(int, sys.stdin.readline().split())
# l = list(map(int,sys.stdin.readline().split()))
# l.sort(reverse=True)
# print(l[k-1])

# # 2751 수 정렬하기2
# import sys
# T = int(sys.stdin.readline())
#
# plus_l = [False for _ in range(1000000+1)]
#
# minus_l = [False for _ in range(1000000+1)]
# for _ in range(T):
#     idx = int(sys.stdin.readline())
#     if idx >= 0:
#         plus_l[idx] = True
#     else:
#         minus_l[idx] = True
#
# for i in range(1, len(minus_l)+1):
#     if minus_l[i-1]:
#         print((len(minus_l)-(i-1))*(-1))
#
# for i in range(len(plus_l)):
#     if plus_l[i]:
#         print(i)

# # 10989 수 정렬하기3
# import sys
# T = int(sys.stdin.readline())
#
# plus_l = [0 for _ in range(1000000+1)]
#
# for _ in range(T):
#     idx = int(sys.stdin.readline())
#     plus_l[idx] += 1
#
# for i in range(len(plus_l)):
#     if plus_l[i]:
#         for cnt in range(plus_l[i]):
#             print(i)

# 2108 통계학
import sys
N = int(sys.stdin.readline())
l = [0 for i in range(8001)]
for _ in range(N):
    pass