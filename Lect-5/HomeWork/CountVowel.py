str="AbcdaeioU1234455"
count=0;
# for ch in str:
#     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
#         count=count+1

# print(count)
conCount=0
# for ch in str:
#     if ch in "aeiouAEIOU":
#         count=count+1
#     else:
#         conCount=conCount+1

# print(count)
str="abcAEIOUqwr123"
vCount=0
Ccount=0
for ch in str:
    if ch.isalpha()==True:
        if ch.lower() in "aeiou":
            vCount=vCount+1
        else:
             Ccount=Ccount+1    

print(f"consonent is  {Ccount} and Vowel is {vCount}")