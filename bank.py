""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account

class Bank:

    def __init__(self, name, bal):
        self._accounts = []
    
    def create_acc(self, name, bal):
        for account in self._accounts:
            if name == name.get_acc_info():
                raise ValueError("Account already exists")
        self._accounts.append(name)

    def del_acc(self, name):
        for account in self._accounts:
            if name != name.get_acc_info():
                raise ValueError("Account doesn't exist")
        self._accounts.remove(account)

    def transfer(self, name, bal):
        for account1 in self._accounts:
            if name != name.get_acc_info():
                raise ValueError("Transaction Canceled, Account Doesn't Exist")
        for account2 in self._accounts:
            if name != name.get_acc_info():
                raise ValueError("Transaction Canceled, Account Doesn't Exist")
         
    def depo(self, name, bal, depo_amm):
        for account in self._accounts:
            if name != name.get_acc_info(account):
                raise ValueError("Account doesn't Exist")
        self.depo(depo_amm)

    def withdraw(self, name, withdraw_amm):
        for account in self._accounts:
            if name == account._name:
                account.withdraw(withdraw_amm)

    create_acc("Jeff", 12.00)
    withdraw(12)