class teller:
    def __init__(self,holder="",number="",balance=""):
        self.name=holder
        self.num=number
        self.bal=balance
    def __credit__(self,amount):
        self.amt=amount
        balance-=amt
        print(amt)
    def __debit__(self,amount):
        self.amt=amount
        balance+=amt
        print(amt)
    def __str__(self):
        return str(self.name)+" "+str(self.number)+" "+str(self.balance)
one=teller("amar","ab123","12345")
one+1000
