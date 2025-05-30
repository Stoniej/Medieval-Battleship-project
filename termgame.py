import random
import os

# Constants
BOARD_SIZE = 10
UNITS = {
    "Platoon": 2,
    "Archers": 3,
    "Cavalry": 3,
    "Catapult": 4,
    "Castle": 5
}

# Display Title and Instructions
def display_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    title = r"""

 ███▄ ▄███▓▓█████ ▓█████▄  ██▓▓█████ ██▒   █▓ ▄▄▄       ██▓        ▄▄▄▄    ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ██▓    ▓█████     ██▓     ▒█████   ██▀███  ▓█████▄   ██████  ▐██▌ 
▓██▒▀█▀ ██▒▓█   ▀ ▒██▀ ██▌▓██▒▓█   ▀▓██░   █▒▒████▄    ▓██▒       ▓█████▄ ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒    ▓█   ▀    ▓██▒    ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▒██    ▒  ▐██▌ 
▓██    ▓██░▒███   ░██   █▌▒██▒▒███   ▓██  █▒░▒██  ▀█▄  ▒██░       ▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░    ▒███      ▒██░    ▒██░  ██▒▓██ ░▄█ ▒░██   █▌░ ▓██▄    ▐██▌ 
▒██    ▒██ ▒▓█  ▄ ░▓█▄   ▌░██░▒▓█  ▄  ▒██ █░░░██▄▄▄▄██ ▒██░       ▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ▒██░    ▒▓█  ▄    ▒██░    ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌  ▒   ██▒ ▓██▒ 
▒██▒   ░██▒░▒████▒░▒████▓ ░██░░▒████▒  ▒▀█░   ▓█   ▓██▒░██████▒   ░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░ ░██████▒░▒████▒   ░██████▒░ ████▓▒░░██▓ ▒██▒░▒████▓ ▒██████▒▒ ▒▄▄  
░ ▒░   ░  ░░░ ▒░ ░ ▒▒▓  ▒ ░▓  ░░ ▒░ ░  ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░   ░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░     ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░ ░▀▀▒ 
░  ░      ░ ░ ░  ░ ░ ▒  ▒  ▒ ░ ░ ░  ░  ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░   ▒░▒   ░   ▒   ▒▒ ░   ░        ░    ░ ░ ▒  ░ ░ ░  ░   ░ ░ ▒  ░  ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░ ░  ░ 
░      ░      ░    ░ ░  ░  ▒ ░   ░       ░░    ░   ▒     ░ ░       ░    ░   ░   ▒    ░        ░        ░ ░      ░        ░ ░   ░ ░ ░ ▒    ░░   ░  ░ ░  ░ ░  ░  ░      ░ 
       ░      ░  ░   ░     ░     ░  ░     ░        ░  ░    ░  ░    ░            ░  ░                     ░  ░   ░  ░       ░  ░    ░ ░     ░        ░          ░   ░    
                   ░                     ░                              ░                                                                         ░                     

    """
    print(title)
    print("""
Welcome to Medieval Battle Lords!
    Created by Ryan Bandy
Instructions:
- This is a 10x10 turn-based strategy game.
- You command medieval units: Platoons, Archers, Cavalry, Catapults, and a Castle.
- On your turn, enter coordinates (e.g., 3 5) to attack.
- X = Hit, O = Miss.
- First to destroy all enemy units wins!

    """)

# Create Board
def create_board():
    return [["~" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Print Board
def print_board(board, reveal=False):
    print("   " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        line = f"{i:2} "
        for cell in row:
            if cell in ("X", "O") or reveal:
                line += f"{cell} "
            else:
                line += "~ "
        print(line)

# Place Units
def place_units(board):
    for unit, size in UNITS.items():
        placed = False
        while not placed:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            horizontal = random.choice([True, False])
            if horizontal:
                if col + size > BOARD_SIZE:
                    continue
                if all(board[row][col + i] == "~" for i in range(size)):
                    for i in range(size):
                        board[row][col + i] = unit[0]
                    placed = True
            else:
                if row + size > BOARD_SIZE:
                    continue
                if all(board[row + i][col] == "~" for i in range(size)):
                    for i in range(size):
                        board[row + i][col] = unit[0]
                    placed = True

# Handle Turn
def take_turn(board, tracking_board):
    while True:
        try:
            coords = input("Enter attack coordinates (row col): ").split()
            if len(coords) != 2:
                raise ValueError
            row, col = int(coords[0]), int(coords[1])
            if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                raise IndexError

            if board[row][col] != "~" and board[row][col] not in ("X", "O"):
                print("Hit!")
                tracking_board[row][col] = "X"
                board[row][col] = "X"
            elif board[row][col] == "~":
                print("Miss.")
                tracking_board[row][col] = "O"
                board[row][col] = "O"
            else:
                print("Already attacked there.")
                continue
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 0 and 9.")

# Check Win
def check_win(board):
    for row in board:
        for cell in row:
            if cell not in ("~", "X", "O"):
                return False
    return True

# Main Game Loop
def play_game():
    display_title()
    player_board = create_board()
    computer_board = create_board()
    player_tracking = create_board()

    place_units(computer_board)
    place_units(player_board)

    while True:
        print("\nYour Board:")
        print_board(player_board, reveal=True)
        print("\nEnemy Board:")
        print_board(player_tracking)

        print("\nYour turn:")
        take_turn(computer_board, player_tracking)
        if check_win(computer_board):
            print("\nYou have defeated the enemy forces! Victory!")
            break

        print("\nEnemy's turn:")
        while True:
            enemy_row = random.randint(0, BOARD_SIZE - 1)
            enemy_col = random.randint(0, BOARD_SIZE - 1)
            if player_board[enemy_row][enemy_col] not in ("X", "O"):
                if player_board[enemy_row][enemy_col] == "~":
                    print(f"Enemy attacked ({enemy_row}, {enemy_col}) and missed.")
                    player_board[enemy_row][enemy_col] = "O"
                else:
                    print(f"Enemy attacked ({enemy_row}, {enemy_col}) and hit your unit!")
                    player_board[enemy_row][enemy_col] = "X"
                break

        if check_win(player_board):
            print("\nYour forces have been defeated. Game over.")
            break

# Run the game
if __name__ == "__main__":
    play_game()
