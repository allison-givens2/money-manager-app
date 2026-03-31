"""
=== Transaction Methods ===
1. Constructor(float, str, str, str)
2. get_spent_amount
3. to_dict
4. from_dict
getters and setters
"""

# TODO: Create a Transaction class with the attributes amount, category_name, description, and date. All attributes should be
#       declared as private.
#Transaction class
class Transaction:
    def __init__(self, amount, category_name, description, date):
        self.__amount = amount
        self.__category_name = category_name
        self.__description = description
        self.__date = date

    # TODO: Write getters and setters for all attributes (4 getters and 4 setters)
    #getters and setters
    #function to get amount
    def get_amount(self):
        return self.__amount

    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a to_dict method that will turn an object into a dictionary using the attribute names and values as key-value pairs.
    def to_dict(self):
        return {
            "amount": self.__amount,
            "category_name": self.__category_name,
            "description": self.__description,
            "date": self.__date
        }

    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a from_dict method that will use a dictionary parameter to create and return a Transaction object.
    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data.get("amount"),
            category_name=data.get("category_name"),
            description=data.get("description"),
            date=data.get("date")
        )