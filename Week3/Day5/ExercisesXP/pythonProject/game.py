import random
class RPS_Game:
    def __init__(self, game):
        self.game = game

    def get_user_item(self):
        rps_choices = ["r", "p", "s"]
        user_choice = input("Select (r)ock, (p)aper, or (s)cissors:")
        if user_choice not in rps_choices:
            print("Invalid response")
            user_choice = input("Please make your choice between rock, paper, or scissors by enterring 'r', 'p', or 's': ")
        return user_choice
    def get_computer_item(self):
        rps_choices = ["r", "p", "s"]
        comp_choice = random.choice(rps_choices)
        return comp_choice
    def get_game_result(self, user_item, comp_item):
        if user_item == comp_item:
            return "draw"
        if user_item == "r":
            if comp_item == "p":
                return "loss"
            elif comp_item == "s":
                return "win"
        if user_item == "s":
            if comp_item == "r":
                return "loss"
            elif comp_item == "p":
                return "win"
        if user_item == "p":
            if comp_item == "s":
                return "loss"
            elif comp_item == "r":
                return "win"
