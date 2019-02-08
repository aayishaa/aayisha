l=input().split()
m=int(l[0])
n=int(l[1])
for num in range(m,n):
  temp=num
  sum=0
  while temp>0:
      digit=temp%10
      sum=sum+digit**3
      temp=temp//10
      if sum==num:
           print (num)
