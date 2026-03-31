"""
=== Debt Methods ===
1. Constructor(str, float)
2. make_payment
3. get_remaining_balance
getters and setters
"""

#Debt class
class Debt:
    def __init__(self, name, total_amount):
        self.__name = name
        self.__total_amount = total_amount
        self.__amount_paid = 0

    #getters and setters
    #function to get name
    def get_name(self):
        return self.__name

    #function to set name
    def set_name(self, name):
        self.__name = name
    #function to get total amount
    def get_total_amount(self):
        return self.__total_amount

    #function to get amount paid
    def get_amount_paid(self):
        return self.__amount_paid

    #function to set amount paid
    def set_amount_paid(self, amount):
        self.__amount_paid = amount

    #function to set total amount
    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    #function that adds a payment to the amount paid on a debt based off of off user story 9
    def make_payment(self, payment):
        self.__amount_paid += payment

    #function that calculates how much debt is left to be paid based on user story 9
    def get_remaining_balance(self):
        return self.__total_amount - self.__amount_paid
    