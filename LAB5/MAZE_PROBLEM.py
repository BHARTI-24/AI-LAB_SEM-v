row=4
column=4

board= [
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    ]
def print_board():
    for i in range(0,6):
        print('#',end=" ")
        
    print("\n# "+board[0][0]+" "+board[0][1]+" "+board[0][2]+" "+board[0][3]+" # ")   
    print("# "+board[1][0]+" "+board[1][1]+" "+board[1][2]+" "+board[1][3]+" # ") 
    print("# "+board[2][0]+" "+board[2][1]+" "+board[2][2]+" "+board[2][3]+" # ")
    print("# "+board[3][0]+" "+board[3][1]+" "+board[3][2]+" "+board[3][3]+" # ")
    for i in range(0,6):
        print('#',end=" ")
        
    return

board[1][0]=str(0)  #start state 
board[2][3]=str(1)  #final state


moves={}

moves=dict(moves)
 
 
def obstacles():
    board[1][1]='#'
    board[2][1]='#'
    board[1][2]='#'
    board[0][3]='#'
    board[3][0]='#'
    return



def create_moves():
    for i in range (0,4):
        for j in range (0,4):
            if board[i-1,j-1]==' ':
                moves[(i-1,j-1)=1
    
            elif board[i-1,j]==' ':
                moves[(i-1,j)]=1
            
            elif board[i-1,j+1]==' ':
                moves[(i-1,j+1)]=1
            
            elif board[i,j-1]==' ':
                moves[(i,j-1)]=1
            
            elif board[i,j]==' ':
                moves[([i,j)]=1 
                
            elif board[i,j+1]==' ':
                moves[(i,j+1)]=1
                
            elif board[i+1,j-1]==' ':
                moves[(i+1,j-1)]=1
                
            elif board[i+1,j]==' ':
                moves[(i+1,j)]=1
                
            elif board[i+1,j+1]==' ':
                moves[(i+1,j+1)]=1
            else
                return
            
    
    return


obstacles()
print_board()
