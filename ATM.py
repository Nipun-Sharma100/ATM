class atm(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber


    def withdrawal(self):
        print("withdrawed")

    def inquiry(self):
        print("inquired")

card=atm("abcdef","123456")
card.withdrawal()
card.inquiry()
