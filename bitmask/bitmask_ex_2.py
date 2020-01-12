# 에라토스테네스의 체 예제

import math


# binary prefix 제거
def del_prefix(bin_num):
    return bin_num[2:]


# 8비트로 나타낼 때
def bit_8(bin_num):
    bin_num = del_prefix(bin_num)
    return bin_num.zfill(8)


# 1. 체의 크기를 2의 8승으로 임의로 지정
SIZE = 2 ** 8 + 1

# 2. 체를 8비트 단위로 나누기
sieve = [255 for _ in range(SIZE // 8 + 1)]


# n이 속한 체의 원소를 찾고, 속한 원소에서 n에 해당하는 비트를 0으로 설정
def set_composite(n):
    sieve[n >> 3] &= ~(1 << (n & 7))


"""
1. n이 속한 체의 원소 찾기 seive[n >> 3] : 8로 나누기
2. n & 7 : 8로 나눈 나머지
3. 1 << (n & 7) : 찾은 원소 안에서의 위치
4. sieve[8 >> 3] &= ~(1 << (8 & 7)) : 해당 원소의 위치를 0으로 설정
"""
print("8이 속한 원소의 위치 : ", 8 >> 3)
print("8을 7로 나눈 나머지 : ", 8 & 7)
print("원소 안에서 8의 위치 : ", 1 << (8 & 7))

# 해당하는 위치를 0으로 초기화 : 8의 경우 1111 1111 -> 1111 1110
print(~(1 << (8 & 7)))
print(255 & ~(1 << (8 & 7)))
sieve[8 >> 3] &= ~(1 << (8 & 7))

# 결과
print(sieve, end="\n\n")

# 3. 0과 1은 소수가 아니기 때문에 0으로 설정
set_composite(0)
set_composite(1)


# prime 판별
def is_prime(n):
    # print(sieve[n >> 3])
    # print(1 << (n & 7))
    # print(bit_8(bin(sieve[n >> 3])))
    # print(bit_8(bin(1 << (n & 7))))
    return True if sieve[n >> 3] & (1 << (n & 7)) else False


# 체 만들기
for i in range(2, int(math.sqrt(SIZE))):
    if is_prime(i):
        # i*i 보다 작은 원소는 이미 지워졌으므로 신경쓸 필요 없음
        for j in range(i*i, SIZE+1, i):
            set_composite(j)

print(sieve)

print(is_prime(127))
print(is_prime(255))

ff = 1
if not ff:
    print("시발")