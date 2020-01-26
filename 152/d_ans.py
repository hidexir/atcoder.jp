n = int(input())
d = [[0]* 9 for _ in range(9)]
 
for num in range(1, n+1):
    str_num = str(num)
    if str_num[-1] != "0":
        start = int(str_num[0]) - 1
        end = int(str_num[-1]) - 1
        d[start][end] += 1
 
ans = 0
for i in range(9):
    for j in range(9):
        ans += d[i][j] * d[j][i]
 
print(ans)
