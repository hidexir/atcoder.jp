import sys

n = list(map(int, input().split()))
b = [list(map(int, input().split())) for i in range(n[1])]
keta = n[0]
ans = [0] * keta
ans[0] = 1


for target_list in b:
    key = target_list[0]
    value = target_list[1]
    if key == 1:
        ans[key - 1] = value
    elif value == 0:
        ans[key-1] = value
    elif ans[key-1] == 0:
        ans[key-1] = value
    elif ans[key-1] > value:
        ans[key-1] = value
    else:
        pass

for target_list in range(keta):
    if len(ans) == 1:
        break
    if ans[target_list] == 0:
        print("-1")
        sys.exit()
    else:
        break

h = "".join(map(str, ans))
print(h)