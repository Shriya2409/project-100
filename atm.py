class Atm(object):
    def __init__ (self, user, cardNumber, pinNumber):
        self.user=user
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def CashWithdrawl(self):
        print("Cash has been withdrawd")
    def BalanceEnquiry(self):
        print("Your balance is: ___")
BalanceEnquiry()   
CashWithdrawl()     