from outils import *
import random

def ia(board, signe):
    
    coups = []
    i = 0

    if testCase(4,board):
        return 4
        
    while i < 2:
        for x in range(9):

            if(testCase(x,board)):

                board[x//len(board)][x%len(board)] = signe

                if victoire(x,board):
                    board[x//len(board)][x%len(board)] = 0
                    return x

                if i == 0 and testCoup(x, board, signe):
                    coups += [x]

                board[x//len(board)][x%len(board)] = 0

        if signe == 1:
            signe = 2
        else:
            signe = 1

        i+=1
        

    if len(coups) > 0:
        print("coups:",coups)
        return random.choice(coups)

    while True:
        
        emplacement  = random.randint(0,8)
        if testCase(emplacement, board):
            break

    return emplacement

def testCoup(c, p, signe):
    ligne = [ p[c//3][0], p[c//3][1], p[c//3][2] ]
    colonne = [ p[0][c%3], p[1][c%3], p[2][c%3] ]
    coins = [0,2,6,8]

    match signe:
        case 1:
            if(2 in ligne or 2 in colonne) or c not in coins:
                return False
        case 2:
            if(1 in ligne or 1 in colonne) or c not in coins:
                return False
    return True