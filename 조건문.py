# 2753 윤년
year = int(input())

if year % 400 == 0:
    print(1)
elif (year % 4 == 0) and (year % 100 != 0):
    print(1)
else:
    print(0)

# 2884 알람 시계
h, m = map(int, input().split(' '))

if m >= 45:
    print(h, m - 45)
if m < 45:
    if h == 0:
        print(23, 60 - (45 - m))
    if h > 0:
        print(h - 1, 60 - (45 - m))

# 2525 오븐 시계
h, m = map(int, input().split(' '))
need = int(input())
s = m + need

if s // 60 >= 0:
    h += s // 60
    if h > 23:
        print(h - 24, s % 60)
    else:
        print(h, s % 60)
if s // 60 < 0:
    print(h, s % 60)


# 2480 주사위 세개
def prize(f, s, t):
    if f == s and s == t:
        print(10000 + f * 1000)
        return

    if f == s and s != t:
        print(1000 + f * 100)
        return

    if f == t and s != t:
        print(1000 + f * 100)
        return

    if s == t and f != s:
        print(1000 + s * 100)
        return

    if f != s and s != t:
        print(max(f, s, t) * 100)
        return


f, s, t = map(int, input().split(' '))
prize(f, s, t)
