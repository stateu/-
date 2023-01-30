# # 1712 손익분기점
# a, b, c = map(int, input().split())
#
# if b >= c:
#     print(-1)
# else:
#     print(a // (c - b) + 1)

# # 2292 벌집
# n = int(input())
# i = 1
# limit = 1
#
# if n == 1:
#     print(i)
# else:
#     while True:
#         if n <= limit:
#             print(i)
#             break
#         i += 1
#         limit = limit + 6 * (i-1)

# # 1193 분수찾기
# n = int(input())
# i = 0
# limit = 1
#
# while True:
#     if n < limit:
#         # print(i)
#         # print(limit-i)
#         # print(limit)
#         break
#     i += 1
#     limit += i
#
# idx = n - (limit - i)
#
# if i % 2 == 0:
#     print(str(idx + 1) + '/' + str(i - idx))
# if i % 2 == 1:
#     print(str(i - idx) + '/' + str(idx + 1))

# # 2869 달팽이는 올라가고 싶다
# import math
# a,b,v = map(int, input().split())
# print(math.ceil((v-a)/(a-b))+1)

# # 10250 ACM호텔
# import sys
#
# T = int(sys.stdin.readline())
# for _ in range(T):
#     h, w, n = map(int, sys.stdin.readline().split())
#
#     if n // h < 10:
#         if n % h == 0:
#             print(str(h) + str(0) + str(n // h))
#             continue
#         print(str(n % h) + str(0) + str(n // h +1))
#     else:
#         if n % h == 0:
#             print(str(h) + str(n // h))
#             continue
#         print(str(n % h) + str(n // h +1))

# 2775 부녀회장이 될테야
# # 재귀 풀이
# def sigma(k,n):
#     if k==0:
#         return n
#     if n==1:
#         return 1
#     return sigma(k,n-1)+sigma(k-1,n)
#
# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#
#     print(sigma(k,n))

# # 이중 리스트 풀이
# T = int(input())
# for _ in range(T):
#     K = int(input())
#     N = int(input())
#
#     l = [[i for i in range(1, N+1)]]
#
#     for k in range(1, K+1):
#         a = []
#         for n in range(1,N+1):
#             a.append(sum([i for i in l[k-1][:n]]))
#         l.append(a)
#
#     # print(l)
#     print(l[K][N-1])

# # 2839 설탕배달 (star star star)
# # 큰 수로 나누어 지는게 봉지 수가 더 최소 -> 작은 수로 빼가면서 큰 수로 나누어 떨어질 때까지 반복
# # -1 출력에 너무 신경씀;;
# n = int(input())
# cnt = 0
#
# while True:
#     if n % 5 == 0:
#         print(cnt + (n // 5))
#         break
#
#     n -= 3
#     cnt += 1
#
#     if n < 0:
#         print(-1)
#         break

# # 10757 큰 수 A+B
# a,b = map(int, input().split())
# print(a+b)