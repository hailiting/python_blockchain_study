import datetime
class Transaction:
    def __init__(self, payer, recer, money):
        self.payer = payer
        self.recer = recer
        self.money = money
        self.timestamp = datetime.datetime.now()
    def __repr__(self):
        return  "Transaction: payer:{}, recer:{}, money:{}, timestamp:{} ".format(self.payer,self.recer, self.money, self.timestamp)

if __name__ =="__main__":
    t1=Transaction("小明","小红", "0.00001")
    print(t1)