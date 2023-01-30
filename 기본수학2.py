# 1978 소수찾기
import math

N = int(input())
temp = list(map(int, input().split()))

cnt = 0

for i in temp:
    if i == 1:
        continue

    for d in range(2, math.ceil(i/2)+1):
        if i % d == 0: # 소수가 아님
            break
    else:
        cnt += 1

print(cnt)

# 2581 소수
import math
M = int(input())
N = int(input())

prime_list = []
for num in range(M, N+1):
    if num == 1:
        continue
    for d in range(2, math.ceil(num/2)+1):
        if num % d == 0: # 소수가 아님
            break
    else:
        prime_list.append(num)

if len(prime_list) >= 1:
    print(sum(prime_list))
    print(min(prime_list))
elif len(prime_list) <= 0:
    print(-1)

# 11653 소인수분해
def prime_number(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

N = int(input())
if N == 1:
    print()
else:
    d = 2
    while True:
        if N == 1:
            break

        if not prime_number(d):
            d += 1

        if N % d == 0:
            print(d)
            N = N // d
        else:
            d += 1

# 1929 소수 구하기
M, N = map(int,input().split())

def prime_number(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_list = []
for num in range(M,N+1):
    if num == 1:
        continue
    if prime_number(num):
        prime_list.append(num)
        continue

print("\n".join(map(str, prime_list)))

prime_list = [2]

M, N = map(int, input().split())
for num in range(2, M):
    for d in prime_list:
        if num % d == 0: # 소수 아니
            break
    else:
        prime_list.append(num)

for num in range(M, N+1):
    if num == 1:
        continue
    if num == 2:
        print(num)
        continue
    for d in prime_list:
        if num % d == 0:
            break
    else:
        prime_list.append(num)
        print(num)

m, n = map(int, input().split())
prime = [True for _ in range(n+1)] # 리스트를 미리 생성
prime[0], prime[1] = False, False # 0과 1은 False

for i in range(2, int((n**0.5)+1)): # 소수의 배수를 다 제거하므로, 최소 소수만 남으면 됨
    if prime[i]:
        for j in range(i*2, n+1, i): # 소수의 배수를 모두 False로
            prime[j] = False

for i in range(m, len(prime)):
    if prime[i]:
        print(i)

# 4948 베르트랑 공준
prime = [True for _ in range(123456*2+1)]
prime[0] = False
prime[1] = False

for idx in range(2,123456):
    if prime[idx]:
        for jdx in range(idx*2, 123456*2+1, idx):
            prime[jdx] = False

temp = int(input())
while temp:
    cnt = 0

    for num in range(temp+1, temp *2 +1):
        if prime[num]:
            cnt+= 1

    print(cnt)

    temp = int(input())

# 9020 골드바흐의 추측
prime = [True for _ in range(10001)]
prime[0] = False
prime[1] = False

for idx in range(2, 10001):
    if prime[idx]:
        for jdx in range(idx * 2, 10001, idx):
            prime[jdx] = False

T = int(input())

for _ in range(T):
    n = int(input())

    idx = 2
    dif, a, b = 1000, 0, 0
    while True:
        if prime[idx]:  # 소수인가?
            m = n - idx
            if prime[m]:  # 소수인가?
                if abs(idx - m) <= dif:
                    dif = abs(idx - m)
                    a, b = idx, m
                    idx += 1
                else:
                    idx += 1
            else:
                idx += 1
        else:
            idx += 1

        if idx == n:
            break

    if a > b:
        print(b, a)
    else:
        print(a, b)