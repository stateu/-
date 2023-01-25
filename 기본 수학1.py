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