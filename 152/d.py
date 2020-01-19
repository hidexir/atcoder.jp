import sys
sys.setrecursionlimit(10000)

n = int(input())
ans = 0

def check(a,b):
    if list(str(a)[0]) == list(str(b)[-1]) and list(str(a)[-1]) == list(str(b)[0]) :        
        global ans
        ans += 1

    if a >= n:        
        return ans
    if b >= n:  
        check(a+1,1)
        return
    
    check(a,b+1)

check(1,1)

print(ans)
