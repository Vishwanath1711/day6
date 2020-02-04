class consultant:
    def __init__(self,name="",skill="",exp=0):
        self.name1=name
        self.skill1=skill
        self.exp1=exp
    def __min__():
        if self.skill=="java" or self.skill1=="python" and self.exp1>=5 or self.exp<=10:
            pay=12000
        elif self.skill=="ai" or self.skill1=="python" and self.exp1>=3 or self.exp<=8:
            pay=7000
        elif self.skill=="java" or self.skill1=="python" or self.skill1=="c" or self.skill1=="c++"and self.exp1>=5 or self.exp<=10:
            pay=5000
    def __str__(self):
        return str(self.name1)+" "+str(self.skill1)+" "+str(self.exp1)+" "+(self.pay)
one=consultant("amar","python",6)
print(min())
