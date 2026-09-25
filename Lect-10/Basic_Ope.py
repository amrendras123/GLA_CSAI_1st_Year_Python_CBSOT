

student_data={
    "name":"aman",
    "name":"amit",
    "name":"Daksh",
    "roll_Num":2,
    "add":"noida"
}
# data
name=input("enter your name")
student_data["name"]=name

print(student_data["name"])
print(student_data)

# Key

for key in student_data:
    print(key)

# Value

for avishka in student_data.values():
    print(avishka)

# key -> value
for key ,val in student_data.items():
    print(key ,"->",val)


# CW
student={
    "os":90,
    "cn":85,
    "phy":75,
    "python":80,
    "java":75,
    "c":50
}

print(student["os"])
print("os" in student)
# add -HTML ->60
# c-70 update
# delete -java
# print Value
# print key
# print key,value 
# print the name of subject sudent got marks 80 and above
# print total marks
# print average marks
# count subject marks less than 70
# print highest marks subject 
# print lowest marks subject 

