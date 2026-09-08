
n=int(input("enter the number"))

c=0
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        c+=1
        break
if(c>0):
    print(f"{n} not a prime number")
else:
    print(f"{n} is a prime number")


# c=0
# for i in range(2,n):
#     if n%i==0:
#         c+=1
#         break
# if(c>0):
#     print(f"{n} not a prime number")
# else:
#     print(f"{n} is a prime number")