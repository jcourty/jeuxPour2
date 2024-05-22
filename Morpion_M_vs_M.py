import random
import time
# Def pour afficher la grille du morpion
def afficher_grille(tab : list[str]):
    """Procedure permettant d'afficher la scene de jeu du morpion

    Args:
        tab (_type_): La grille de morpion
    """
    
    print("     0)  1)  2)")    # Défini les colones de la grille 
    print("    ___ ___ ___ ")     # ligne de la grille
    print("0)", end='')     # definie les lignes de la grille
    for i in range (3):
        print(" | " + str(tab[i]), end='')
    print(" |")
    print("   |___|___|___|")    # ligne de la grille
    print("1)", end='')     # definie les lignes de la grille
    for i in range (3):
        print(" | " + str(tab[i+3]), end='')
    print(" |")
    print("   |___|___|___|")    # ligne de la grille
    print("2)", end='')     # definie les lignes de la grille
    for i in range (3):
        print(" | " + str(tab[i+6]), end='')
    print(" |")
    print("   |___|___|___|")    # ligne de la grille
# Def pour permettre a chaque joueur de jouer 
def tour(tab : list[str], player : int):
    """Procedure permettant au joueur de placer son caractère dans la grille du morpion.

    Args:
        tab (_type_): La grille du morpion
        player (int): Le numero du joueur 
    """
    colonne : int
    ligne : int
    
    # Definie la case que le joueur veut jouer 
    print("C'est le tour du bot "+str(player))
    colonne=random.randint(0,2)
    ligne=random.randint(0,2)
    print("La case (", colonne, ",", ligne, ") à été joué")
    
    # Permet de verifier si la case et prise ou non 
    while tab[int(colonne)+int(ligne)*3]!=" ":
        afficher_grille(tab)        # affiche la grille pour pouvoir voir les case vide
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=random.randint(0,2)
        ligne=random.randint(0,2)
        print("Vous avez joué la case (", colonne, ",", ligne, ")")
 
    if player == 1 :
        tab[colonne + ligne *3]="X"
    else :
        tab[colonne + ligne*3]="O"
    
    afficher_grille(tab)    # Affiche la grille avec le nouveau caractère ajouter
    
# def Pour savoir si victoire
def est_gagnant(tab : list[str]):
    """Procedure permettant de verifier si un joueur a remporter la partie

    Args:
        tab (_type_): La grille du morpion.

    Returns:
        binaire : si il retourne 1 alors un joueur a remporter la partie.
    """
    
    # teste tout les combinaison de victoire possible 
    if (tab[0]==tab[1]) and (tab[0]==tab[2]) and (tab[0]!=" "): 
        return 1        # Retourne 1 si cette combinaison est respecter 
        
    if (tab[3]==tab[4]) and (tab[3]==tab[5]) and (tab[3]!=" "):
        return 1        # Retourne 1 si cette combinaison est respecter 
        
    if (tab[6]==tab[7]) and (tab[6]==tab[8]) and (tab[6]!=" "):
        return 1        # Retourne 1 si cette combinaison est respecter 
        
    if (tab[0]==tab[3]) and (tab[0]==tab[6]) and (tab[0]!=" "):
        return 1        # Retourne 1 si cette combinaison est respecter 
        
    if (tab[1]==tab[4]) and (tab[1]==tab[7]) and (tab[1]!=" "):
        return 1        # Retourne 1 si cette combinaison est respecter 
        
    if (tab[2]==tab[5]) and (tab[2]==tab[8]) and (tab[2]!=" "):
        return 1        # Retourne 1 si cette combinaison est respecter 
        
    if (tab[0]==tab[4]) and (tab[0]==tab[8]) and (tab[0]!=" "):
        return 1        # Retourne 1 si cette combinaison est respecter 
        
    if (tab[2]==tab[4]) and (tab[2]==tab[6]) and (tab[2]!=" "):
       return 1         # Retourne 1 si cette combinaison est respecter 
# def pour savoir si match nul
def Match_nul(tab : list[str]):
    """Fonction permettant de savoir si il y a match nul

    Args:
        tab (list[str]): La grille du morpion

    Returns:
        0 / 1 : 0 ou 1 en fonction de si il y a match (1) nul ou non (0)
    """
    for i in range(9):
        if tab[i]==" ":
            return 0
    return 1
    
    
    return verif
# def pemettan de lancer le jeu
def jeu_morpion_M_vs_M():
    """Fonction permettant de lancer le jeu
    """
    # Affectation des variables. 
    gagne : int
    grille : list[str]
    joueur : int
    
    # Déclaration des variables.
    joueur = 1
    gagne=0
    grille=[" ", " "," ", " "," ", " "," ", " "," "]        # Representer le tableau du morpion.
     
    # Montre ce que chaque joueur joue comme caractère.
    print("Le joueur 1  possède les X. Le joueur 2 possède les 0")
    afficher_grille(grille)     # permet d'afficher la grille du morpion.
    
    while gagne == 0:
        time.sleep(1)
        tour(grille,joueur) # permet au joueur de placer son caractère sur la grille  
        if est_gagnant(grille):     # teste si il y a une combinaison gagnante.
            print("Le bot " , joueur, "remporte la partie !! ")    # Annonce le gagnant de la partie.
            gagne = 1 
        else:       # teste si il y a un match nul.
            if Match_nul(grille):
                print("Plus de place ! Match nul !")
                gagne=1
            
        # permet de definir le tour de chaque joueur.
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
            
