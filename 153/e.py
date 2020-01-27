from sys import stdin
readline = stdin.readline

H, N = map(int, readline().split())
AB = [list(map(int, readline().split())) for _ in range(N)]

# 最初に入力の最大値と最大量でdp配列を作成
dp = [100000000] * (H + 10 ** 4 + 1)
dp[0] = 0

for i in range(H):
    if dp[i] == 100000000:
        continue
    for a, b in AB:
        # tは100000000 + 消費魔力
        t = dp[i] + b
        # dp[i + a] aはダメージ量
        if t < dp[i + a]:
            dp[i + a] = t

print(min(dp[H:]))

def main():
    from sys import stdin
    readline = stdin.readline
    H, N = map(int, readline().split())
    AB = [list(map(int, readline().split())) for _ in range(N)]

    dp = [100000000] * (H + 10 ** 4 + 1)
    dp[0] = 0
    for i in range(H):
        if dp[i] == 100000000:
            continue
        for a, b in AB:
            t = dp[i] + b
            if t < dp[i + a]:
                dp[i + a] = t
    print(min(dp[H:]))


main()
