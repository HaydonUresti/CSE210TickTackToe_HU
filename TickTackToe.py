



def board(spaces): 
    """ prints the game board and includes the elements of the list containing each space's contents
    Paramenters: 
        spaces: takes a list that holds the value of the current space
    """
    print(f" \n{spaces[0]}|{spaces[1]}|{spaces[2]} \n-----\n{spaces[3]}|{spaces[4]}|{spaces[5]} \n-----\n{spaces[6]}|{spaces[7]}|{spaces[8]}\n")


def make_choice(spaces, player):
    """A function that takes user input and adds it to the board by appending the list containing each space's contents
    Parameters:
        spaces: takes a list that holds the value of the current space
        player: the current value to be placed on the board (X/O)
        """
    choice = input("Enter the number of the space you want to mark (1-9): ")

    for i in range(len(spaces)):
        if spaces[i] == choice:
            spaces[i] = player
    



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

        turn += 1



if __name__ == "__main__":
    main()