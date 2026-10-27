
dict={
    1:"abc",
    2:"bcd",
    3:"aman",
    4:"ram",
    5:"shyam",
    6:"def"
}
for x in dict:
    if x%2==0:
        print(dict[x])
# if 4 in dict:
#     print("4 is available")



# print(dict.keys())
# print(dict.values())
# print(dict.items())








# print(dict.get(4,"roll doesnt exist"))

# print(dict[3])
# print(dict[4])

data={
    "aman":20,
    "amit":40,
    "abc":60,
    "ram":67,
    "om":90
}
# print(type(data))
# # print(data[67])
# print(data.get("aman","key does not exist"))
# # crud

# data1={3,4,5,6,6,6,8}

# print(data1)

# print( type(data1))


# find frequency of each character
s="pppyyttthonnnnonnp"
freq={}

for ch in s:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1    

print(freq)

# count vowel in the given string
s="pythonprogramming"

s1="aeiouAEIOU"
vcount=0
for ch in s:
    if ch in s1:
        print(ch)
        vcount+=1

print(vcount)


# reverse vowel of string

s2="python"
l=list(s2)
print(l.reverse())
print(l[::-1])