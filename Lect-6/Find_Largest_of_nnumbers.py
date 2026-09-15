import math
max=-math.inf
n=int(input("Enter the value of n :"))
list=[]

i=0
# n inputs from the user
while i<n:
    num=int(input("enter the number"))
    list.append(num)
    i+=1

j=0
# find max of given n number from the list
while j<len(list):
    if list[j]>max:
        max=list[j]
    j+=1
print("maximum number is ",max)
# for i in range(n):
#     num=int(input("Enter the number : "))
#     if num>max:
#         max=num
# print("largest number is ",max)        

# j=0
# while j<n:
#     num=int(input())
#     if num>max:
#         max=num
#     j+=1    
# print("largest number is ",max)          