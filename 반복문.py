"""
Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우
.rstrip()을 추가로 해 주는 것이 좋다.
"""

# 10950 A+B-3
T = int(input())

# 여러줄  출력
for i in range(T):
    a, b = map(int, input().split())
    print(a + b)

# 여러줄 받는데 시간이 더 짧아 => input()보다 빨라
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):  # T번 반복
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)

# 25304 영수증
import sys

X = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
sum_ = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    sum_ += a * b

if sum_ == X:
    print('Yes')
else:
    print('No')

# 15552 빠른 A+B
import sys

T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(a + b)

# 11021 A+B-7
import sys

T = int(input())

for i, _ in enumerate(range(T), start=1):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))

    print(f'Case #{i}: {a + b}')

# 10952 A+B-5
import sys

while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a == 0 and b == 0:
        break

    print(a + b)

# 10951 A+B-4
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
    except:
        break

    print(a+b)

# 1110 더하기 사이클
origin_num = input()
num = origin_num
cnt = 0
while True:
    if int(num) < 10:  # 10보다 작은 경우
        num = '0' + num

    sum_ = 0  # 두 자릿수 합
    for idx in num:
        sum_ += int(idx)

    num = num[-1] + str(sum_)[-1]

    cnt += 1

    if int(num) == int(origin_num):
        break

print(cnt)