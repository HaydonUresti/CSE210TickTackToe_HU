def board(spaces): 
    """ prints the game board and includes the elements of the list containing each space's contents
    Paramenters: 
        spaces: takes a list that holds the value of the current space
    """
    print(f" \n{spaces[0]}|{spaces[1]}|{spaces[2]} \n-----\n{spaces[3]}|{spaces[4]}|{spaces[5]} \n-----\n{spaces[6]}|{spaces[7]}|{spaces[8]}\n")


def make_choice(spaces, player):
    """A function that takes and tests user input and adds it to the board by appending the list containing each space's contents
    Parameters
        spaces: takes a list that holds the value of the current space
        player: the current value to be placed on the board (X/O)
        """
    while True:

        choice = input("Enter the number of the space you want to mark (1-9): ")
        if choice == 'q':
            exit_message()
        
        # tests input for board availability
        if choice not in spaces:
            print("\nThat is not an available space. Please enter an available space\n")
        else:
            break
#searches for the user's chosen placement and inserts marker
    for i in range(len(spaces)):
        if spaces[i] == choice:
            spaces[i] = player

def test_horizontal(spaces):
    """A function that checks for a winner on the x axis
    Parameters
        spaces: takes a list that holds the value of the current space
        """
    if spaces[0] == spaces[1] == spaces[2]:
        return True
    elif spaces[3] == spaces[4] == spaces[5]:
        return True
    elif spaces[6] == spaces[7] == spaces[8]:
        return True
    else:
        return False

def test_vertical(spaces):
    """A function that checks for a winner on the y axis
    Parameters
        spaces: takes a list that holds the value of the current space
        """
    if spaces[0] == spaces[3] == spaces[6]:
        return True
    elif spaces[1] == spaces[4] == spaces[7]:
        return True
    elif spaces[2] == spaces[5] == spaces[8]:
        return True
    else:
        return False

def test_diagonal(spaces):
    """A function that checks for a winner on the diagonals
    Parameters
        spaces: takes a list that holds the value of the current space
        """
    if spaces[0] == spaces[4] == spaces[8]:
        return True
    elif spaces[6] == spaces[4] == spaces[2]:
        return True
    else:
        return False

def exit_message():
    """A function that gives the user the option to quit the game"""
    while True:
        quit = input("Are you sure you want to quit? Please enter 'y' or 'n': ")
        if quit == 'y':
            exit()
        elif quit == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
def main(): 
    space_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    turn = 1
    
    print("Welcome to Tick-Tack-Toe!")
    answer = input("Please press enter to continue or type 'q' at any time to quit: ")
    if answer == 'q':
        exit_message()
    # Main game loop
    while True:

        #gets current user
        if turn % 2 == 0:
            player = 'O'
        else: 
            player = "X"

        board(space_list)

        make_choice(space_list, player)
        
        #checking for a winner
        if test_horizontal(space_list) or test_vertical(space_list) or test_diagonal(space_list):
            print(f"\n{player} Wins!!")
            break


        turn += 1

        #checks for a draw
        if turn == 10:
            print("DRAW, GAME OVER...")



if __name__ == "__main__":
    main()



    # Add a computer player, probably just rng
    
    # handle non valid input