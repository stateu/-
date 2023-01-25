# 11720 숫자의 합
import sys

N = int(sys.stdin.readline().rstrip())
num = sys.stdin.readline().rstrip()

sum_ = 0
for idx in num:
    sum_ += int(idx)

print(sum_)

# 10809 알파벳 찾기
str_temp = input()

str_check = 'abcdefghijklmnopqrstuvwxyz'

for idx in str_check:
    if idx in str_temp:
        print(str_temp.index(idx), end=' ')
        continue
    print(-1, end=' ')

# 2675 문자열 반복
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, temp = sys.stdin.readline().rstrip().split()

    for idx in str(temp):
        print(idx * int(n), end='')
    print()

# 1157 단어 공부
temp = input().lower()
dic = dict()

for idx in temp:
    if idx in dic:
        dic[idx] += 1
    else:
        dic[idx] = 1

max_value = max(dic.values())

most = [k for k, v in dic.items() if v == max_value]
if len(most) > 1:
    print('?')
else:
    print(most[0].upper())
# cnt = 0
# for i in dic.values():
#     if i == max_value:
#         cnt += 1
#
#     if cnt > 1:
#         print('?')
#         break
# else:
#     for k,v in dic.items():
#         if v == max_value:
#             print(k.upper())


# 1152 단어의 개수
temp = input().strip()
if temp == '':
    print(0)
else:
    print(temp.count(' ') + 1)

# 2908 상수
import sys

A, B = sys.stdin.readline().rstrip().split()
new_a = new_b = ''

for a in A[::-1]:
    new_a += a

for b in B[::-1]:
    new_b += b

if int(new_a) > int(new_b):
    print(new_a)
else:
    print(new_b)

# 5622 다이얼
# 문자열 문제는 아스키코드를 이용하는 것도 좋아.
import sys

temp = sys.stdin.readline().rstrip()
dic = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}

cnt_time = 0  # 1번까지 도달
for idx in temp:
    for k, v in dic.items():
        if idx in k:  # 해당 문자의 위치 추적
            cnt_time += v + 1  # v+1초 걸려
print(cnt_time)

# 2941 크로아티아 알파벳
import sys

temp = sys.stdin.readline().rstrip()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet = 0

while temp:
    for idx in croatia:  # 크로아티아 알파벳 소거 겸 카운트
        if idx in temp:
            alphabet += 1
            temp = temp.replace(idx, ' ', 1)
            break
    else:
        for idx in temp.split():
            alphabet += len(idx)
        break

print(alphabet)

# 1316 그룹 단어 체커
import sys

N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    temp = sys.stdin.readline()

    last = set()

    for idx in range(len(temp)):
        last.add(temp[idx])

        if idx == len(temp) - 1:
            cnt += 1
            break

        if temp[idx] != temp[idx + 1]:
            if temp[idx + 1] in last:
                break

print(cnt)