n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
INF = 1 << 30


# binary prefix 제거
def del_prefix(bin_num):
    return bin_num[2:]


# n 비트로 나타낼 때
def nbit(bin_num):
    bin_num = del_prefix(bin_num)
    return bin_num.zfill(n)


def solve(pos, visited):
    # 모두 방문했을 경우 matrix 반환, matrix가 false일 경우 INF 반환
    if visited == cpl:
        print([pos+1, start+1], "가중치 : ", matrix[pos][start])
        return matrix[pos][start] or INF

    # 이미 방문했을 경우
    if DP[pos][visited]:
        return DP[pos][visited]

    ans = INF
    for i in range(n):
        print([pos+1, i+1], "\t가중치 :", matrix[pos][i], '\t방문 여부 :', True if visited & (1 << i) else False)
        # 경로가 존재하고, i번째 도시(다음 도시)에 방문을 하지 않았을 떄
        if matrix[pos][i] and not visited & (1 << i):
            print("다음 방문지 :", i+1)
            print()
            # visited | (1 << i) 는 i 번째 도시를 방문한 것으로 check 하는 과정
            ans = min(ans, solve(i, visited | (1 << i)) + matrix[pos][i])

    # 현재위치 pos 에서 방문상태가 visited 일때 value는 나머지를 순회하는 비용
    DP[pos][visited] = ans
    print("\n===start")
    for line in DP:
        print(line)
    print("===end\n")

    return ans


answer = INF
start = 0

cpl = (1 << n) - 1
DP = [[0] * (1 << n) for _ in range(n)]
"""
EX) 4개의 도시 : A, B, C, D
방문 상태 표시를 위해 비트마스크 사용
1. A, B, C, D 방문 : 1111
2. A, C 방문 : 1010
3. A 방문 : 1000
"""


answer = min(answer, solve(start, 1 << start))
print(answer)

"""
4
0 10 15 20
5  0  9 10
6 13  0 12
8  8  9  0

3
0 5 1
7 0 9
10 20 0

2
0 2
1 0
"""