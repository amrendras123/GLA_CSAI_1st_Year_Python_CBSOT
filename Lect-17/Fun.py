def f(a,b):
    return a+b

# print(f(2,3))

# variable number of args
def f1(*args):
    return sum(args)


# print(type(f1))

# print(type(sum))

# print(f1(2,3))
# print(f1(2,3,4,5,6))
# print(f1(2,3,4,5,7,8,9,1,1,1,1,1,2.13))
# print(f1(2,3,10))

# arguments
# def student(name,age,roll):
#     print(f"name={name} ,age={age} , roll={roll}")

# student(age=18,name="abc",roll=1)

# diff between print and return   

# square

def square(n):
    return n*n

print(square(2))

for i in range(n):
    print(i)