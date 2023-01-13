from outils import *
import random

def ia(board, signe):
    
    caseLibre = caseRestante(board)
    coinsLibre = []
    coups = []
    i = 0

    if testCase(4,board):
        return 4
        
    while i < 2:
        for x in caseLibre:

            board[x//3][x%3] = signe

            if victoire(x,board):
                board[x//3][x%3] = 0
                return x

            if i == 0 and testCoup(x, board, signe):
                coups += [x]

            if x in coins:
                coinsLibre += [x]

            board[x//3][x%3] = 0

        if signe == 1:
            signe = 2
        else:
            signe = 1

        i+=1
      

    if len(coups) > 0:
        return random.choice(coups)
    
    if len(coinsLibre) > 0:
        return random.choice(coinsLibre)

    return random.choice(caseLibre)

def testCoup(c, p, signe):

    ligne = [ p[c//3][0], p[c//3][1], p[c//3][2] ]
    colonne = [ p[0][c%3], p[1][c%3], p[2][c%3] ]

    match signe:
        
        case 1:
            if(2 in ligne or 2 in colonne) or c not in coins:
                return False
                
        case 2:
            if(1 in ligne or 1 in colonne) or c not in coins:
                return False

    return True