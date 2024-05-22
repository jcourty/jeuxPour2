import time
import random
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
def jeu_Alumettes_M_vs_M():
    """Procédure permettant de lancer le jeu des Alumettes
    """
    # Initialisation des variables
    allumettes : int
    bot : int
    choix_bot1 : int
    choix_bot2 : int
    # Déclarartion des variables
    allumettes = 20
    bot = 1
    # Corps du jeu
    while allumettes > 0:
        time.sleep(1)
        print("Au tour du bot", bot)  # permet de savoir quel joueur joue
        # tour du joueur 1
        if bot == 1 :
            choix_bot1 = random.randint(1,3)
            # controlle si le joueur 2 à gagner 
            if victoire(allumettes, choix_bot1) == True:     # appel a la fonction victoire
                print("")
                print("bot 1 à GAGNER !!!")
                allumettes = 0
            # Affiche le nombre d'alumettes restante
            else :
                allumettes = allumettes - choix_bot1
                print("Il reste :",allumettes,"allumettes")
                print("")
            bot = 2
        # tour du joueur 2
        else:
            choix_bot2 = random.randint(1,3)
            # controlle si le joueur 1 à gagner 
            if victoire(allumettes, choix_bot2) == True:     # appel a la fonction victoire
                print("")
                print("bot 2 à GAGNER !!!")
                allumettes = 0
            # Affiche le nombre d'alumettes restante
            else:
                allumettes = allumettes - choix_bot2
                print("Il reste :",allumettes,"allumettes")
                print("")
            bot = 1
