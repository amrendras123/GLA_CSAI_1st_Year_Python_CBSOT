def count_even_odd(n):
    odd=0
    even=0
    while n>0:
        dig=n%10
        if dig%2==0:
            even=even+1
        else:
            odd=odd+1
        n=n//10  
    print(f"odd count is {odd} even count is {even}")      
def palindrome(n):
    num=n
    rev=0
    while(num!=0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if rev==n:
        count_even_odd(n)
        return ("Palindrome")
    else:
        return("Not a Palindrome")

# num=int(input("Enter the number"))
print(palindrome(121))
print(palindrome(1221))
print(palindrome(12237381))