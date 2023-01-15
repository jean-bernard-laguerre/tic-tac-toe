coins = [0,2,6,8]

def testCase(case, plateau):

    #Retourne True si la case est vide
    if plateau[case//3][case%3] == 0:
        return True

    return False

def caseRestante(plateau):

    #Retourne liste des cases libres
    caseLibre = []

    for x in range(9):

        if plateau[x//3][x%3] == 0:
            caseLibre += [x]
    

    return caseLibre

def victoire(case,p):

    #Teste si la ligne/colonne de la case jouée ou l'une des diagonales a 3 fois le meme signe 
    ligne = (p[case//3][0] == p[case//3][1] == p[case//3][2])
    colonne = (p[0][case%3] == p[1][case%3] == p[2][case%3])
    diagonale1 = (p[0][0] == p[1][1] == p[2][2] != 0)
    diagonale2 = (p[0][2] == p[1][1] == p[2][0] != 0)


    if  ligne or colonne or diagonale1 or diagonale2:
        return True

    return False

def nul(plateau):

    #Retourne True si aucune case est vide
    for x in range(3):
        for y in range(3):

            if plateau[x][y] == 0:
                return False

    return True