#Done: transaction.py
"""
=== Transaction Methods ===
1. Constructor(float, str, str, str)
getters and setters
"""

#Done: Transaction class
class Transaction:
    def __init__(self, amount, category_name, description, date):
        self.__amount = amount
        self.__category_name = category_name
        self.__description = description
        self.__date = date

    #Done: getters
    def get_amount(self):
        return self.__amount

    def get_category(self):
        return self.__category_name

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    #Done: setters
    def set_amount(self, amount):
        if not isinstance(amount, float):
            raise ValueError("Amount must be a monetary value!")
        self.__amount = amount

    def set_category_name(self, category_name):
        if not isinstance(category_name, str):
            raise ValueError("Category name must be a string!")
        self.__category_name = category_name

    def set_description(self, description):
        if not isinstance(description, str):
            raise ValueError("Description must be a string!")
        self.__description = description
