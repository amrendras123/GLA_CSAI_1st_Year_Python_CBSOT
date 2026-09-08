
# single quote
# s='abc'
# print(id(s))
# # double quote
# s1="Abc"
# print(id(s1))
# print('abc'=="abc")

# triple quote

# sent="""welcome to cbsot
# welcome to gla university"""

# print(sent)


# indexing
# s="python"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(s[-2])
# print(s[6])  string index out range

# slicing

# s="python"

# print(s[:]) 
# print(s[:5])
# print(s[1:6])
# print(s[-1:-5])
# print(s[::-1])
# print(s[::2])
# print(s[-3:-6:-1])


# immutable
# s="python"
# s[1]='t'
# print(s)

# s1="j"+s[1:]
# print(s1)

# s2=s[:2]+"x"+s[3:]
# print(s2)

# 
# s="hi "
# print(4*s)

# for i in range(5):
#     print(s)

# concatination
# f_name="ram"
# l_name="kumar"
# name=f_name+" "+l_name
# print(name)
# print(len(name))
# length len(variable_name)
# s="python"
# print(len(s))
# print(str(6)+"5")

# for i in range(len(s)):
#     print(type(i))
#     print(s[i])

# for i in s:
#     # print(type(i))
#     print(i)

# print("P" in s)    
# print("t" not in s)

# # 
# s1="Hello World"
# print(s1.lower())
# print(s.upper())


# find()
# str="honello python"
# print(str.find(""))
# print(str.find("h"))
# print(s[1:1])

# n=1234
# output=1+2+3+4=10

# n=int(input("Enter the number"))
# num=n
# sum=0
# while n>0:
#     dig=n%10
#     if dig%2!=0:
#       sum=sum+dig
#     n=n//10
# print(f"sum of odd digits of {num} is {sum}")



# reverse
n=int(input("enter a number : "))
num=n
rev=0
while n>0:
   rem=n%10
   rev=rev*10+rem
   n=n//10

print(rev==num)




