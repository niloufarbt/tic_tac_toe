#niloufar BAYAT 
#this is a tic tac toe game for two players


board = {'a1':' ','a2': ' ','a3':' ',
        'b1':' ','b2':' ','b3':' ',
        'c1':' ','c2':' ','c3':' ' }

#to initiate first player
player = 1
#to count moves
nb_moves = 0


def check():
    # checking the moves of player one
    #for horizontal
    if ( (board['a1']=='X' and board['a2']=='X' and board['a3']=='X') or
        (board['b1']=='X' and board['b2']=='X' and board['b3']=='X') or
        ( board['c1']=='X' and board['c2']=='X' and board['c3']=='X') ) :
        print('Player one won !')
        return 1
    #for diagonal
    if ( (board['a1']=='X' and board['b2']=='X' and board['c3']=='X') or
        (board['a3']=='X' and board['b2']=='X' and board['c1']=='X') ):
        print('Player One Won!!')
        return 1
    #for vertical
    if( (board['a1']=='X' and board['b1']=='X' and board['c1']=='X') or 
        (board['a2']=='X' and board['b2']=='X' and board['c2']=='X') or 
        (board['a3']=='X' and board['b3']=='X' and board['c3']=='X') ):
        print('Player One Won!!')
        return 1


    # checking the moves of player two
    #for horizontal
    if( (board['a1']=='O' and board['a2']=='O' and board['a3']=='O') or
        (board['b1']=='O' and board['b2']=='O' and board['b3']=='O') or
        (board['c1']=='O' and board['c2']=='O' and board['c3']=='O') ):
        print('Player Two Won!!')
        return 1  # used to end the game
    #for diagonal
    if ( (board['a1']=='O' and board['b2']=='O' and board['c3']=='O') or
        (board['a3'] == 'O' and board['b2'] == 'O' and board['c1'] == 'O') ):
        print('Player Two Won!!')
        return 1
    #for vertical
    if ( (board['a1']=='O' and board['b1']=='O' and board['c1']=='O') or
        (board['a2']=='O' and board['b2']=='O' and board['c2']=='O') or
        (board['a3']=='O' and board['b3']=='O' and board['c3']=='O') ):
        print('Player Two Won!!')
        return 1

    return 0


print( 'a1 | a2 | a3' + "\n" + '-  | -  | -  ' )
print( 'b1 | b2 | b3' + "\n" + '-  | -  | -  ' )
print( 'c1 | c2 | c3')
print( '*****************************')

while True :
    print( board['a1'] + ' | ' + board['a2'] + ' | ' + board['a3'] )
    print( board['b1'] + ' | ' + board['b2'] + ' | ' + board['b3'] )
    print( board['c1'] + ' | ' + board['c2'] + ' | ' + board['c3'] )
    print( '*****************************')
    end_check = check()
    if (nb_moves == 9) or (end_check == 1):
        break
    while True :
        if player == 1:
            p1_input = input('player one : ')
            if (p1_input.lower() in board) and (board[p1_input.lower() ] == ' '):
                board[p1_input.lower()] = 'X'
                player = 2
                break
            else : #wrong input
                print('invalid input try again')
                continue
        else:
            p2_input = input('player two : ')
            if ( p2_input.lower() in board) and (board[p2_input.lower()] == ' ') :
                board[p2_input.lower()] = 'O'
                player = 1
                break
            else : #wrong input
                print('invalid input try again')
                continue
    nb_moves += 1
    print('*****************************')
    print()
   

