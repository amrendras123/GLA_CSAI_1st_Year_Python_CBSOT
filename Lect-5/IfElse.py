# marks=int(input("enter your marks: "))

# if marks>=90 and marks<=100:
#     print("A+")
# elif marks>=80 and marks<90:
#     print("A")
# elif marks>=70 and marks<80:
#     print("B+")
# elif marks>=60 and marks<70:
#     print("B")    
# elif marks>=50 and marks<60:
#     print("C")
# else:
#     print("fail")   

marks=int(input("enter your marks: "))

if marks<0 or marks>100:
    print("invalid input")  
elif marks>=90:
    print("A+")
    if marks>=95:
        print("excellent")
        if marks==100:
            print("got full marks")  
elif marks>=80:
    print("A")
elif marks>=70:
    print("B+")
elif marks>=60:
    print("B")    
elif marks>=50:
    print("C")
else:
    print("fail")      