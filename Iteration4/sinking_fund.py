"""
=== Sinking Fund Methods ===
1. Constructor(str, float, float)
2. add_contribution
3. get_progress
4. get_percent_saved
getters and setters
"""

#SinkingFund class
class SinkingFund:
    def __init__(self, name, goal_amount):
        self.__name = name
        self.__goal_amount = goal_amount
        self.__current_amount = 0

    #getters and setters
    #function to get name
    def get_name(self):
        return self.__name

    #function to set name
    def set_name(self, name):
        self.__name = name

    #function to get goal amount
    def get_goal_amount(self):
        return self.__goal_amount

    #function to set goal amount
    def set_goal_amount(self, goal_amount):
        self.__goal_amount = goal_amount

    #function to get current amount
    def get_current_amount(self):
        return self.__current_amount

    #function to set current amount
    def set_current_amount(self, current_amount):
        self.__current_amount = current_amount

    #function that adds a contribution to the current amount based on user story 12
    def add_contribution(self, contribution):
        self.__current_amount += contribution

    #helper function that gets the current progress toward a goal for get_percent_saved
    def get_progress(self):
        return self.__current_amount/self.__goal_amount

    #function that shows the percent saved toward a goal
    def get_percent_saved(self):
        return self.get_progress() * 100
    