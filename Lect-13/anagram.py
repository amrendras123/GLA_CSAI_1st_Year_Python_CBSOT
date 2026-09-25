s="amankumar"
s1="kumarnamp"
freq1={}
freq2={}

for i in s:
    if i in freq1:
        freq1[i]+=1
    else:
        freq1[i]=1

for j in s1:
    if j in freq2:
        freq2[j]+=1
    else:
        freq2[j]=1

if(freq1==freq2):
    print("Yes they are anagram")
else:
    print("No")