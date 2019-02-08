n=int(input())
aa=list(map(int,str(n)))
bb=list(map(lambda x:x**3,aa))
if(sum(bb)==n):
    print("yes")
else:
    print("no")
