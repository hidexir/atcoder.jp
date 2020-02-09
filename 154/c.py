n = input()
a = list(map(int, input().split()))

def has_duplicates(seq):
    return len(seq) != len(set(seq))

ans = has_duplicates(a)
if ans:
    print("NO")
else:
    print("YES")