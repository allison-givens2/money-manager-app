"""
=== Sinking Fund Methods ===
1. Constructor(str, float, float)
2. add_contribution
3. get_progress
4. get_percent_saved
5. to_dict
6. from_dict
getters and setters
"""

# TODO: Create a Sinking_Fund class with the attributes name, goal_amount, and current_amount. All attributes should be 
#       declared as private. The current amount should be automatically set to $0.
#SinkingFund class
class SinkingFund:
    def __init__(self, name, goal_amount):
        self.__name = name
        self.__goal_amount = goal_amount
        self.__current_amount = 0

    # TODO: Write getters and setters for all attributes (3 getter and 3 setters)
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

    """
    User Story 12.	Track Fund Contribution: As a user, I need to track a contribution to my sinking fund so that I can grow the fund.
    """
    # TODO: Create an add_contribution method which accepts an amount of money the user is adding to the total saved
    #function that adds a contribution to the current amount based on user story 12
    def add_contribution(self, contribution):
        self.__current_amount += contribution


    """
    Used in get_percent_saved()
    """
    # TODO: Create a get_progress method to help the get_percent_saved method
    #helper function that gets the current progress toward a goal for get_percent_saved
    def get_progress(self):
        return self.__current_amount/self.__goal_amount


    """
    User Story 19.	View Percent Paid: As a user, I need to see the percent saved of my sinking fund so that I know how close I am to my goal.
    """
    # TODO: Create a get_percent_saved method to calculate what percent of the goal has been saved
    #function that shows the percent saved toward a goal
    def get_percent_saved(self):
        return self.get_progress() * 100

    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a to_dict method that will turn an object into a dictionary using the attribute names and values as key-value pairs.
    def to_dict(self):
        return {
            "name": self.__name,
            "goal_amount": self.__goal_amount,
            "current_amount": self.__current_amount
        }

    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a from_dict method that will use a dictionary parameter to create and return a Sinking Fund object.
    @classmethod
    def from_dict(cls, data):
        obj = cls(
            name=data.get("name"),
            goal_amount=data.get("goal_amount")
        )
        obj.set_current_amount(data.get("current_amount", 0))
        return obj