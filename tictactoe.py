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

def tour(signe, plateau, joueur, niveau, score):

    caseLibre = caseRestante(plateau)

    meilleurChoix = ia(plateau, signe)
    mauvaisChoix = [case for case in caseLibre if case != meilleurChoix]

    if joueur["mode"] == 1:

        if random.randint(1,10) > niveau:

            if mauvaisChoix:
                j = random.choice(mauvaisChoix)
            else:
                j = random.choice(caseLibre)
            
            print("IA",signe,": ",j)
            
        else:
            j = meilleurChoix
            print("IA",signe,": ",j)
        
    else :
        while True:
            
            try:
                j = int(input(joueur["Nom"] + ": "))

                if 0 <= j <= 8 and testCase(j,plateau):
                    break

            except:
                print("chiffres entre 0 et 8.")
    
    
    plateau[j//3][j%3] = signe

    affichage(plateau)

    if victoire(j,plateau):
        print(joueur["Nom"]+ " a gagné!\n")
        score[signe] += 1
        return False

    if nul(plateau):
        print("Match Nul.\n")
        score[0] += 1
        return False

    return True

def partie(joueurs, niveauIA, score):

    plateau = [[0,0,0],[0,0,0],[0,0,0]]

    while True:

        if not (tour(1, plateau, joueurs[0], niveauIA[0], score)):
            break
        if not (tour(2, plateau, joueurs[1], niveauIA[1], score)):
            break

    print(f"Match nul : {score[0]}  |  {joueurs[0]['Nom']} : {score[1]} | {score[2]} : {joueurs[1]['Nom']}\n")

def main():

    joueurs = [{"mode" : 0, "Nom" : ""} , {"mode" : 0, "Nom" : ""}]
    niveauIA = [0,0]
    score = [0,0,0]

    for i in range(2):

        while True:

            try:
                
                joueurs[i]["mode"] = int(input("Joueur%s: Manuel(0) ou Auto(1) ? " % (i+1)))

                if joueurs[i]["mode"] == 1:
                    niveauIA[i] = int(input("Niveau IA 0(Facile) à 10(Difficile) ? "))
                    joueurs[i]["Nom"] = f"IA{niveauIA[i]}-{i+1}"

                else:
                    joueurs[i]["Nom"] = input("Nom : ")

                if joueurs[i]["mode"] == 0 or joueurs[i]["mode"] == 1 and 0 <= niveauIA[i] <= 10:
                    break

            except:
                print("input invalide, chiffre seulement.")
    
    while True:

        partie(joueurs, niveauIA, score)

        rejouer = input("Rejouer ? oui(0): ")
        if rejouer != "0":
            break

        
    f = open("scores.txt", "a")
    f.write(f"Match nul : {score[0]}  |  {joueurs[0]['Nom']} : {score[1]} | {score[2]} : {joueurs[1]['Nom']}\n")
    f.close()

main()