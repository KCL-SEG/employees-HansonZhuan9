"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission = ''):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        if self.commission:
            return self.contract.salary() + self.commission.totalCommision()
        else:
            return self.contract.salary()

    def __str__(self):
        if self.commission:
            return f'{self.name} works on a {self.contract} and receives a {self.commission}.  Their total pay is {self.get_pay()}.'
        else:
            return f'{self.name} works on a {self.contract}.  Their total pay is {self.get_pay()}.'
        
class Contract:
    def __init__(self, type, pay, hours=0):
        self.type = type
        self.pay = pay
        self.hours = hours
    
    def salary(self):
        if self.hours:
            return self.pay * self.hours
        else:
            return self.pay
        
    def __str__(self):
        if not self.hours:
            return f'monthly salary of {self.pay}'
        else:
            return f'contract of {self.hours} hours at {self.pay}/hour'

class Commission:
    def __init__(self, type , amount, number=1):
        self.type = type
        self.amount = amount
        self.number = number
    
    def totalCommision(self):
        return self.amount * self.number
    
    def __str__(self):
        if self.number == 1:
            return f'{self.type} commission of {self.amount}'
        else:
            return f'commission for {self.number} contract(s) at {self.amount}/contract'
        



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
contract_bi = Contract('monthly', 4000)
billie = Employee('Billie',contract_bi)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
contract_ch = Contract('hourly', 25, 100)
charlie = Employee('Charlie',contract_ch)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
contract_re = Contract('monthly', 3000)
commission_re = Commission('contract', 200, 4)
renee = Employee('Renee',contract_re,commission_re)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
contract_ja = Contract('hourly', 25, 150)
commission_ja = Commission('contract', 220, 3)
jan = Employee('Jan',contract_ja,commission_ja)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
contract_ro = Contract('monthly', 2000)
commission_ro = Commission('bonus', 1500)
robbie = Employee('Robbie',contract_ro,commission_ro)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
contract_ar = Contract('hourly', 30, 120)
commission_ar = Commission('bonus', 600)
ariel = Employee('Ariel',contract_ar,commission_ar)
