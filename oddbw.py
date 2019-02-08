a=input().split()
N=int(a[0])
Q=int(a[1])
list=[]
for i in range(N+1,Q):
    if(i%2!=0):
    	list.append(i)
print(" ".join(map(str,list)))
