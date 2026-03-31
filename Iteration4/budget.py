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

#importing other classes
from transaction import Transaction
from sinking_fund import SinkingFund
from debt import Debt
from category import Category

#Budget class
class Budget:
    def __init__(self):
        self.__monthly_income = 0
        self.__categories = []
        self.__transactions = []
        self.__sinking_funds = []
        self.__debts = []

    #function to create a transaction and add it to a list based on user story 2
    def add_transaction(self, amount, category, description, date):
        new_transaction = Transaction(amount, category, description, date)
        self.__transactions.append(new_transaction)

    #function to find total spend on all transactions based on user story 13
    def get_total_spent(self):
        total = 0
        for t in self.__transactions:
            total += t.get_amount()
        return total

    #function to return a list of transactions based on user story 3
    def get_transaction_choices(self):
        choices = []
        for index, t in enumerate(self.__transactions, start=1):
            string = f"{t.get_date()} -  {t.get_description()} (${t.get_amount():.2f}) in {t.get_category_name()}"
            choices.append((index, string))
        return choices
    
    #function to find the amount left to spend for the month based on user story 14
    def get_remaining_budget(self):
        return self.__monthly_income - self.get_total_spent()

    #function to add a category based on user story 4
    def add_category(self, category_name, budget):
        new_category = Category(category_name, budget)
        self.__categories.append(new_category)

    #function to search for a category
    def get_category_by_name(self, category_name):
        for c in self.__categories:
            if c.get_name() == category_name:
                return c
        return "Category not found"

    #function to add a debt based on user story 8
    def add_debt(self, name, total):
        new_debt = Debt(name, total)
        self.__debts.append(new_debt)

    #function to return a list of debts
    def get_debt_choices(self):
        choices = []
        for index, d in enumerate(self.__debts, start=1):
            string = f"{d.get_name()}: Paid ${d.get_amount_paid():.2f} / ${d.get_total_amount():.2f}"
            choices.append((index, string))
        return choices

    #function to add a sinking
    def add_sinking_fund(self, name, goal, current):
        new_sinking_fund = SinkingFund(name, goal)
        self.__sinking_funds.append(new_sinking_fund)

    #function to return a list of sinking funds
    def get_fund_choices(self):
        choices = []
        for index, f in enumerate(self.__sinking_funds, start=1):
            string = f"{f.get_name()}: Saved ${f.get_current_amount():.2f} / ${f.get_current_amount():.2f}"
            choices.append((index, string))
        return choices

    #getters and setters
    #function to get monthly income
    def get_monthly_income(self):
        return self.__monthly_income

    #function to set monthly income
    def set_monthly_income(self, monthly_income):
        self.__monthly_income = monthly_income

    #function to get categories
    def get_categories(self):
        return self.__categories

    #function to set categories
    def set_categories(self, categories):
        self.__categories = categories

    #function to get transactions
    def get_transactions(self):
        return self.__transactions

    #function to set transactions
    def set_transactions(self, transactions):
        self.__transactions = transactions

    #function to get sinking funds
    def get_sinking_funds(self):
        return self.__sinking_funds

    #function to set sinking funds
    def set_sinking_funds(self, sinking_funds):
        self.__sinking_funds = sinking_funds

    #function to get debts
    def get_debts(self):
        return self.__debts

    #function to set debts
    def set_debts(self, debts):
        self.__debts = debts

    #function to get a transaction based on the index
    def get_transaction_by_index(self, index):
        return self.__transactions[index]

    #function to delete a transaction based on user story 16
    def delete_transaction_by_index(self, index):
        self.__transactions.pop(index)

    #function to get a debt at a specific index
    def get_debt_by_index(self, index):
        return self.__debts[index]

    #function to delete a debt based on user story 17
    def delete_debt_by_index(self, index):
        self.__debts.pop(index)

    #helper function that returns a sinking fund based on an index
    def get_sinking_fund_by_index(self, index):
        return self.__sinking_funds[index]

    def delete_sinking_fund_by_index(self, index):
        self.__sinking_funds.pop(index)

    #helper function to that makes a summary for a category
    summary = {}
    def get_summary_by_category(self):
        summary = {}
        for c in self.__categories:
            total = c.get_spent_amount(self.__transactions)
            summary[c.get_name()] = total
        return summary

    #function that prints spending for a category based on user story 5
    def get_category_summary(self, category_name):
        summary = {}
        transactions = []
        for t in self.__transactions:
            if t.get_category_name() == category_name:
                transactions.append(t)
        for c in self.__categories:
            if c.get_name() == category_name:
                summary = {"category": category_name,
                           "total": c.get_spent_amount(transactions),
                           "limit": c.get_budget_limit(),
                           "transactions": transactions}
            return summary
        return "Category not found"
