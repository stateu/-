# 10815 숫자카드
N = int(input())  # 상근이 개수
N_set = set(list(map(int,input().split())))

M = int(input())
M_list = list(map(int, input().split()))

# in 비교 : list << set / list의 경우 시간초과 났음.
for m in M_list:
    if m in N_set:
        print(1, end=' ')
    else:
        print(0, end=' ')

# 14425 문자열 집합
import sys

N, M = map(int, sys.stdin.readline().split())
S_set = set()
for _ in range(N):
    S_set.add(sys.stdin.readline())

cnt = 0
for _ in range(M):
    temp = sys.stdin.readline()
    if temp in S_set:
        cnt += 1

print(cnt)

# 1620 나는야 포켓몬 마스터 이다솜
import sys
N,M = map(int, sys.stdin.readline().split())
pocket = dict()
pocket_number = dict()

for idx in range(N):
    key = sys.stdin.readline().strip()
    pocket[key] = idx
    pocket_number[str(idx)] = key

for _ in range(M):
    search = sys.stdin.readline().rstrip()
    try:
        search = int(search)
    except:
        pass

    if type(search) == str:
        print(pocket[search]+1)
    elif type(search) == int:
        print(pocket_number[str(search-1)])

# 10816 숫자카드 2
import sys
from collections import defaultdict
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_dict = defaultdict(int)

for idx in N_list:
    N_dict[idx] += 1

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for jdx in M_list:
    print(N_dict[jdx], end=' ')

# 1764 듣보잡
import sys
N,M = map(int, sys.stdin.readline().split())
N_dict = dict()
for _ in range(N):
    temp = sys.stdin.readline().rstrip()

    if temp in N_dict:
        N_dict[temp] += 1
    else:
        N_dict[temp] = 1

cnt = 0
M_list = []
for _ in range(M):
    temp = sys.stdin.readline().rstrip()

    if temp in N_dict:
        cnt += 1
        M_list.append(temp)

print(cnt)
for idx in sorted(M_list):
    print(idx)

# 1269 대칭 차집합
import sys
a, b = map(int, sys.stdin.readline().split())

set_a = set(list(map(int, sys.stdin.readline().rstrip().split())))
set_b = set(list(map(int, sys.stdin.readline().rstrip().split())))

a_diff_b = set_a-set_b
b_diff_a = set_b-set_a

print(len(set_a^set_b)) # 대칭 차집합 연산 ^

# 11478 서로 다른 부분 문자열의 개수
temp = input().strip()
sub_temp = []

for idx in range(len(temp)):
    for jdx in range(idx, len(temp)+1):
        sub_temp.append(temp[idx:jdx])
print(len(set(sub_temp))-1)
