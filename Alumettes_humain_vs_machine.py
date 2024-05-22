import time 
import random
# def controller un nombre
def controller(val : int, borneMin : int, borneMax : int ):
    """Procédure permettant de verifier si un nombre est bien entre sa borne min et sa borne max

    Args:
        val (int): la valeur du nombre demmander
        borneMin (int): Valeur minimal du nombre
        borneMax (int): valeur maximal du nombre
        
    rerourne le nombrecontroller
    """
    while val < borneMin or val > borneMax:
        print("Erreure")
        val = int(input("Saisir une nouvelle valeur : "))

    return val
# def savoir si victoire
def victoire(val_principal : int, nombre : int)-> bool:
    """C'est une fonction permettant de savoir si une variable est infèrieure ou égal à zero

    Args:
        val_principal (int): valeur de la variable à controller 
        nombre (int): nombre à soustraire

    Returns:
        bool: retourne la vérification pour savoir si la variable est infèrieure ou égal à zero
    """
    verif : bool
    verif = True
    # permet de voir si un joueur a gagner
    val_principal = val_principal - nombre
    if val_principal <= 0:
        verif = True    # renvoi la réponse que un joueur à gagner 
    else:
        verif = False   # # renvoi la réponse que aucun joueur à gagner
    
    return verif
# def pemettan de lancer le jeu
def jeu_Alumettes_H_vs_M(joueur : str, score_j : int)-> int:
    """Procédure permettant de lancer le jeu des Alumettes
    """
    # Initialisation des variables
    allumettes : int
    player : str
    choix_joueur : int
    choix_bot : int
    # Déclarartion des variables
    allumettes = 20
    player = joueur
   
    # Corps du jeu
    while allumettes > 0:

        print("au tour du joueur",player,"!")   # permet de savoir quel joueur joue
        # tour du joueur 1
        if player == joueur :
            choix_joueur = int(input("combien d'allumettes voulez-vous retirer : "))
            controller(choix_joueur,1,3)       # appelle a la fonction controller
            # controlle si le joueur 2 à gagner 
            if victoire(allumettes, choix_joueur) == True:     # appel a la fonction victoire
                print("")
                print(joueur,"à GAGNER !!!")
                score_j = score_j + 1
                allumettes = 0
                return score_j
            # Affiche le nombre d'alumettes restante
            else :
                allumettes = allumettes - choix_joueur
                print("Il reste :",allumettes,"allumettes")
                print("")
            player = "bot"
        # tour du joueur 2
        else:
            time.sleep(1)
            choix_bot = random.randint(1,3)
            # controlle si le joueur 1 à gagner 
            if victoire(allumettes, choix_bot) == True:     # appel a la fonction victoire
                print("")
                print(player," à PERDU !!!")
                if player == "bot":
                    score_j = score_j + 1
                allumettes = 0
            # Affiche le nombre d'alumettes restante
            else:
                print("bot à retirer", choix_bot, "alumettes")
                allumettes = allumettes - choix_bot
                print("Il reste :",allumettes,"allumettes")
                print("")
            player = joueur
    
    # affiche les scores en fin de jeu
    print(score_j, "pour", joueur)
    return score_j
      