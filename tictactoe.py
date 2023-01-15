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

        #En fonction du niveau choisi l'ia a une chance plus ou moins élevée de se tromper
        if random.randint(1,10) > niveau:

            if mauvaisChoix:
                j = random.choice(mauvaisChoix)
            else:
                j = random.choice(caseLibre)
              
        else:
            j = meilleurChoix

        print(f"{joueur['Nom']}: {j}")
        
    else :
        while True:
            
            try:
                j = int(input(f"{joueur['Nom']}: "))

                if 0 <= j <= 8 and testCase(j,plateau):
                    break

            except:
                print("chiffres entre 0 et 8.")
    
    
    plateau[j//3][j%3] = signe

    affichage(plateau)

    #Après que le tour sois joué on verifie si le coup est gagnant
    if victoire(j,plateau):
        print(f"{joueur['Nom']} a gagné!\n")
        score[signe] += 1
        return False

    #Ou s'il y a match nul
    if nul(plateau):
        print("Match Nul.\n")
        score[0] += 1
        return False

    return True


def partie(joueurs, niveauIA, score):

    plateau = [[0,0,0],[0,0,0],[0,0,0]]

    while True:
        #La fonction tour retourne False si la partie est terminée
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
        #Menu Joueur
        while True:

            try:

                joueurs[i]["mode"] = int(input(f"Joueur{i+1}: Manuel(0) ou Auto(1) ? "))

                if joueurs[i]["mode"] == 1:
                    niveauIA[i] = int(input("Niveau IA 0(Facile) à 10(Difficile) ? "))
                    
                    joueurs[i]["Nom"] = f"IA{niveauIA[i]}-{i+1}"

                else:
                    joueurs[i]["Nom"] = input("Nom : ")

                if joueurs[i]["mode"] == 0 or joueurs[i]["mode"] == 1 and 0 <= niveauIA[i] <= 10:
                    break

            except:
                print("input invalide, chiffre uniquement.")
    
    while True:

        partie(joueurs, niveauIA, score)

        rejouer = input("Rejouer ? oui(0): ")
        if rejouer != "0":
            break

    #Ecriture des scores dans un fichier texte
    f = open("historique.txt", "a")
    f.write(f"Match nul : {score[0]}  |  {joueurs[0]['Nom']} : {score[1]} | {score[2]} : {joueurs[1]['Nom']}\n")
    f.close()

main()