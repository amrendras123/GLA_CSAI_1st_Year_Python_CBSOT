n=407
n=str(n)
sum=0
l=len(n)
for i in n :
    i=int(i)
    sum=sum+pow(i,l)
    # sum=sum+i**l
    
n=int(n)
if sum == n:
    print("yes")
else:
    print("no")

