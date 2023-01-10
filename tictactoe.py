from ia import *
from outils import *

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
    print("")

def tour(joueur, plateau, mode):

    if mode == "ia":
        j = ia(plateau, joueur)
        print("IA",joueur,": ",j)
    else :
        while True:

            j = int(input("Joueur " + str(joueur) + ": "))
            if 0 <= j <= 8 and testCase(j,plateau):
                break
            print("invalide")
    
    
    plateau[j//len(plateau)][j%len(plateau)] = joueur

    affichage(plateau)

    if victoire(j,plateau):
        print("Joueur " + str(joueur) + " a gagné!")
        return False

    if nul(plateau):
        print("Match Nul.")
        return False

    return True

def main():

    plateau = [[0,0,0],[0,0,0],[0,0,0]]
    mode1 = ""
    mode2 = "ia"

    while True:

        if not (tour(1, plateau, mode1)):
            break
        if not (tour(2, plateau, mode2)):
            break

main()