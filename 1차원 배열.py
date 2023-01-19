# 10807 개수세기
import sys

N = int(input())
List = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(input())

cnt = 0
for idx in List:
    if idx == v:
        cnt += 1

print(cnt)

# 10871 X보다 작은 수
import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for idx in A:
    if idx < X:
        print(idx, end=' ')

# 10818 최소, 최대
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
print(min(A), max(A))

# 2562 최댓값
import sys

List = []
for _ in range(9):
    List.append(int(sys.stdin.readline().rstrip()))
# List = [int(input()) for _ in range(9)]  # List Comprehension으로 하면 더 단축 가능
List_max = max(List)

print(List_max)
print(List.index(List_max) + 1)

# 5597 과제 안 내신 분?
# 속도는 sys.stdio.readline() > input()
List = [int(input()) for _ in range(28)]

for idx in range(1, 31):
    if idx not in List:
        print(idx)

# 3052 나머지
# 중복 제외한 개수를 셀 때, set()도 유용함.
import sys

dic = dict()

List = [int(sys.stdin.readline().rstrip()) for _ in range(10)]

for idx in List:
    num = idx % 42
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

print(len(dic))

# 1546 평균
import sys

N = int(sys.stdin.readline().rstrip())
List = list(map(int, sys.stdin.readline().rstrip().split()))

M = max(List)
mu = 0

for score in List:
    mu += ((score / M) * 100)

print(mu / N)

# 8958 OX퀴즈
import sys

T = int(sys.stdin.readline().rstrip())

while T:
    score = 0
    total_score = 0
    temp = sys.stdin.readline().rstrip()

    for check in temp:
        if check == 'O':
            score += 1
            total_score += score
        if check == 'X':
            score = 0

    print(total_score)

    T -= 1

# 4344 평균은 넘겠지
import sys

C = int(sys.stdin.readline().rstrip())

for _ in range(C):
    score_list = list(map(int, sys.stdin.readline().rstrip().split()))
    N = score_list.pop(0)
    mu = sum(score_list) / N

    cnt = 0
    for score in score_list:
        if score > mu:
            cnt += 1

    print(f'{cnt / N * 100:.3f}%')
