S="programmingp"

# find first unique character /non repeating character of given string


s = "programminpgo"
freq={}

for ch in s :
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in s :
    if freq[ch]==1:
        print(ch)
        break
