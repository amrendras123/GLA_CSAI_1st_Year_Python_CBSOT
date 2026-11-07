
# l=[1,2,3]

# print(type(l))


class BankAccount:
    def __init__(self,bal,address):
        self.bal=bal
        self.type="current"
        self._address=address
        self.__pin=1234
    def pin(self):
        print(self.__pin)
    def display(self):
        print(self.bal,self._address,self.type)    
        # self.__pin=123



class Bank1(BankAccount):



# b1=Bank1()


# b1=BankAccount(5000,"bcde")
# b1.pin()
# print(b1._address)
# print(b1.bal)
# b1.display()