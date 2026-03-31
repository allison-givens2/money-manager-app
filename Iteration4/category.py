"""
=== Category Methods ===
1. Constructor(str, float)
2. get_spent_amount
getters and setters
"""

#Category class
class Category:
    def __init__(self, name, budget_limit):
        self.__name = name
        self.__budget_limit = budget_limit

    #getters and setters
    #function to get name
    def get_name(self):
        return self.__name

    #function to set name
    def set_name(self, name):
        self.__name = name

    #function to get budget limit
    def get_budget_limit(self):
        return self.__budget_limit

    #function to set budget limit
    def set_budget_limit(self, budget_limit):
        self.__budget_limit = budget_limit

    #helper function that finds the total spent on transactions in a certain category
    def get_spent_amount(self, transactions):
        total = 0
        for t in transactions:
            if t.category == self.__name:
                if t.amount < 0:
                    total += t.amount
        return total