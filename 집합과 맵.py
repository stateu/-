# # 10815 숫자카드
# N = int(input())  # 상근이 개수
# N_set = set(list(map(int,input().split())))
#
# M = int(input())
# M_list = list(map(int, input().split()))
#
# # in 비교 : list << set / list의 경우 시간초과 났음.
# for m in M_list:
#     if m in N_set:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# # 14425 문자열 집합
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# S_set = set()
# for _ in range(N):
#     S_set.add(sys.stdin.readline())
#
# cnt = 0
# for _ in range(M):
#     temp = sys.stdin.readline()
#     if temp in S_set:
#         cnt += 1
#
# print(cnt)

# 1620 나는야 포켓몬 마스터 이다솜
import sys
N,M = map(int, sys.stdin.readline().split())
pocket = dict()
pocket_number = dict()

for idx in range(N):
    key = sys.stdin.readline()
    pocket[key] = idx
    pocket_number[str(idx)] = key

for _ in range(M):
    search = sys.stdin.readline()
    try:
        search = int(search)
    except:
        pass

    if type(search) == str:
        print(pocket[search]+1)
    else:
        print(pocket_number[str(search-1)])
