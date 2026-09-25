s="abcabcabc"
print(set(s))

# output s1="abc" 

s1=""

for ch in s:
    if ch not in s1:
        s1=s1+ch

print(s1)