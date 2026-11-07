# class car:
#     def run(self):
#         print("car can run")



# c1=car()
# c2=car()
# c1.run()
# c2.run()

class student:
    college="GLA university"  
    # def __init__(self,name,uniroll,address):
    #     self.name=name
    #     self.uniroll=uniroll
    #     self.address=address
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def test(self,name1):
        print("success")
    def test(self,name1 ,age):
        print(name1, age)    
    def prnt(self):
        print(self.name,self.uniroll,self.address)

s3=student("abc","bcd")
# s3.
print(s3.address)
s3.test("a",19)
s3.test("ab",23)
# s1=student("pranshu",23,"abc")
# s1.prnt()
# print(s1.name)
# print(s1.college)
# s2=student("abc",2,"def")

