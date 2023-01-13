from ia import *
from outils import *

def affichage(plateau):

    for x in range(3):
        for y in range(3):

            match plateau[x][y]:
                case 1:
                    print(" X ", end="")
                case 2:
                    print(" O ", end="")
                case _:
                    print("   ", end="")
                
        print("")
    print("")

def tour(joueur, plateau, mode, niveau, score):

    caseLibre = caseRestante(plateau)

    meilleurChoix = ia(plateau, joueur)
    mauvaisChoix = [case for case in caseLibre if case != meilleurChoix]

    if mode == 1:

        if random.randint(1,10) > niveau:

            if mauvaisChoix:
                j = random.choice(mauvaisChoix)
            else:
                j = random.choice(caseLibre)
            
            print("IA",joueur,": ",j)
            
        else:
            j = meilleurChoix
            print("IA",joueur,": ",j)
        
    else :
        while True:
            
            try:
                j = int(input("Joueur " + str(joueur) + ": "))

                if 0 <= j <= 8 and testCase(j,plateau):
                    break

            except:
                print("chiffres entre 0 et 8.")
    
    
    plateau[j//3][j%3] = joueur

    affichage(plateau)

    if victoire(j,plateau):
        print("Joueur " + str(joueur) + " a gagné!\n")
        score[joueur] += 1
        return False

    if nul(plateau):
        print("Match Nul.\n")
        score[0] += 1
        return False

    return True

def partie(mode, niveauIA, score):

    plateau = [[0,0,0],[0,0,0],[0,0,0]]

    while True:

        if not (tour(1, plateau, mode[0], niveauIA[0], score)):
            break
        if not (tour(2, plateau, mode[1], niveauIA[1], score)):
            break


def main():

    mode = [0,0]
    niveauIA = [0,0]
    score = [0,0,0]

    for i in range(2):

        while True:

            try:
                mode[i] = int(input("Joueur%s: Manuel(0) ou Auto(1) ? " % (i+1)))

                if mode[i] == 1:
                
                    niveauIA[i] = int(input("Niveau IA 0(Facile) à 10(Difficile) ? "))

                if mode[i] == 0 or mode[i] == 1 and 0 <= niveauIA[i] <= 10:
                    break

            except:
                print("input invalide, chiffre seulement.")
    
    while True:

        partie(mode, niveauIA, score)

        print("Match nul : %s  |  Joueur1 : %s | %s : Joueur2\n" % (score[0],score[1],score[2]))

        rejouer = input("Rejouer ? oui(0): ")
        if rejouer != "0":
            break

        
    f = open("scores.txt", "a")
    f.write("Match nul : %s  |  Joueur1 : %s | %s : Joueur2\n" % (score[0],score[1],score[2]))
    f.close()

main()