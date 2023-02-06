# # 10872 팩토리얼
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)
#
# N = int(input())
# print(factorial(N))
#
# # 10870 피보나치 수5
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
#
# N = int(input())
# print(fibonacci(N))
#
# # 25501 재귀의 귀재
# def recursion(S, idx, e):
#     global cnt
#     cnt += 1
#     if idx >= e:
#         return 1
#
#     elif S[idx] != S[e]:
#         return 0
#
#     else:
#         return recursion(S, idx + 1, e - 1)
#
#
# def is_palindrome(S):
#     return recursion(S, 0, len(S) - 1)
#
#
# T = int(input())
#
# for _ in range(T):
#     cnt = 0
#     temp = input()
#     print(is_palindrome(temp), cnt)

# # 11729 하노이 탑 이동 순서 star star
# def move(L):
#
# N = int(input())
#
# cnt = 0