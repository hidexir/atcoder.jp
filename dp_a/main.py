import copy

# N = int(input())
# H = list(map(int, input().split()))

N = 4
H = [10, 30, 40, 20]


l = [0] * N
all = []

def check (n):
    if n == N:
        b = copy.deepcopy(l)
        all.append(b)
        return

    for i in range(1, 3):
        l[n] = i
        check(n+1)

check(0)

def count_cost(data,i):
    if i >= N:
        return

    next_index = data[i]
    print(next_index)
    count_cost(data,i+next_index)


for data in all:
    count_cost(data,0)


