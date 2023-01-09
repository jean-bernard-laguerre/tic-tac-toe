def affichage(plateau):

    for x in range(len(plateau)):
        for y in range(len(plateau)):

            match plateau[x][y]:
                case 1:
                    print(" X ", end="")
                case 2:
                    print(" O ", end="")
                case _:
                    print("   ", end="")
                

        print("")

def testCase(case, plateau):

    if plateau[case//len(plateau)][case%len(plateau)] == 0:
        return True

    return False

def testVictoire(case,p):

    ligne = (p[case//len(p)][0] == p[case//len(p)][1] == p[case//len(p)][2])
    diagonale1 = (p[0][0] == p[1][1] == p[2][2] != 0)
    diagonale2 = (p[0][2] == p[1][1] == p[2][0] != 0)

    if  ligne or diagonale1 or diagonale2:
        return True
    return False

def testNul(plateau):

    for x in range(len(plateau)):
        for y in range(len(plateau)):
            if plateau[x][y] == 0:
                return False
    return True

def tour(joueur, plateau):

    while True:

        j = int(input("Joueur " + str(joueur) + ": "))
        if 0 <= j <= 8 and testCase(j,plateau):
            break
        print("invalide")
    
    plateau[j//len(plateau)][j%len(plateau)] = joueur

    affichage(plateau)

    if testVictoire(j,plateau):
        print("Joueur " + str(joueur) + " a gagné!")
        return False

    if testNul(plateau):
        print("Match Nul.")
        return False

    return True

def main():

    plateau = [[0,0,0],[0,0,0],[0,0,0]]

    while True:

        if not (tour(1, plateau)):
            break
        if not (tour(2, plateau)):
            break

main()