
from Alumettes_humain_vs_humain import controller
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
def tour(tab : list[str], player : str, player1 : str, player2 : str):
    """Procedure permettant au joueur de placer son caractère dans la grille du morpion.

    Args:
        tab (_type_): La grille du morpion
        player (int): Le numero du joueur 
    """
    colonne : int
    ligne : int
    # Definie la case que le joueur veut jouer 
    print("C'est le tour du joueur "+str(player))
    colonne=int(input("Entrez le numero de la colonne : "))
    colonne = controller(colonne,0,2)
    ligne=int(input("Entrez le numero de la ligne : "))
    ligne = controller(ligne,0,2)
    print("Vous avez joué la case (", colonne, ",", ligne, ")")
    
    # Permet de verifier si la case et prise ou non 
    while tab[int(colonne)+int(ligne)*3]!=" ":
        afficher_grille(tab)        # affiche la grille pour pouvoir voir les case vide
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=int(input("Entrez le numero de la colonne : "))
        colonne = controller(colonne,0,2)
        ligne=int(input("Entrez le numero de la ligne : "))
        ligne = controller(ligne,0,2)
        print("Vous avez joué la case (", colonne, ",", ligne, ")")
 
    if player == player1 :
        tab[colonne + ligne *3]="X"     # Définie le caractére utiliser pour le joueur 1
    if player == player2 :
        tab[colonne + ligne*3]="O"      # Définie le caractére utiliser pour le joueur 2
    afficher_grille(tab)        # Affiche la grille avec le nouveau caractère ajouter
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
def jeu_morpion(joueur1 : str, joueur2 : str, score_j1 : int, score_j2: int)-> str:
    """Fonction permettant de lancer le jeu
    """
    # Affectation des variables. 
    joueur : str
    gagne : int
    grille : list[str]
    
    # Déclaration des variables.
    joueur= joueur1
    gagne=0
    grille=[" ", " "," ", " "," ", " "," ", " "," "]        # Representer le tableau du morpion.
     
    # Montre ce que chaque joueur joue comme caractère.
    print("Le joueur 1  possède les X. Le joueur 2 possède les 0")
    afficher_grille(grille)     # permet d'afficher la grille du morpion.
    
    while gagne == 0:
        tour(grille, joueur, joueur1, joueur2 )        # permet au joueur de placer son caractère sur la grille 
        if est_gagnant(grille):     # teste si il y a une combinaison gagnante.
            print("Le joeur " + str(joueur) + " remporte la partie !! ")    # Annonce le gagnant de la partie. 
            # Faire les scores de chaque joueur 
            if joueur == joueur1 : 
                score_j1 = score_j1 + 1
                print(score_j1, "pour", joueur1)
                print(score_j2, "pour", joueur2)
                return joueur1
            else:
                score_j2 = score_j2 + 1
                print(score_j1, "pour", joueur1)
                print(score_j2, "pour", joueur2)
                return joueur2
            
        else:       # teste si il y a un match nul.
            if Match_nul(grille):
                print("Plus de place ! Match nul !")
                gagne=1
            
        # permet de definir le tour de chaque joueur.
        if joueur == joueur1:
            joueur = joueur2
        else:
            joueur = joueur1  
    return " Personne "


