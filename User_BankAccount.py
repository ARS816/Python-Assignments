class CheckingAccount:
    all_accts = []
    def __init__(self, balance):
        self.balance = balance
        CheckingAccount.all_accts.append(self)
    
    def display_acct_info(self):
        print('Checking account balance:', self.balance)
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficent funds')
        else:
            self.balance = self.balance - amount
    @classmethod
    def all_accounts(cls):
        for account in cls.all_accts:
            account.display_acct_info()


class SavingsAccount:
    all_accts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        SavingsAccount.all_accts.append(self)
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficent funds')
        else:
            self.balance = self.balance - amount

    def display_acct_info(self):
        print('Savings account balance:', self.balance)

    def yield_int(self):
        if self.balance > 0:
            self.balance = round(self.balance + (self.balance * self.int_rate), 2)
            return self

    @classmethod
    def all_accounts(cls):
        for account in cls.all_accts:
            account.display_acct_info()

class User:
    all_users = []
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email= email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        self.checking = CheckingAccount(balance=0)
        self.savings = SavingsAccount(int_rate=0.02, balance=0)

    def make_deposit(self, check_amt, save_amt):
        self.checking.deposit(check_amt)
        self.savings.deposit(save_amt)
        if check_amt > 0:
            print('You have made a deposit of', check_amt ,'dollars to your checking account')
        if save_amt > 0:
            print('You have made a deposit of', save_amt ,'dollars to your savings account')
    
    def make_withdrawal(self, check_amt, save_amt):
        self.checking.withdraw(check_amt)
        self.savings.withdraw(save_amt)
        if check_amt > 0:
            print('You have withdrawn', check_amt ,'dollars from your checking account')
        if save_amt > 0:
            print('You have withdrawn', save_amt ,'dollars to from savings account')
    
    def display_balance(self):
        self.checking.display_acct_info()
        self.savings.display_acct_info()
    
    def transfer_between_accts(self, from_checking, from_savings):
        self.checking.balance = self.checking.balance + from_savings
        self.savings.balance = self.savings.balance - from_savings
        self.checking.balance = self.checking.balance - from_checking
        self.savings.balance = self.savings.balance + from_checking

    def tranfer_to_users(self, amount, user_other):
        if self.checking.balance < amount:
            print('Insufficent funds')
        else: 
            self.checking.balance = self.checking.balance - amount
            user_other.checking.balance = user_other.checking.balance + amount
        
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    
    def enroll(self):
        if self.is_rewards_member == True:
            print('An account for this member already exists.')
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print('Thank you for joining. Your new Gold Card balance is', self.gold_card_points)
        return self

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points = self.gold_card_points - amount
            print('You have spent', amount, 'points. Your remaining Gold Card balance is', self.gold_card_points)
        else:
            print('Insufficent Funds')
        return self
    
    @classmethod
    def all_accounts(cls):
        for account in cls.all_accts:
            account.display_acct_info()


aimee = User('Aimee','Santone', 'as123@gmail.com', '27', True, 350)
harrison = User('Harrison', 'Redden', 'harry98@rocketmail.com','25')
joe = User('Joe', 'Santone', 'jmsantone@sbcglobal.net', '29', True, 224)

aimee.make_deposit(650,2000)
aimee.tranfer_to_users(700, harrison)
aimee.transfer_between_accts(0,100)
aimee.tranfer_to_users(700, harrison)
aimee.display_balance()


