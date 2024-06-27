n,k = map(int ,input().split())
p = list(map(int, input().split()))

res = []
res.append(p[0])
for i in range(len(p)-1):
    res.append(res[i] + p[i+1])

print(res)