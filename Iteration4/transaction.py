"""
=== Transaction Methods ===
1. Constructor(float, str, str, str)
getters and setters
"""

#Transaction class
class Transaction:
    def __init__(self, amount, category_name, description, date):
        self.__amount = amount
        self.__category_name = category_name
        self.__description = description
        self.__date = date

    #getters and setters
    #function to get amount
    def get_amount(self):
        return self.__amount

    #function to set amount
    def set_amount(self, amount):
        self.__amount = amount

    #function to get category name
    def get_category_name(self):
        return self.__category_name

    #function to set category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    #function to get description
    def get_description(self):
        return self.__description

    #function to set description
    def set_description(self, description):
        self.__description = description

    #function to get date
    def get_date(self):
        return self.__date

    #function to set date
    def set_date(self, date):
        self.__date = date