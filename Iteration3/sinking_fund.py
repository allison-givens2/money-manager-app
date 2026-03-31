#Done: sinking_fund
"""
=== Sinking Fund Methods ===
1. Constructor(str, float, float)
2. add_contribution
3. get_progress
4. get_percent_saved
getters and setters
"""

#Done: Sinking_fund class
class Sinking_Fund:
    def __init__(self, name, goal_amount, current_amount):
        self.__name = name
        self.__goal_amount = goal_amount
        self.__current_amount = current_amount

    #Done: getters
    def get_name(self):
        return self.__name

    def get_goal_amount(self):
        return self.__goal_amount

    def get_current_amount(self):
        return self.__current_amount

    #Done: setters
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string!")
        self.__name = name

    def set_goal_amount(self, goal_amount):
        if not isinstance(goal_amount, float):
            raise ValueError("Goal amount must be a monetary value!")
        if goal_amount < 0:
            raise ValueError("Goal amount must be positive!")
        self.__goal_amount = goal_amount

    def set_current_amount(self, current_amount):
        if not isinstance(current_amount, float):
            raise ValueError("Current amount must be a monetary value!")
        self.__current_amount = current_amount

    """
    User Story 12.	Track Fund Contribution: As a user, I need to track a contribution to my sinking fund so that I can grow the fund.
    """
    #Done: add_contribution method
    def add_contribution(self, contribution):
        if not isinstance(contribution, float):
            raise ValueError("Contribution must be a monetary value!")
        self.__current_amount += contribution

    """
    Used in get_percent_saved()
    """
    #Done: get_progress method
    def get_progress(self):
        #calculate progress towards goal
        return self.__current_amount / self.__goal_amount

    """
    User Story 19.	View Percent Paid: As a user, I need to see the percent saved of my sinking fund so that I know how close I am to my goal.
    """
    #Done: get_percent_saved method
    def get_percent_saved(self):
        #turn progress into a percentage
        return self.get_progress() * 100
    