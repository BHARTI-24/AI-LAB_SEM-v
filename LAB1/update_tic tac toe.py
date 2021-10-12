import time

# globals 
game_going = True

winner = None

empty_count = 0


demo_board= ["1","2","3",
             "4","5","6",
             "7","8","9"]
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]



#by default
first = computer = "O"    

second = current_player = "X"

player = first


def display_board():
    print("\n\t" + board[0] + " | " + board[1] + " | " + board[2])
    print("\t" + board[3] + " | " + board[4] + " | " + board[5])
    print("\t" + board[6] + " | " + board[7] + " | " + board[8]+"\n")
    
    
def display_demo_board():
    print("\t" + demo_board[0] + " | " + demo_board[1] + " | " + demo_board[2])
    print("\t" + demo_board[3] + " | " + demo_board[4] + " | " + demo_board[5])
    print("\t" + demo_board[6] + " | " + demo_board[7] + " | " + demo_board[8])
    
    
    
    # funct  to choose who play first , and choose 'x' or 'o' ...
def choose():
    global current_player,computer,first,second,player
    
    you=input("\t\t Choose 'X' or 'O'  :  ")
    
    current_player = you.upper()
    
    
    if current_player == "O":
        computer = "X"
    elif current_player == "X":
        computer = "O"
        
    choice=input("\t\t  Want to play  first>> say 'y' or 'n' :  ")
    if choice == 'y' or choice == 'Y':
        first = current_player
        second = computer
        
    elif choice == 'n' or choice == 'N':
        first = computer
        second = current_player
    player = first  
    
    return


    
def display_instruction():
    
    print("      --------------TIC TAC TOE-------------")
    print("\n\t press 'h' for help , 'q' to quit  'y' to start ")
    cmd=input(":> ")
    if cmd == 'h' or cmd == 'H':
        help_me()
    elif cmd == 'q' or cmd == 'Q':
        print("Closing"),
        sleeping(" *",4)
        print("\tPlay Again!! (@@) ")
        sleeping("-",4)
        quit()
    elif cmd == 'y' or cmd == 'Y':
        start()
        
    return

def start():
    print("\n \t Lets start !! hold back ...")
    sleeping("",3)
    choose()
    return


def help_me():
    print("\n  you have to choose position from 1 to 9")
    sleeping(" \t",2)
    print("  Demo board: ")
    display_demo_board()
    print("")
    sleeping(" ",4)
    conditions()
    start()
    return

def sleeping(x,i):
    y = 0
    while y <= i:
        time.sleep(0.5)
        print(x)
        y = y+1
    return

def conditions():
    print("\n\t conditions:")
    sleeping("",2)
    print("There are four different ways to win at tick-tack-toe:")
    sleeping(" ",1)
    print("1. form a horizontal line")
    sleeping("",1)
    print("2. form a vertical line")
    sleeping("",1)
    print("3. form a diagonal line from the upper-left to the lower-right corner")
    sleeping("",1)
    print("4. form a diagonal line from the lower-left to the upper-right corner")
    sleeping("",2)
    print("\t   ---------------------------------------\n")
    return

def play_game():
    
    display_instruction()
    display_board()
    
    
    while game_going:
          handle_turn(player)
          # for keeping count of the  empty spaces
          
         
          print("the count iis :> " + str(empty_count))
          
          check_if_over()
          flip_player()

    if winner == "X" or winner == "O":
        if winner == computer:
           print("\n\t You lost !!  \n computer won .. \n  symbol: "+ winner)
        elif winner == current_player:
           print("\n\t You Won .. \n your symbol: "+ winner)
        response()
    elif winner== None:
        print("Tie.")
        response()
    
    
    
        #####
def response():
    res=("\n To restart game , press 'r' \n  'q' to quit :")    
    if res == "q" or res == "Q":
        quit()
    elif res == "r" or res == "R":
        play_game()
    else:
        quit()
    return
def handle_turn(player):
    global current_player,empty_count
    if player == current_player:
       player_name = "Your"
    else:
        player_name = "\t\tComputer"
    
    print(player_name + "'s turn." + "[ "+player+" ]")
    
    
    if player == current_player:
        position=input(" to quit 'q' ,else  choose a position from 1-9: ")
        
        valid = False
        while not valid:
        
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "Q"]:
                position=input("Invalid! choose a position from 1-9: ")
                # if q pressed, quit 
            if position == "q" or position == "Q":
                sleeping("",3)
                print("\t\t----Exited----")
                quit()
                
            empty_count += 1    
            position = int(position)-1
            if board[position] == "-":
                valid = True
            else:
                print("Cant contine! go again")
            
            
        board[position]= player
        display_board()
    else:
         
         intelligence()
         #ai_calculate_position()
         display_board()
    

