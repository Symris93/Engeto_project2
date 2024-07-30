"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lukáš Fúzik
email: fuzik@atlas.cz
discord: symris93
"""

def game(placement, game_progress):
    if placement + "X" in game_progress:
        return " X "
    elif placement + "O" in game_progress:
        return " O "
    else:
        return "   "
        
        

def current_player(current_turn):
    if current_turn % 2 == 0:
        return "X"
    else:
        return "O"
current_turn = 1

game_progress = set()
taken_spots = []
winning_conditions = [
    {"1X","2X","3X"},{"1O","2O","3O"},
    {"4X","5X","6X"},{"4O","5O","6O"},
    {"7X","8X","9X"},{"7O","8O","9O"},
    {"1X","4X","7X"},{"1O","4O","7O"},
    {"2X","5X","8X"},{"2O","5O","8O"},
    {"3X","6X","9X"},{"3O","6O","9O"},
    {"1X","5X","9X"},{"1O","5O","9O"},
    {"3X","5X","7X"},{"3O","5O","7O"}
]


print("""Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================""")
input("Press \"Enter\" to start the game!")
while True:
    print(f"""--------------------------------------------
+---+---+---+
|{game("1",game_progress)}|{game("2",game_progress)}|{game("3",game_progress)}|
+---+---+---+
|{game("4",game_progress)}|{game("5",game_progress)}|{game("6",game_progress)}|
+---+---+---+
|{game("7",game_progress)}|{game("8",game_progress)}|{game("9",game_progress)}|
+---+---+---+
============================================""")
    #Win
    for win in winning_conditions:
        if win.issubset(game_progress):
            print(f"Player {current_player(current_turn-1)} wins. Congratulations!")
            exit()

    #Draw
    if len(taken_spots) == 9:
        print("Looks like a draw! Better luck next time!")
        exit()

    move = input(f"Player {current_player(current_turn)} | Please enter your move number: ")
    try:
        int(move)
    except ValueError:
        print("Please enter a number between 1-9!")
        continue
    else:
        if not 0 < int(move) < 10:
            print("You entered a number outside of the game board! Try 1-9")
        else:
            if move in taken_spots:
                print("This spot is already taken!")
            else:
                game_progress.add(move + current_player(current_turn))
                taken_spots.append(move)
                current_turn += 1