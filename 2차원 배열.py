# 2738 행렬 덧셈
import sys
n,m = map(int,sys.stdin.readline().split())
A = []
B = []
for _ in range(n*2):
    if _ < n: # A
        l = list(map(int, sys.stdin.readline().split()))
        A.append(l)
    if _ >= n: # B
        l = list(map(int, sys.stdin.readline().split()))
        B.append(l)

result = []
for a,b in zip(A,B):
    sum_ = []
    for i,j in zip(a,b):
        sum_.append(i + j)
    result.append(sum_)

for temp in result:
    print(' '.join(map(str,temp)))

# 2566 최댓값
import sys
mat = []

for _ in range(9):
    mat.append(list(map(int, sys.stdin.readline().split())))

max_value = []
max_idx = []

for row in mat: # 1행 ~ 9행까지 확인
    max_value.append(max(row)) # 각 행의 최댓값
    max_idx.append(row.index(max(row))) # 각 행의 최댓값의 인덱스 (열 정보)


max_ = max(max_value)
idx = max_value.index(max_) # 행정보

print(max_)
print(idx+1, max_idx[idx]+1)

# 2563 색종이
T = int(input())
s = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(T):
    n,m = map(int, input().split())

    for row in range(n-1, n-1+10):
        for col in range(m-1, m-1+10):
            s[row][col] += 1

addiction = 0
differ = 0

for temp in s:
    for num in temp:
        if num:
            addiction += 1

print(addiction)