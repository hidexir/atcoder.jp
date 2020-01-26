d = int(input())

kaisu = 0

def atack(tairyoku):
    global kaisu

    if tairyoku < 2.99999:
        return

    kaisu += 1
    atack(tairyoku/2)

atack(d)

ans = 0
def keisan(x):
    global ans
    if x <= 1:
        return
    ans += x
    keisan(int(x/2))

keisan(2**kaisu + 1)

print(ans)