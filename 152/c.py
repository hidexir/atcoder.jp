n = int(input())
p = list(map(int, input().split()))

max = p[0]
ans = 0

for i, v in enumerate(p):
   if max >= v:
       ans += 1
       max = v

print(ans)
