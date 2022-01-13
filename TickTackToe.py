



def board(spaces):
    print(f"{spaces[0]}|{spaces[1]}|{spaces[2]} \n-----\n{spaces[3]}|{spaces[4]}|{spaces[5]} \n-----\n{spaces[6]}|{spaces[7]}|{spaces[8]} ")



def main(): 
    space_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9" ]

    while True:
        board(space_list)

if __name__ == "__main__":
    main()