

# find freq of each char using dictionary 
s="programming"

freq={}

for char in s:
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1

# print(freq)

# p ->1
# r ->2
# o ->1
# .
# .
