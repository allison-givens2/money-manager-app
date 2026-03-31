"""
=== Category Methods ===
1. Constructor(str, float)
2. get_spent_amount
3. to_dict
4. from_dict
getters and setters
"""

# TODO: Create a Category class with the attributes name and budget_limit. All attributes should be declared as private.
#Category class
class Category:
    def __init__(self, name, budget_limit):
        self.__name = name
        self.__budget_limit = budget_limit

    # TODO: Write getters and setters for all attributes (2 getters and 2 setters)
    # getters and setters
    # function to get name
    def get_name(self):
        return self.__name

    # function to set name
    def set_name(self, name):
        self.__name = name

    # function to get budget limit
    def get_budget_limit(self):
        return self.__budget_limit

    # function to set budget limit
    def set_budget_limit(self, budget_limit):
        self.__budget_limit = budget_limit

    """
    This is a helper function for finding the category summaries
    """
    # TODO: Create a get_spent_amount method that uses a list of transactions to find the total spent from transactions in a certain category.
    #helper function that finds the total spent on transactions in a certain category
    def get_spent_amount(self, transactions):
        total = 0
        for t in transactions:
            if t.category == self.__name:
                if t.amount < 0:
                    total += t.amount
        return total

    # TODO: Write a to_dict method that will turn an object into a dictionary using the attribute names and values as key-value pairs.
    def to_dict(self):
        return {
            "name": self.__name,
            "budget_limit": self.__budget_limit
        }
    # TODO: Write a from_dict method that will use a dictionary parameter to create and return a Category object.
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            budget_limit=data.get("budget_limit")
        )