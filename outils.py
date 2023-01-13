coins = [0,2,6,8]

def testCase(case, plateau):

    if plateau[case//3][case%3] == 0:
        return True

    return False

def caseRestante(plateau):

    caseLibre = []

    for x in range(9):

        if plateau[x//3][x%3] == 0:
            caseLibre += [x]
    

    return caseLibre

def victoire(case,p):

    ligne = (p[case//3][0] == p[case//3][1] == p[case//3][2])
    colonne = (p[0][case%3] == p[1][case%3] == p[2][case%3])
    diagonale1 = (p[0][0] == p[1][1] == p[2][2] != 0)
    diagonale2 = (p[0][2] == p[1][1] == p[2][0] != 0)

    if  ligne or colonne or diagonale1 or diagonale2:
        return True

    return False

def nul(plateau):

    for x in range(3):
        for y in range(3):

            if plateau[x][y] == 0:
                return False

    return True