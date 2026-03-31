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
20. to_dict
21. save_to_file
22. from_dict
23. load_from_file
"""

# TODO: import the other classes
#importing other classes
from transaction import Transaction
from sinking_fund import SinkingFund
from debt import Debt
from category import Category
import json

# TODO: Create a Budget class with the attributes monthly_income, categories, transactions, sinking_funds, and debts.
#       All attributes should be declared as private. The monthly_income should be set to 0 and the others should be empty lists.
#Budget class
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
    # TODO: Create an add_transaction method. It will take in the information to make a transaction object then add
    #       it to the list of transactions managed by the budget
    #function to create a transaction and add it to a list based on user story 2
    def add_transaction(self, amount, category, description, date):
        new_transaction = Transaction(amount, category, description, date)
        self.__transactions.append(new_transaction)


    """
    User Story 13.	View Total Spent: As a user, I need to see my total spent in a month so that I can track my overall spending.
    """
    # TODO: Create a get_total_spent method. This method will find the total spend from all transactions.
    #function to find total spend on all transactions based on user story 13
    def get_total_spent(self):
        total = 0
        for t in self.__transactions:
            total += t.get_amount()
        return total

    """
    User Story As a user, I need to view all my transactions so that I can review past activity.
    """
    # TODO: Create a get_transaction_choices method. It will return a list of tuples with the number of the transaction 
    #       and the formatted transaction data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuples should be formatted as such:
    #       (number of transaction, "date - description ($amount) in category")
    #       The amount should print two decimal places.
    def get_transaction_choices(self):
        choices = []
        for index, t in enumerate(self.__transactions, start=1):
            string = f"{t.get_date()} - {t.get_description()} (${t.get_amount():.2f}) in {t.get_category_name()}"
            choices.append((index, string))
        return choices

    """"
    User Story 14.	See Remaining Budget: As a user, I need to see my remaining budget so that I can avoid overspending.
    """
    # TODO: Create a get_remaining_budget method. This will find the difference between the monthly income and the amount already spent.
    #function to find the amount left to spend for the month based on user story 14
    def get_remaining_budget(self):
        return self.__monthly_income - self.get_total_spent()

    """
    User Story 4. Add a Category: As a user, I need to add a category so that I can organize my transactions.
    """
    # TODO: Create an add_category method that will take in all the data to create a category object then add it 
    #       to the list of categories managed by the budget.
    #function to add a category based on user story 4
    def add_category(self, category_name, budget):
        new_category = Category(category_name, budget)
        self.__categories.append(new_category)

    """
    This will be used in a later function to retrieve a desired category.
    """
    # TODO: Create a get_category by name method. This will retrieve the category object from the list of categories by 
    #       searching for the entry with the same name as the string given to the function.
    #function to search for a category
    def get_category_by_name(self, category_name):
        for c in self.__categories:
            if c.get_name() == category_name:
                return c
        return "Category not found"

    """
    User Story 8. Add a Debt: As a user, I need to add a debt so that I can track what I owe.
    """
    # TODO: Create an add_debt method that will take in all the data to create a debt object then add it to the list of debts
    #       managed by the budget.
    #function to add a debt based on user story 8
    def add_debt(self, name, total):
        new_debt = Debt(name, total)
        self.__debts.append(new_debt)

    """
    This will be used in a later function to retrieve a desired debt.
    """
    # TODO: Create a get_debt_choices method. This method will return a list of tuples with the number of the debt
    #       and the formatted debt data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuple should be formatted as such: 
    #       (number of debt, "name: Paid $paid / $total")
    #       The paid and total should print two decimal places.
    #function to return a list of debts
    def get_debt_choices(self):
        choices = []
        for index, d in enumerate(self.__debts, start=1):
            string = f"{d.get_name()}: Paid ${d.get_amount_paid():.2f} / ${d.get_total_amount():.2f}"
            choices.append((index, string))
        return choices

    """
    User Story 11. Add a Sinking Fund: As a user, I need to add a sinking fund so that I can save toward specific goals.
    """
    # TODO: Create an add_sinking_fund method that will take in all the data to create a sinking fund object then add it to 
    #       the list of sinking funds managed by the budget.
    #function to add a sinking
    def add_sinking_fund(self, name, goal, current):
        new_sinking_fund = SinkingFund(name, goal)
        self.__sinking_funds.append(new_sinking_fund)

    """
    This will be used in a later function to retrieve a desired sinking fund.
    """
    # TODO: Create a get_fund_choices method. This method will return a list of tuples with the number of the sinking fund
    #       and the formatted sinking fund data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuple should be formatted as such: 
    #       (number of debt, "name: Saved $saved / $goal")
    #       The saved and goal should print two decimal places.
    #function to return a list of sinking funds
    def get_fund_choices(self):
        choices = []
        for index, f in enumerate(self.__sinking_funds, start=1):
            string = f"{f.get_name()}: Saved ${f.get_current_amount():.2f} / ${f.get_goal_amount():.2f}"
            choices.append((index, string))
        return choices

    # TODO: Write getters and setters for each of the attributes (5 getters and 5 setters)
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

    """
    This will be a helper function for deleting and editing a transaction
    """
    # TODO: Create a get_transaction_by_index method that will take in an index number and return the transaction
    #       object stored at that position in the list of transactions.
    #function to get a transaction based on the index
    def get_transaction_by_index(self, index):
        return self.__transactions[index]

    """
    User Story 16. Delete a Transaction: As a user, I need to delete a transaction so that I can remove mistakes.
    """
    # TODO: Create a delete_transaction_by_index method. This method will take in an index number and remove the
    #       transaction object at that position from the list of transactions.
    #function to delete a transaction based on user story 16
    def delete_transaction_by_index(self, index):
        self.__transactions.pop(index)

    """
    This will be a helper function for deleting and editing a debt
    """
    # TODO: Create a get_debt_by_index method that will take in an index number and return the debt
    #       object stored at that position in the list of debts.
    #function to get a debt at a specific index
    def get_debt_by_index(self, index):
        return self.__debts[index]

    """
    User Story 17. Delete a Debt: As a user, I need to delete a debt so that I can remove a fully paid or incorrect one.
    """
    # TODO: Create a delete_debt_by_index method. This method will take in an index number and remove the
    #       debt object at that position from the list of debts.
    #function to delete a debt based on user story 17
    def delete_debt_by_index(self, index):
        self.__debts.pop(index)

    """
    This will be a helper function for deleting and editing a sinking fund
    """
    # TODO: Create a get_sinking_fund_by_index method that will take in an index number and return the sinking fund
    #       object stored at that position in the list of sinking funds.
    #helper function that returns a sinking fund based on an index
    def get_sinking_fund_by_index(self, index):
        return self.__sinking_funds[index]

    """
    User Story 18. Delete a Sinking Fund: As a user, I need to delete a sinking fund so that I can remove old or irrelevant ones.
    """
    # TODO: Create a delete_sinking_fund_by_index method. This method will take in an index number and remove the
    #       sinking fund object at that position from the list of sinking funds.
    def delete_sinking_fund_by_index(self, index):
        self.__sinking_funds.pop(index)

    """
    This will be a helper function for deleting and editing a category
    """
    # TODO: Create a get_summary_by_category method. This method will build a dictionary containing the total amount
    #       spent for each category. It should loop through every category in the list and calculate its total by calling
    #       the category’s get_spent_amount method. The resulting dictionary should use the category name as the key and
    #       the total amount spent as the value.
    #helper function to that makes a summary for a category
    summary = {}
    def get_summary_by_category(self):
        summary = {}
        for c in self.__categories:
            total = c.get_spent_amount(self.__transactions)
            summary[c.get_name()] = total
        return summary


    """
    User Story 5. View Spending by Category: As a user, I need to view spending by category so that I can see where my money goes.
    """
    # TODO: Create a get_category_summary method. This method will take in a category name and return a dictionary
    #       containing all spending information related to that category. It should find all transactions that match
    #       the category name, total their amounts, and include each transaction’s details (amount, description, and date).
    #       The returned dictionary should include:
    #           - "category": the category name
    #           - "total": total amount spent in that category
    #           - "limit": the category’s budget limit
    #           - "transactions": a list of dictionaries containing each transaction’s details
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


    """
    The following four methods implement memory persistence—the idea of data persisting across runs. With these functions the same
    data will be loaded every time the application runs automatically, so you won't have to manually input the data every time 
    you want to test a function of the application. I felt so mean having you implement this so late.
    """
    # TODO: Write a method that will convert a Budget object to a dictionary. It should use the attribute names and values
    #       as the key-value pairs in the dictionary. Each attribute that is composed of other classes should also be converted
    #       to dictionary objects using their respective to_dict methods
    def to_dict(self):
        return {
            "monthly_income": self.__monthly_income,
            "categories": [c.to_dict() for c in self.__categories],
            "transactions": [t.to_dict() for t in self.__transactions],
            "sinking_funds": [f.to_dict() for f in self.__sinking_funds],
            "debts": [d.to_dict() for d in self.__debts]
        }

    # TODO: Add memory persistence by saving to a file. Open the specified filename from the parameter.
    #       Use json.dump to write the budget to the file as a dictionary.
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    # TODO: Write a method to convert a dictionary object into a budget object. This will be a static method which means it does
    #       not need the self attribute. Put @staticmethod above the function definition to show this. This method should take in
    #       a dictionary as a parameter and populate a Budget object with the data from the dictionary. The dictionary keys 
    #       should be the same as the attributes for Budget. This should load the values for each attribute in a budget from the 
    #       corresponding key in the dictionary. The attributes that should be composed of other objects should call that object's
    #       respective from_dict method.
    @staticmethod
    def from_dict(data):
        b = Budget()
        b.set_monthly_income(data.get("monthly_income", 0))

        # Load categories
        b.set_categories([Category.from_dict(c) for c in data.get("categories", [])])

        # Load transactions
        b.set_transactions([Transaction.from_dict(t) for t in data.get("transactions", [])])

        # Load sinking funds
        b.set_sinking_funds([SinkingFund.from_dict(f) for f in data.get("sinking_funds", [])])

        # Load debts
        b.set_debts([Debt.from_dict(d) for d in data.get("debts", [])])

        return b

    # TODO: Write a load_from_file method that takes a file name passed in the parameters. It should then use json.load to read
    #       the contents of the file. The data read from the file should then be converted to objects from the dictionary contents.
    #       This will also be a static function.
    @staticmethod
    def load_from_file(filename):
        import json
        with open(filename, "r") as f:
            data = json.load(f)
        return Budget.from_dict(data)

    # TODO: Write a rollever method that is a static method. It will be passed a previous Budget object. It will take the following
    #       values from the previous budget and set the corresponding attributes on the current budget:
    #           - monthly_income
    #           - categories and all their attributes
    #           - sinking funds keeping their goal amount and progress
    #           - debts keeping their owed amount and progress
    #       The function will then return the newly created budget with values rolled over from the prvious month.
    @staticmethod
    def rollover(old):
        new = Budget()

        # Copy monthly income
        new.set_monthly_income(old.get_monthly_income())

        # Copy categories (same limits, reset spending)
        new_categories = []
        for c in old.get_categories():
            new_cat = Category(c.get_name(), c.get_budget_limit())
            new_categories.append(new_cat)
        new.set_categories(new_categories)

        # Copy sinking funds (keep goal + progress)
        new_funds = []
        for f in old.get_sinking_funds():
            nf = SinkingFund(f.get_name(), f.get_goal_amount())
            nf.set_current_amount(f.get_current_amount())
            new_funds.append(nf)
        new.set_sinking_funds(new_funds)

        # Copy debts (keep owed amount + paid)
        new_debts = []
        for d in old.get_debts():
            nd = Debt(d.get_name(), d.get_total_amount())
            nd.set_amount_paid(d.get_amount_paid())
            new_debts.append(nd)
        new.set_debts(new_debts)

        return new

