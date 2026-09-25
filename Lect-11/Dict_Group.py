list=["cat","dog","tiger","elephant","rat","orange","grapes","banana","five","python"]

# create a dictionary group word according to their length
# find length having maximum number of words

# ans={
#     3:["cat","dog","rat"],

# }

group={

}
# group each word by length
for i in list:
    l=len(i)
    if l in group:
        group[l].append(i)
    else:
        group[l]=[i]    
print(group)

max=0
maxKey=0
for key in group:
    curr=len(group[key])
    if curr>max:
        maxKey=key
        max=curr

print(maxKey)