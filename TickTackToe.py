
def board(spaces): 
    """ prints the game board and includes the elements of the list containing each space's contents
    Paramenters: 
        spaces: takes a list that holds the value of the current space
    """
    print(f" \n{spaces[0]}|{spaces[1]}|{spaces[2]} \n-----\n{spaces[3]}|{spaces[4]}|{spaces[5]} \n-----\n{spaces[6]}|{spaces[7]}|{spaces[8]}\n")


def make_choice(spaces, player):
    """A function that takes user input and adds it to the board by appending the list containing each space's contents
    Parameters
        spaces: takes a list that holds the value of the current space
        player: the current value to be placed on the board (X/O)
        """
    choice = input("Enter the number of the space you want to mark (1-9): ")

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


def main(): 
    space_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    turn = 1
    
    # Main game loop
    while True:

        if turn % 2 == 0:
            player = 'O'
        else: 
            player = "X"

        board(space_list)

        make_choice(space_list, player)

        if test_horizontal(space_list) or test_vertical(space_list) or test_diagonal(space_list):
            print(f"\n{player} Wins!!")
            break


        turn += 1
        if turn == 10:
            print("DRAW, GAME OVER...")



if __name__ == "__main__":
    main()



    # Add a computer player, probably just rng
    
    # handle non valid input