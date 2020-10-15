from datetime import datetime, date


class BankAccount:

    def __init__(self, name, bank_account_id, balance):
        self.__name = name
        self.__bank_account_id = bank_account_id
        self.__balance = balance
        self.__transactions = []

    def deposit(self, money):
        self.__balance += money - (money / 100)
        self.__transactions.append(money)
        self.__transactions.append("deposit")
        self.__transactions.append(date.today())

    def withdraw(self, money):
        self.__balance -= money + (money / 100)
        self.__transactions.append(money)
        self.__transactions.append("withdraw")
        self.__transactions.append(date.today())

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__bank_account_id

    def get_transaction(self):
        return self.__transactions

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


bank_account = BankAccount("Binko", 65, 100)
bank_account.deposit(300)
bank_account.withdraw(200)
bank_account.deposit(900)
print(bank_account.get_balance())
print(bank_account.get_transaction())