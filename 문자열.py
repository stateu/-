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
