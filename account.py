""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account:
    
    def __init__(self, name, bal):
        self._name = name
        self._bal = bal
    
    def get_bal(self, bal):
        return(self._bal)

    def get_acc_info(self, name, bal):
        return(self._name, self._bal)

    def set_name(self, name, new_name):
        if new_name == name:
            raise ValueError("No name change detected")
        self._name == new_name

    def set_bal(self, bal, new_bal):
        if new_bal == bal:
            raise ValueError("No balance change detected")
    
    def depo(self, bal, depo_amm):
        if depo_amm <= 0:
            raise ValueError("Deposit amount can't be less than 0")
        self._bal += self.depo_amm

    def withdraw(self, bal,  withdraw_amm):
        if withdraw_amm >= bal:
            raise ValueError("Withdraw amount cant be larger than your current balance")
        self._bal -= self.withdraw_amm