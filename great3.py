n=input().split()
aa=int(n[0])
bb=int(n[1])
cc=int(n[2])
if(aa>bb and aa>cc):
  print(aa)
elif(bb>aa and bb>cc):
  print(bb)
elif(cc>aa and cc>bb):
  print(cc)
else:
  print("Invalid")
