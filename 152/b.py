a,b = list(map(int, input().split()))

if a > b:
    ans = ''
    for target_list in range(a):
        ans = ans + str(b)

    print(ans)

if b > a:
    ans = ''
    for target_list in range(b):
        ans = ans + str(a)

    print(ans)
    

if b == a:
    ans = ''
    for target_list in range(b):
        ans = ans + str(a)

    print(ans)
