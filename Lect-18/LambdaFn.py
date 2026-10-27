# n=int(input())

# fn=lambda n:n*2
# print(fn(n))
# print(type(fn))


# sum=lambda a,b,c:a+b+c

# print(sum(2,3,4))
# #odd even
# def f1(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")    


f1=lambda x:"even" if x%2==0 else "odd"
print(f1(5))

l=[1,2,3,4,5]

# lambda x:x*x

# list=list(map(lambda x:x*2 ,l))
print(list(map(lambda x:x*2 ,l)))

fl=list(filter(lambda x:x%2==0,l))
print(fl)
# print(list(filter()))

print( (lambda a,b:a+b)(4,5))
print((lambda x:x*x)(5))