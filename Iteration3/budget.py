"""
=== Budget Methods ===
1. Budget(float, list, list, list, list)
2. add_transaction(float, str, str, str): void
3. get_total_spent(): float
4. get_transaction_choices(): list of tuples
5. get_remaining_budget(): float
6. add_category(str, float): void
7. get_category_by_name(str): Category
8. add_debt(str, float, float): void
9. get_debt_choices(): list of tuples
10. add_sinking_fund(str, float, float): void
11. get_fund_choices(): list of tuples
12. get_transaction_by_index
13. delete_transaction_by_index
14. get_debt_by_index
15. delete_debt_by_index
16. get_sinking_fund_by_index
17. delete_sinking_fund_by_index
18. get_summary_by_category
19. get_category_summary
"""

#imports
from category import Category
from debt import Debt
from sinking_fund import Sinking_Fund
from transaction import Transaction

#Done: Budget class
class Budget:
    def __init__(self):
        self.__monthly_income = 0
        self.__categories = []
        self.__transactions = []
        self.__sinking_funds = []
        self.__debts = []

    """
    User Story 2.	Add a Transaction: As a user, I need to add a transaction so that I can record my spending.
    """
    #Done: add_transaction method
    def add_transaction(self, amount, category_name, description, date):
        new_transaction = Transaction(amount, category_name, description, date)
        self.__transactions.append(new_transaction)

    """
    User Story 13.	View Total Spent: As a user, I need to see my total spent in a month so that I can track my overall spending.
    """
    #Done: get_total_spent method
    def get_total_spent(self):
        total_spent = 0
        for transaction in self.__transactions:
            total_spent += transaction.get_amount()
        return total_spent

    """
    User Story As a user, I need to view all my transactions so that I can review past activity.
    """
    #Done: get_transaction_choices method
    def get_transaction_choices(self):
        choices = []
        for index, transaction in enumerate(self.__transactions, start=1):
            date = transaction.get_date()
            description = transaction.get_description()
            amount = transaction.get_amount()
            category = transaction.get_category_name()
            formatted = f"{date} - {description} (${amount:.2f}) in {category}"
            choices.append((index, formatted))
        return choices

    """"
    User Story 14.	See Remaining Budget: As a user, I need to see my remaining budget so that I can avoid overspending.
    """
    #Done: get_remaining_budget method
    def get_remaining_budget(self):
        remaining = self.__monthly_income - self.get_total_spent()
        return remaining

    """
    User Story 4. Add a Category: As a user, I need to add a category so that I can organize my transactions.
    """
    #Done: add_category method
    def add_category(self, name, budget_limit):
        new_category = Category(name, budget_limit)
        self.__categories.append(new_category)

    """
    This will be used in a later function to retrieve a desired category.
    """
    #Done: get_category_by_name
    def get_category_by_name(self, name):
        for category in self.__categories:
            if category.get_name() == name:
                return category
        return None

    """
    User Story 8. Add a Debt: As a user, I need to add a debt so that I can track what I owe.
    """
    #Done: add_debt method
    def add_debt(self, name, total_amount, paid):
        new_debt = Debt(name, total_amount, paid)
        self.__debts.append(new_debt)

    """
    This will be used in a later function to retrieve a desired debt.
    """
    #Done: get_debt_choices
    def get_debt_choices(self):
        choices = []
        for index, debt in enumerate(self.__debts, start=1):
            name = debt.get_name()
            total_amount = debt.get_total_amount()
            amount_paid = debt.get_amount_paid()
            formatted = f"{name}: Paid ${amount_paid:.2f} / {total_amount:.2f}"
            choices.append((index, formatted))
        return choices

    """
    User Story 11. Add a Sinking Fund: As a user, I need to add a sinking fund so that I can save toward specific goals.
    """
    #Done: add_sinking_fund method
    def add_sinking_fund(self, name, goal_amount, balance = 0):
        new_sinking_fund = Sinking_Fund(name, goal_amount, balance)
        self.__sinking_funds.append(new_sinking_fund)


    """
    This will be used in a later function to retrieve a desired sinking fund.
    """
    #Done: get_fund_choices method
    def get_fund_choices(self):
        choices = []
        for index, fund in enumerate(self.__sinking_funds, start=1):
            name = fund.get_name()
            goal_amount = fund.get_goal_amount()
            current_amount = fund.get_current_amount()
            formatted = f"{name}: Saved ${current_amount:.2f} / {goal_amount:.2f}"
            choices.append((index, formatted))
        return choices

    #Done: getters
    def get_monthly_income(self):
        return self.__monthly_income

    def get_categories(self):
        return self.__categories

    def get_transactions(self):
        return self.__transactions

    def get_sinking_funds(self):
        return self.__sinking_funds

    def get_debts(self):
        return self.__debts

    #Done: setters
    def set_monthly_income(self, monthly_income):
        if not isinstance(monthly_income, float):
            raise ValueError("Monthly income must be a monetary value!")
        if monthly_income < 0:
            raise ValueError("Monthly income cannot be negative!")
        self.__monthly_income = monthly_income

    def set_categories(self, categories):
        if not isinstance(categories, list):
            raise ValueError("Categories must be a list!")
        self.__categories = categories

    def set_transactions(self, transactions):
        if not isinstance(transactions, list):
            raise ValueError("Transactions must be a list!")
        self.__transactions = transactions

    def set_sinking_fund(self, sinking_funds):
        if not isinstance(sinking_funds, list):
            raise ValueError("Sinking funds must be a list!")
        self.__sinking_funds = sinking_funds

    def set_debts(self, debts):
        if not isinstance(debts, list):
            raise ValueError("Debts must be a list!")
        self.__debts = debts

    """
    This will be a helper function for deleting and editing a transaction
    """
    #Done: get_transaction_by_index method
    def get_transaction_by_index(self, index):
        if index < 1 or index >= len(self.__transactions):
            raise ValueError("Transaction index out of range!")
        else:
            return self.__transactions[index - 1]

    """
    User Story 16. Delete a Transaction: As a user, I need to delete a transaction so that I can remove mistakes.
    """
    #Done: delete_transaction_by_index method
    def delete_transaction_by_index(self, index):
        if index < 1 or index > len(self.__transactions):
            raise ValueError("Transaction index out of range!")
        del self.__transactions[index - 1]

    """
    This will be a helper function for deleting and editing a debt
    """
    #Done: get_debt_by_index method
    def get_debt_by_index(self, index):
        if index < 1 or index >= len(self.__debts):
            raise ValueError("Debt index out of range!")
        else:
            return self.__debts[index - 1]

    """
    User Story 17. Delete a Debt: As a user, I need to delete a debt so that I can remove a fully paid or incorrect one.
    """
    #Done: delete_debt_by_index method
    def delete_debt_by_index(self, index):
        if index < 1 or index > len(self.__debts):
            raise ValueError("Debt index out of range!")
        del self.__debts[index - 1]

    """
    This will be a helper function for deleting and editing a sinking fund
    """
    #Done: get_sinking_fund_by_index method
    def get_sinking_fund_by_index(self, index):
        if index < 1 or index >= len(self.__sinking_funds):
            raise ValueError("Sinking Fund index out of range!")
        else:
            return self.__sinking_funds[index - 1]

    """
    User Story 18. Delete a Sinking Fund: As a user, I need to delete a sinking fund so that I can remove old or irrelevant ones.
    """
    #Done: delete_sinking_fund_by_index method
    def delete_sinking_fund_by_index(self, index):
        if index < 1 or index > len(self.__sinking_funds):
            raise ValueError("Sinking Fund index out of range!")
        else:
            del self.__sinking_funds[index - 1]

    """
    This will be a helper function for deleting and editing a category
    """
    #Done: get_summary_by_category method
    def get_summary_by_category(self):
        summary = {}
        for category in self.__categories:
            spent = category.get_spent_amount(self.__transactions)
            summary[category.get_name()] = spent
        return summary


    """
    User Story 5. View Spending by Category: As a user, I need to view spending by category so that I can see where my money goes.
    """
    #Done: get_category_summary method
    def get_category_summary(self, name):
        for category in self.__categories:
            if category.get_name() == name:
                total = category.get_spent_amount(self.__transactions)
                limit = category.get_budget_limit()
                category_transactions = []
                for transaction in self.__transactions:
                    if transaction.get_category_name() == name:
                        category_transactions.append({
                            "amount": transaction.get_amount(),
                            "description": transaction.get_description(),
                            "date": transaction.get_date()
                        })
                spending_info = {
                    "category": name,
                    "total": total,
                    "limit": limit,
                    "transactions": category_transactions
                }
                return spending_info
        return None
