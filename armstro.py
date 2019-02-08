
m=int(input())
lll=list(map(int,str(m)))
bbb=list(map(lambda x:x**3,lll))
if(sum(bbb)==n):
    print("yes")
else:
    print("no")
