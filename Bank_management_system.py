
class Bank:
    def __init__(self,name,account,amount):
        self.name=name
        self.account=account
        self.amount=amount

    def Account(self):
        print("customer Name: ",self.name)
        print("account number: ",self.account)
        print("bank_balance: ",self.amount)
 
    def add(self,added):
        self.amount+=added  
        print("\nadded amount:", added)
        print("new_amount:", self.amount)

    def withdrall(self,withdraw):
        if withdraw<self.amount:
            self.amount-=withdraw
            print("\nwithdraw",withdraw)
        else:
            print("The amount is not sufficient")
        print("total money",self.amount)

s1=Bank("Zunaid Alam", 1234786,56000)

choice=int(input("do you want  to add=1 / remove=0: "))
if choice==1:
    addeed=int(input("\nEnter a number: "))
    s1.add(addeed)
if choice==0:
    remove=int(input("\nEnter a number: "))    
    s1.withdrall(remove)