def check_if_over():
    check_winner()
    check_if_tie()


def check_winner():
    global winner
    # check rows
    row_winner = check_rows()
    #check coloumns
    coloumn_winner = check_columns()
    
    #check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


    # to check rows 
def check_rows():
    global game_going
    
    
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    if row_1 or row_2 or row_3:
        game_going = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    
    global game_going
    
    
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    if column_1 or column_2 or column_3:
        game_going = False
    
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
        
    return


def check_diagonals():
    
    global game_going
    
    
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
   
    
    if diagonal_1 or diagonal_2:
        game_going = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    
    
    return


def check_if_tie():
    global game_going
    
    if "-" not in board:
        game_going = False
    return


  
def flip_player():
    #global variable
    global first,second,player
     
    if player == first:
        player = second
    elif player == second:
        player = first
    return





### implementation of ai_calculate_position function to get position automatically by intelligence

def intelligence():
     
    global computer, empty_count
    
    print("yet to implement") 
    
    if  empty_count == 0:
        # default set by me
        board[0]=computer
        
    elif empty_count == 1:
       
            
         
         check_prior_pos1()
         
    # elif empty_count == 2:
       
            
        
    # elif empty_count == 3:
       
            
        
        
    # elif empty_count == 4:
       
            
        
         
    # elif empty_count == 5:
       
            
        
    return
    
    
def check_prior_pos1():
    
    print("in check_prior_pos1 function ")
    
    if board[0]== board[2] == board[6] == board[8] == current_player:
        x = pref_odd()
        board[x] = computer
    
    
    return

def pref_odd():
    if i in range (1,8,2):
        pref_odd_board[i] = 0
       
    pref_odd_board[1] = 1
    pref_odd_board[3] = 3
    pref_odd_board[5] = 5
    pref_odd_board[7] = 7
    
    
    
    retun  value(min(pref_odd_board[1],pref_odd_board[3],pref_odd_board[5],pref_odd_board[7]))
    
def ai_calculate_position():
    global computer
    
    
    sleeping("",2)
         # case when computer got second turn
    if   board[0]==current_player and board[1]==board[2]==board[3]== board[4]==board[5]==board[6]==board[7]==board[8]=="-":
         board[2] = computer
    elif   board[1]==current_player and board[0]==board[2]==board[3]== board[4]==board[5]==board[6]==board[7]==board[8]=="-":
           board[6] = computer
    elif   board[2]==current_player and board[1]==board[0]==board[3]== board[4]==board[5]==board[6]==board[7]==board[8]=="-":
           board[0] = computer
    elif   board[3]==current_player and board[1]==board[2]==board[0]== board[4]==board[5]==board[6]==board[7]==board[8]=="-":
           board[2] = computer
    elif   board[4]==current_player and board[1]==board[2]==board[3]== board[0]==board[5]==board[6]==board[7]==board[8]=="-":
           board[2] = computer
    elif   board[5]==current_player and board[1]==board[2]==board[3]== board[4]==board[0]==board[6]==board[7]==board[8]=="-":
           board[0] = computer
    elif   board[6]==current_player and board[1]==board[2]==board[3]== board[4]==board[5]==board[0]==board[7]==board[8]=="-":
           board[8] = computer
    elif   board[7]==current_player and board[1]==board[2]==board[3]== board[4]==board[5]==board[6]==board[0]==board[8]=="-":
           board[2] = computer
    elif   board[8]==current_player and board[1]==board[2]==board[3]== board[4]==board[5]==board[6]==board[7]==board[0]=="-":
           board[6] = computer
           
    # case when computer got third turn , computer placed first 
    elif   board[0]==current_player and board[1]==board[3]== board[4]==board[5]==board[6]==board[7]==board[8]=="-" and board[2]== computer:
           board[6] = computer
           
    elif   board[2]==current_player and board[1]==board[3]== board[4]==board[5]==board[6]==board[7]==board[8]=="-" and board[0]==computer:
           board[8] = computer
           
    elif   board[6]==current_player and board[0]==board[1]==board[2]==board[3]== board[4]==board[5]==board[7]=="-" and board[8]== computer:
           board[0] = computer
    elif   board[8]==current_player and board[0]==board[1]==board[2]==board[3]== board[4]==board[5]==board[7]=="-" and board[6]==computer:
           board[2] = computer
           
           
           
     # case when computer make first entry 
    elif   board[0]==board[1]==board[2]==board[3]== board[4]==board[5]==board[6]==board[7]==board[8]=="-":
         board[0]=computer
    
    
    # for rows with 2 enteries
        # for row 1
    elif   board[0] == board[1] == current_player and board[2] == "-":
         board[2] = computer
    elif board[0] == board[2] == current_player and board[1] == "-":
         board[1]  = computer
    elif board[1] == board[2] == current_player and board[0] == "-":
         board[0]  = computer
         # for row 2
    elif board[3] == board[4] == current_player and board[5] == "-":
         board[5]  = computer     
    elif board[3] == board[5] == current_player and board[4] == "-":
         board[4]  = computer
    elif board[4] == board[5] == current_player and board[3] == "-":
         board[3]  = computer
         
         #for row 3
    elif board[6] == board[7] == current_player and board[8] == "-":
         board[8]  = computer
    elif board[6] == board[8] == current_player and board[7] == "-":
         board[7]  = computer
    elif board[0] == board[1] == current_player and board[3] == "-":
         board[2]  = computer
         
         # for column 1
    elif board[0] == board[3] == current_player and board[6] == "-":
         board[6]  = computer
    elif board[0] == board[6] == current_player and board[3] == "-":
         board[3]  = computer
    elif board[3] == board[6] == current_player and board[0] == "-":
         board[0]  = computer 
         # for column 2
    elif board[1] == board[4] == current_player and board[7] == "-":
         board[7]  = computer
    elif board[1] == board[7] == current_player and board[4] == "-":
         board[4]  = computer
    elif board[4] == board[7] == current_player and board[1] == "-":
         board[1]  = computer 
         # for column 3
    elif board[2] == board[5] == current_player and board[8] == "-":
         board[8]  = computer
    elif board[2] == board[8] == current_player and board[5] == "-":
         board[5]  = computer
    elif board[5] == board[8] == current_player and board[2] == "-":
         board[2]  = computer    
         
         # for diagonls
         # from left top to right down
    elif board[0]==board[4]== current_player    and board[8]=="-":
        board[8]= computer
    elif board[0]==board[8]== current_player    and board[4]=="-":
        board[4]= computer
    elif board[8]==board[4]== current_player    and board[0]=="-":
        board[0]= computer
        
        
        # from right top to left down
    elif board[2]==board[4]== current_player    and board[6]=="-":
        board[6]= computer
    elif board[6]==board[4]== current_player    and board[2]=="-":
        board[2]= computer
    elif board[2]==board[6]== current_player    and board[4]=="-":
        board[4]= computer
    
    
