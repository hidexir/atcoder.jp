import sys

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
n = int(input())
b = [int(input()) for i in range(n)]

a1.extend(a2)
a1.extend(a3)
result = []

for target_list in b:
    try:
        result.append(a1.index(target_list)+1)
    except:
        continue        

ans = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],[2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


for target_list in ans:
    tmp = set(target_list) & set(result)
    if len(tmp)>=3:
        print("Yes")
        sys.exit()

print("No")    
