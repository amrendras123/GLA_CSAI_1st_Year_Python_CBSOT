
# a=10

# def hello():
#     print("hello world")

# hello()

# def sum(a,b):
#     return a+b
# def sum(a,b):
#     print("no return type")
#     print(a+b)

# sum(5,5)

# c=sum(5,5)
# print(c)
# def sum(a,b,c):
#     print(a+b+c)

# print(sum("hi","hello"))
# print(sum(2,3))


# def oper():
#     b=10
#     c=20
#     return b+c

# print(oper(5,10))    
# print(c)

b=10
c=50
def oper1():
    return b+c,b-c,b*c,b/c

print(oper1())
sum,sub,mul,div=oper1()
print(sum,sub,mul,div)
