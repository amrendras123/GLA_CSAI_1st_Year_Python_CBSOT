n=int(input("enter the number"))

a=0
b=1
# for i in range(n+1):
#     c=a+b
#     print(a,end=" ")
#     a=b
#     b=c

i=0
while i<=n:
    c=a+b
    print(a,end=" ")
    a=b
    b=c
    i+=1
