#Done: category.py
"""
=== Category Methods ===
1. Constructor(str, float)
2. get_spent_amount
getters and setters
"""

#imports
from transaction import Transaction

#Done: Category class
class Category:
    #initialization
    def __init__(self, name, budget_limit):
        self.__name = name
        self.__budget_limit = budget_limit

    #Done: getters
    def get_name(self):
        return self.__name

    def get_budget_limit(self):
        return self.__budget_limit

    #Done: setters
    def set_name(self, name):
        #validate name is a string
        if not isinstance(name, str):
            raise ValueError("Name must be a string!")
        #set name
        self.__name = name

    def set_budget_limit(self, budget_limit):
        #validate budget is monetary value
        if not isinstance(budget_limit, float):
            raise ValueError("Budget limit must be a monetary value!")
        #validate budget is non-negative
        if budget_limit < 0:
            raise ValueError("Budget limit cannot be negative!")
        self.__budget_limit = budget_limit

    """
    This is a helper function for finding the category summaries
    """
    #Done: get_spent_amount method
    def get_spent_amount(self, transactions):
        #variable to keep track of spending
        spent_amount = 0
        #loop through transactions, determine if category matches, and if so add them to spending
        for transaction in transactions:
            if transaction.get_category_name() == self.__name:
                spent_amount += transaction.get_amount()
        return spent_amount