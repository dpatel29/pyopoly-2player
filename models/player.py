import random
from constants import STARTING_FUNDS, PASS_GO_AMOUNT


class Player:
    """
    A player class with player attributes and methods
    """

    def __init__(self, name, symbol, starting_funds):
        """
        A method to instantiate a player.

        :param name: the name of the player
        :param symbol: a single character
        """
        self.name = name
        self.symbol = symbol
        self.funds = starting_funds
        self.current_position = ''
        self.properties = []
        self.insolvent = False

    def __str__(self):
        return '{self.name}, {self.symbol}, {self.funds}, {self.current_position}'.format(self=self)

    def rol_dice_twice(self):
        """
        A method to role a dice twice and set the result for the player
        """
        self.dice_result = random.randint(1, 6) + random.randint(1, 6)

    def move_player(self, position):
        """
        A method to set current player position
        """
        self.current_position = position

    def give_pass_go_amount(self, pass_go_amount):
        self.funds += pass_go_amount
