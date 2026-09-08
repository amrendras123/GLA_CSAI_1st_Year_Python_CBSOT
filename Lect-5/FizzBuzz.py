n=int(input("enter the number"))

if n%3==0 and n%5==0:
    print("fizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print(n)            
