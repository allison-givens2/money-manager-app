#Done: debt.py
"""
=== Debt Methods ===
1. Constructor(str, float)
2. make_payment
3. get_remaining_balance
getters and setters
"""

#Done: Debt class
class Debt:
    def __init__(self, name, total_amount, amount_paid):
        self.__name = name
        self.__total_amount = total_amount
        self.__amount_paid = amount_paid

    #Done: getters
    def get_name(self):
        return self.__name

    def get_total_amount(self):
        return self.__total_amount

    def get_amount_paid(self):
        return self.__amount_paid

    #Done: setters
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string!")
        self.__name = name

    def set_total_amount(self, total_amount):
        if not isinstance(total_amount, float):
            raise ValueError("Amount must be a monetary value!")
        self.__total_amount = total_amount

    def set_amount_paid(self, amount_paid):
        if not isinstance(amount_paid, float):
            raise ValueError("Amount must be a monetary value!")
        if amount_paid < 0:
            raise ValueError("Amount must be positive!")
        self.__amount_paid = total_amount

    """
    User Story 9. Track a Debt Payment: As a user, I need to track a payment to my debt so that I can reduce my balance.
    """
    #Done: make_payment method
    def make_payment(self, amount_paying):
        #validate amount is a monetary value
        if not isinstance(amount_paying, float):
            raise ValueError("Amount must be a monetary value!")
        #validate amount is non-negative
        if amount_paying < 0:
            raise ValueError("Amount must be positive!")
        #validate amount is not greater than debt
        if amount_paying > self.__total_amount:
            raise ValueError("Amount must be less than or equal to the total amount!")
        self.__amount_paid += amount_paying

    """
    User Story 10. View Remaining Balance: As a user, I need to see the remaining balance for my debt so that I know what’s left to pay.
    """
    #Done: get_remaining_balance method
    def get_remaining_balance(self):
        #calculate balance left
        return self.__total_amount - self.__amount_paid
    