
no=int(input())
factorial = 1
if no < 0:
   print("Factorrial does not exist for negative numbers")
elif no== 0:
   print("1")
else:
   for i in range(1,no+ 1):
       factorial = factorial*i
   print(factorial)
