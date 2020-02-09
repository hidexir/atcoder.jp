s, t = map(str,input().split())
num_s, num_t = map(int,input().split())
del_target = input()


data  = {s:num_s,t:num_t}
data[del_target] = data[del_target]-1

print(data[s],data[t])
