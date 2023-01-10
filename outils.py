def testCase(case, plateau):

    if plateau[case//len(plateau)][case%len(plateau)] == 0:
        return True

    return False

def victoire(case,p):

    ligne = (p[case//len(p)][0] == p[case//len(p)][1] == p[case//len(p)][2])
    colonne = (p[0][case%len(p)] == p[1][case%len(p)] == p[2][case%len(p)])
    diagonale1 = (p[0][0] == p[1][1] == p[2][2] != 0)
    diagonale2 = (p[0][2] == p[1][1] == p[2][0] != 0)

    if  ligne or colonne or diagonale1 or diagonale2:
        return True
    return False

def nul(plateau):

    for x in range(len(plateau)):
        for y in range(len(plateau)):
            if plateau[x][y] == 0:
                return False
    return True