# case when it check for its win (egoist)---------------------------------------
    
    # checking Rows
    # checking in 1 row
    elif board[0]==board[1]==computer and board[2]=="-":
        board[2]==computer
    elif board[0]==board[2]==computer and board[1]=="-":
        board[1]==computer
    elif board[1]==board[2]==computer and board[0]=="-":
        board[0]==computer
        
      # checking in 2 row  
    elif board[3]==board[4]==computer and board[5]=="-":
        board[5]==computer
    elif board[3]==board[5]==computer and board[4]=="-":
        board[4]==computer
    elif board[4]==board[5]==computer and board[3]=="-":
        board[3]==computer
        
        # checking in 3 row
    elif board[6]==board[7]==computer and board[8]=="-":
        board[8]==computer
    elif board[6]==board[8]==computer and board[7]=="-":
        board[7]==computer
    elif board[7]==board[8]==computer and board[6]=="-":
        board[6]==computer
        
    #checking column
    # checking column  1
    elif board[0]==board[3]==computer and board[6]=="-":
        board[6]==computer
    elif board[6]==board[0]==computer and board[3]=="-":
        board[3]==computer
    elif board[3]==board[6]==computer and board[0]=="-":
        board[0]==computer
    
    #checking column 2
    elif board[1]==board[4]==computer and board[7]=="-":
        board[7]==computer
    elif board[1]==board[7]==computer and board[4]=="-":
        board[4]==computer
    elif board[7]==board[4]==computer and board[1]=="-":
        board[1]==computer
    
    #checking column 3
    elif board[2]==board[5]==computer and board[8]=="-":
        board[8]==computer
    elif board[2]==board[8]==computer and board[5]=="-":
        board[5]==computer
    elif board[5]==board[8]==computer and board[2]=="-":
        board[2]==computer
     
    # checking diagonls
    # checking diagonal_1
    elif board[0]==board[4]==computer and board[8]=="-":
        board[8]==computer
    elif board[0]==board[8]==computer and board[4]=="-":
        board[4]==computer
    elif board[4]==board[8]==computer and board[0]=="-":
        board[0]==computer
    
    #checking diagonal_2
    elif board[2]==board[4]==computer and board[6]=="-":
        board[6]==computer
    elif board[2]==board[6]==computer and board[4]=="-":
        board[4]==computer
    elif board[4]==board[6]==computer and board[2]=="-":
        board[2]==computer
 # egoist end-------------------------------------------  
    
    return

play_game()    
