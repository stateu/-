# 2750 수 정렬하기
T = int(input())
l = []
for _ in range(T):
    l.append(int(input()))

for idx in sorted(l):
    print(idx)

# 2587 대푯값2
import sys
import statistics

l = []

for _ in range(5):
    l.append(int(sys.stdin.readline()))

print(statistics.mean(l))
print(statistics.median(l))

# 25305 커트라인
import sys

N, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
l.sort(reverse=True)
print(l[k - 1])

# 2751 수 정렬하기2
import sys

T = int(sys.stdin.readline())

plus_l = [False for _ in range(1000000 + 1)]

minus_l = [False for _ in range(1000000 + 1)]
for _ in range(T):
    idx = int(sys.stdin.readline())
    if idx >= 0:
        plus_l[idx] = True
    else:
        minus_l[idx] = True

for i in range(1, len(minus_l) + 1):
    if minus_l[i - 1]:
        print((len(minus_l) - (i - 1)) * (-1))

for i in range(len(plus_l)):
    if plus_l[i]:
        print(i)

# 10989 수 정렬하기3
import sys

T = int(sys.stdin.readline())

plus_l = [0 for _ in range(1000000 + 1)]

for _ in range(T):
    idx = int(sys.stdin.readline())
    plus_l[idx] += 1

for i in range(len(plus_l)):
    if plus_l[i]:
        for cnt in range(plus_l[i]):
            print(i)

# 2108 통계학
import sys
import math

import statistics

N = int(sys.stdin.readline())
# l = [0 for i in range(8001)]
# for _ in range(N):
#     pass
number_list = []
count_list = [0 for _ in range(8001)]

for _ in range(N):
    n = int(sys.stdin.readline())
    number_list.append(n)
    count_list[n + 4000] += 1

number_list.sort()

mu = sum(number_list) / len(number_list)  # mean
# 컴퓨터에서 -2.5의 반올림은 -3이 아닌 -2 => -3 + 0.5 => -2 / 0.5가 반올림돼
if mu < 0:
    r = abs(math.floor(mu)) + mu
    if r >= 0.5:
        r = 1
    if r < 0.5:
        r = 0
    print(math.floor(mu) + r)
if mu >= 0:
    r = mu - math.floor(mu)
    if r >= 0.5:
        r = 1
    if r < 0.5:
        r = 0
    print(math.floor(mu) + r)
print(number_list[math.floor(len(number_list) // 2)])  # median

max_index = [idx - 4000 for idx, v in enumerate(count_list) if v == max(count_list)]
if len(max_index) == 1:
    print(max_index[0])
else:
    print(max_index[1])

number_range = max(number_list) - min(number_list)  # range
print(number_range)

# 1427 소트인사이드
temp = input()
number_list = [int(num) for num in temp]
number_list.sort(reverse=True)

print(''.join(map(str, number_list)))

# 11650 좌표 정렬하기
# sorted(list, key=lambda x : (x[0],x[1]))
# : 중첩 리스트에서 order by 내부 리스트[0] 내부 리스트[1]
import sys

N = int(sys.stdin.readline())
point_list = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    point_list.append([x, y])

point_list.sort(key=lambda x: x[0])
new_list = []

while point_list:
    last = set()
    y_list = []
    idx = 0
    c = 0
    while True:
        if len(point_list) == 1:
            if point_list[idx][0] in last:
                y_list.append(point_list.pop(idx))
                break
            else:
                new_list.append(point_list.pop(idx))
                break

        if c == 0:
            if point_list[idx][0] == point_list[idx + 1][0]:
                last.add(point_list[idx][0])
                y_list.append(point_list.pop(idx))
                continue

            if point_list[idx][0] != point_list[idx + 1][0]:
                y_list.append(point_list.pop(idx))
                break
        c += 1

        if point_list[idx][0] in last:
            y_list.append(point_list.pop(idx))
            continue

        if point_list[idx][0] not in last:
            break

    y_list.sort(key=lambda x: x[1])

    new_list.extend(y_list)

for l in new_list:
    print(l[0], l[1])

# 11651 좌표 정렬하기2
import sys

N = int(sys.stdin.readline())
number_list = []

for _ in range(N):
    number_list.append(list(map(int, sys.stdin.readline().split())))

number_list.sort(key=lambda x: (x[1], x[0]))

for l in number_list:
    print(*l)

# 1181 단어 정렬
import sys

C = int(sys.stdin.readline())
word_list = []

for _ in range(C):
    input_word = sys.stdin.readline().rstrip()
    if input_word not in word_list:
        word_list.append(input_word)

word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)

# 참고 : 튜플 정렬 : sorted([tuples]) - 튜플의 0번째로 먼저 정렬, 이후 1번째로 정렬

# 10814 나이순 정렬
import sys

T = int(sys.stdin.readline())
check_list = []

for idx, _ in enumerate(range(T)):
    age, name = sys.stdin.readline().split()
    check_list.append((int(age), idx, name))

check_list = sorted(check_list)

for l in check_list:
    print(int(l[0]), l[2])

# 18870 좌표 압축
# list에 대한 인덱스 접근보다 dict에 대한 key 접근이 훨씬 빨라
# list.index의 시간복잡도는 O(N), dict[key]의 시간복잡도는 O(1)
# 시간복잡도가 N만큼 차이나기 때문에 시간초과가 날 확률이 높아.
import sys

N = int(sys.stdin.readline())
point_list = list(map(int, sys.stdin.readline().split()))
rank = sorted(set(point_list))  # sorted의 return은 list
print(type(rank))

rank_dict = {k: v for v, k in enumerate(rank)}
for n in point_list:
    print(rank_dict[n], end=' ')
