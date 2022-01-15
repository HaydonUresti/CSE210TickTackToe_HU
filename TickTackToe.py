import random

def board(spaces): 
    """ prints the game board and includes the elements of the list containing each space's contents
    Paramenters: 
        spaces: takes a list that holds the value of the current space
    """
    print(f" \n{spaces[0]}|{spaces[1]}|{spaces[2]} \n-----\n{spaces[3]}|{spaces[4]}|{spaces[5]} \n-----\n{spaces[6]}|{spaces[7]}|{spaces[8]}\n")


def make_choice(spaces, player, bot = False):
    """A function that takes and tests user input and adds it to the board by appending the list containing each space's contents
    Parameters
        spaces: takes a list that holds the value of the current space
        player: the current value to be placed on the board (X/O)
        """
    if bot == False:
        while True:
            
            choice = input("Enter the number of the space you want to mark (1-9): ")
            if choice == 'q':
                exit_message()
            
            # tests input for board availability
            if choice not in spaces:
                print("\nThat is not an available space. Please enter an available space\n")
            else:
                break
    
    #searches for the user's or bot's chosen placement and inserts marker
    if bot == False:
        for i in range(len(spaces)):
            if spaces[i] == choice:
                spaces[i] = player
    else:
        for i in range(len(spaces)):
            if spaces[i] == bot:
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
        quit = input("\nAre you sure you want to quit? Please enter 'y' or 'n': ")
        if quit == 'y':
            exit()
        elif quit == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def play_again():
    """Gives user the option to play again
    """
    while True:
        play_again = input("\nWould you like to play again? (y/n): \n")
        if play_again == 'y':
            main()
        elif play_again == 'n':
            exit()
        else:
            print("Please enter 'y' or 'no'")

def bot(spaces):
    """Returns a random number as the bot's move
    Parameters
        spaces: takes a list that holds the value of the current space
    Returns
        bot_choice: the random number to be used as the bot's choice
        """
    while True:
        bot_choice = random.choice(spaces)
        if bot_choice.isnumeric() == False:
            continue
        else:
            break
    return bot_choice

def main(): 
    space_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    turn = 1
    
    # Pre-game text
    print("\nWelcome to Tick-Tack-Toe!")
    
    answer = input("Please press ENTER to continue or type 'q' at any time to quit: ")
    if answer == 'q':
        exit_message()
    use_bot = input("\nIf you would like to play gainst a bot enter 'bot' else press ENTER: ").casefold()
    if use_bot == 'q':
        exit_message()
    elif use_bot == 'bot':
        use_bot = True
    else:
        use_bot = False
   
    # Main game loop
    while True:

        #gets current user
        if turn % 2 == 0:
            player = 'O'
        else: 
            player = "X"

        board(space_list)

        #determines if current input is player or bot 
        if player == 'O' and use_bot == True:
            bot_choice = bot(space_list)
            make_choice(space_list, player, bot(space_list))
            player = 'X'
        else:
            make_choice(space_list, player)
        
        #checking for a winner
        if test_horizontal(space_list) or test_vertical(space_list) or test_diagonal(space_list):
            print(f"\n{player} Wins!!")
            play_again()


        turn += 1

        #checks for a draw
        if turn == 10:
            print("DRAW, GAME OVER...")
            play_again()
            
           
if __name__ == "__main__":
    main()