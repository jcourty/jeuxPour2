
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
def jeu_Alumettes(joueur1 : str, joueur2 : str, score_j1 : int, score_j2: int)-> str:
    """Procédure permettant de lancer le jeu des Alumettes
    """
    # Initialisation des variables
    allumettes : int
    player : str
    # Déclarartion des variables
    allumettes = 20
    player = joueur1
   
    # Corps du jeu
    while allumettes > 0:

        print("au tour du joueur",player,"!")   # permet de savoir quel joueur joue
        # tour du joueur 1
        if player == joueur1 :
            choix_joueur1 = int(input("combien d'allumettes voulez-vous retirer : "))
            controller(choix_joueur1,1,3)       # appelle a la fonction controller
            # controlle si le joueur 2 à gagner 
            if victoire(allumettes, choix_joueur1) == True:     # appel a la fonction victoire
                print("")
                print(joueur2,"à GAGNER !!!")
                score_j2 = score_j2 + 1
                allumettes = 0
                return joueur2
            # Affiche le nombre d'alumettes restante
            else :
                allumettes = allumettes - choix_joueur1
                print("Il reste :",allumettes,"allumettes")
                print("")
            player = joueur2
        # tour du joueur 2
        else:
            choix_joueur2 = int(input("combien d'allumettes voulez-vous retirer : "))
            controller(choix_joueur2,1,3)       # appelle a la fonction controller
            # controlle si le joueur 1 à gagner 
            if victoire(allumettes, choix_joueur2) == True: # appel a la fonction victoire
                print("")
                print(joueur1,"à GAGNER !!!")
                score_j1 = score_j1 + 1
                allumettes = 0
                return joueur1
            # Affiche le nombre d'alumettes restante
            else:
                allumettes = allumettes - choix_joueur2
                print("Il reste :",allumettes,"allumettes")
                print("")
            player = joueur1
    
    print(score_j1, "pour", joueur1)
    print(score_j2, "pour", joueur2)
    return " Personne "  
        