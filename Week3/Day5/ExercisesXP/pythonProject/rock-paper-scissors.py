from game import RPS_Game
def get_user_menu_choice():
    menu_choice = input("Menu:\n 'g': Play a new Game\n 'x' Show scores and exit\n:")
    if menu_choice == "g" or "x":
        return menu_choice
    else:
        print("You made an invalid choice")
        menu_choice = input("Please select only 'g' to start a new game of 'x' to show scores and exit:")
def play(game):
    user = game.get_user_item()
    comp = game.get_computer_item()
    result = game.get_game_result(user, comp)
    print(f"You selected {user}. The computer selected {comp}. The outcome is a {result}.")
    return result
def print_results(results):
    print(f"Game Result:\n You won {results['win']} times \n You lost {results['loss']} times \n You drew {results['draw']} times \n")
    print("Thank you for playing!")
def main():
    scoreboard = {'win': 0, 'loss': 0, 'draw': 0}
    user_menu_choice = get_user_menu_choice()
    i = 0
    while user_menu_choice != "x":
        current_game = RPS_Game(i)
        outcome = play(current_game)
        scoreboard[outcome] += 1
        i += 1
        user_menu_choice = get_user_menu_choice()
    else:
        print_results(scoreboard)

main()



