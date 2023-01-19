# 15596 정수 N개의 합
def sum_(List):
    sum_value = 0
    for idx in List:
        sum_value += idx
    return sum_value


# 4673 셀프 넘버
# remove가 시간이 많이 소요되긴 하네
def d(n):
    if type(n) == int:
        n = str(n)
    sum_ = 0
    for idx in n:
        sum_ += int(idx)
    return sum_ + int(n)


List = set([i for i in range(1, 10001)])
self_number = set()

for i in range(1, 10001):
    self_number.add(d(i))

for i in sorted(List - self_number):
    print(i)

# 1065 한수
import sys

n = int(sys.stdin.readline().rstrip())
hansu = 0
List = [str(i) for i in range(1, n + 1)]

for str_temp in List:
    if int(str_temp) < 100:
        hansu += 1
        continue

    minus = int(str_temp[0]) - int(str_temp[1])
    yn = 1

    for idx in range(1, len(str_temp)):
        if int(str_temp[idx - 1]) - int(str_temp[idx]) != minus:
            yn = 0
            break

    if yn:
        hansu += 1

print(hansu)
