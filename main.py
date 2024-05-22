from devinettes import devinette, deviBot, deviOrdi
from Alumettes_humain_vs_humain import jeu_Alumettes,controller
from Alumettes_humain_vs_machine import jeu_Alumettes_H_vs_M
from Alumettes_machine_vs_machine import jeu_Alumettes_M_vs_M
from Morpion_H_vs_H import jeu_morpion
from Morpion_H_vs_M import jeu_morpion_H_vs_M
from Morpion_M_vs_M import jeu_morpion_M_vs_M
import os

def choix()->int:
    print("1-Jeux à deux")
    print("2-Jeux contre l'ordi")
    print("3-Jeux ordi contre ordi")
    print("4-Quitter")
    n=int(input("Faites votre choix:"))
    controller(n,1,4)

    return n


def menu(n:int) ->int:
    c:int
    if n==1 or n==2:
        print("1-Jeu de devinette")
        print("2-Jeu des allumettes")
        print("3-Jeu du morpion")
        print("4-Changer de joueur")
        print("5-Les Scores")
        print("6-Quitter")
        c=int(input("Faites votre choix:"))
        controller(c,1,6)
    elif n==3:
        print("1-Jeu de devinette")
        print("2-Jeu des allumettes")
        print("3-Jeu du morpion")
        print("4-Quitter")
        c=int(input("Faites votre choix:"))
        controller(c,1,4)
    return c

from typing import TextIO

if __name__=='__main__':
    f : TextIO
    score_joueur1_devinette : int
    score_joueur2_devinette  : int
    score_joueur1_morpion : int
    score_joueur2_morpion  : int
    score_joueur1_alumettes : int
    score_joueur2_alumettes  : int
    
    score_joueur2_devinette  = 0
    score_joueur1_devinette  = 0
    score_joueur1_morpion = 0
    score_joueur2_morpion = 0
    score_joueur1_alumettes = 0
    score_joueur2_alumettes = 0
    
    c=int
    n=int
    z=str
    n=0
    c=0
    player1 = " "
    player2 = " "

    while n!=4:
        os.system('cls' if os.name=='nt' else 'clear') #permet d'effacer le terminal, pour rendre le jeu plus clair
        n=choix() #le 1 renvoie le menu ou l'on choisi si l'on veut jouer à plusieurs ou non
        if n==1: #jeu à deux
            os.system('cls' if os.name=='nt' else 'clear')
            print("Bonjour joueur. Veuillez saisir vos prénom: ")
            print()
            player1 = str(input("Joueur 1: "))
            print()
            player2 = str(input("Joueur 2: "))
            print()
            print("Bienvenue dans le menu",player1,"et",player2)
            print()

            while c!=6:  #continuera d'afficher le menu des mini-jeux tant que l'on ne quitte pas
                c=menu(n) #le deux renvoie le menu qui affiche les différent mini-jeux 
                if c==1: #devinette
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Devinettes. Le but est de deviner le nombre secret de l'autre. Ce nombre est entre le nombre 1 et une borne choisit")
                    print()
                    print()
                    score_joueur2_alumettes = score_joueur2_alumettes + devinette(player1,player2)
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')

                if c==2: #allumettes
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Allumettes. Chacun son tour, vous devez choisir d'enlever soit 1, 2 ou 3 allumettes. Votre but est d'éviter de ramasser la dernière allumette.")
                    print()
                    print()
                    if jeu_Alumettes(player1,player2,score_joueur1_alumettes,score_joueur2_alumettes) == player1:
                        score_joueur1_alumettes = score_joueur1_alumettes + 1
                    else : score_joueur2_alumettes = score_joueur2_alumettes + 1
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')
            
                if c==3: #morpion
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Morpion. Chacun son tour, les joueurs placent sa marque. Le but du jeu est d'en alligner trois de suite.")
                    print()
                    print()
                    if jeu_morpion(player1, player2,score_joueur1_morpion ,score_joueur2_morpion ) == player1:
                        score_joueur1_morpion  = score_joueur1_morpion  + 1
                    else : score_joueur2_morpion  = score_joueur2_morpion  + 1
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')
            
                if c==4: #changer de joueur
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("1-changer le nom du joeueur 1")
                    print("2-changer le nom du joueur 2")
                    print("3-changer les deux")
                    n=int(input("Faites votre choix:")) # Permet aux joueurs de choisir le nom à changer sans devoir retaper les deux
                    if n==1:
                        player1=str(input("Nouveau nom du joueur 1: "))
                        print("Changement effectué")
                    if n==2:
                        player2=str(input("Nouveau nom du joueur 2: "))
                        print("Changement effectué")
                    else:
                        player1=str(input("Nouveau nom du joueur 1: "))
                        player2=str(input("Nouveau nom du joueur 2: "))
                        print("changement effectué")
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')
                
                if c==5:    # affichage du score de chaque joueur en fonction du jeu 
                    f = open('Score.txt', 'w')  # permet d'ouvrir le fichier pour pouvoir ecrire dedans
                    # écrit le score pour le jeu de devinette
                    f.write('Devinette : ')
                    f.write ('\n')
                    f.write (player1)
                    f.write (': ' + str(score_joueur1_devinette))
                    f.write ('\n')
                    f.write (player2)
                    f.write (': ' + str(score_joueur2_devinette)) 
                    f.write ('\n')
                    f.write ('\n')
                    # écrit le score pour le jeu du morpions
                    f.write('Morpions : ')
                    f.write ('\n')
                    f.write (player1)
                    f.write (': ' + str(score_joueur1_morpion))
                    f.write ('\n')
                    f.write (player2)
                    f.write (': ' + str(score_joueur2_morpion)) 
                    f.write ('\n')
                    f.write ('\n')
                    # écrit le score pour le jeu des alumettes
                    f.write('Alumettes : ')
                    f.write ('\n')
                    f.write (player1)
                    f.write (': ' + str(score_joueur1_alumettes))
                    f.write ('\n')
                    f.write (player2)
                    f.write (': ' + str(score_joueur2_alumettes)) 
                    f.close()  
                    os.system('cls' if os.name=='nt' else 'clear')  
                    # affichage du fichier scores.txt 
                    print("Tableau des scores : ")
                    print("")
                    f = open('Score.txt','r')
                    # affiche tout le contenue 
                    message = f.read()
                    print(message)
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    f.close()
                    os.system('cls' if os.name=='nt' else 'clear')    

        if n==2: #jeu entre joeur et ordi
            os.system('cls' if os.name=='nt' else 'clear') 
            player1 = str(input("Joueur 1: "))
            player2 = "ordi"
            print("Bienvenue dans le menu",player1,"et",player2)
            print()

            while c!=6:  #la boucle continuera d'afficher le menu tant que l'on ne chosit pas de "quitter"
                c=menu(n)
                if c==1:
                    os.system('cls' if os.name=='nt' else 'clear') 
                    print("Devinettes. Le but est de deviner le nombre secret de l'autre. Ce nombre est entre le nombre 1 et une borne choisit")
                    print()
                    print()
                    score_joueur1_devinette = score_joueur1_devinette + deviBot(player1,player2)
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')

                if c==2:
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Allumettes. Chacun son tour, vous devez choisir d'enlever soit 1, 2 ou 3 allumettes. Votre but est d'éviter de ramasser la dernière allumette.")
                    print()
                    print()
                    score_joueur1_alumettes = score_joueur1_alumettes + jeu_Alumettes_H_vs_M(player1, score_joueur1_alumettes)
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')
            
                if c==3:
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Morpion. Chacun son tour, les joueurs placent sa marque. Le but du jeu est d'en alligner trois de suite.")
                    print()
                    print()
                    score_joueur1_morpion = score_joueur1_morpion + jeu_morpion_H_vs_M(player1, score_joueur1_morpion)
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')
            
                if c==4:
                    os.system('cls' if os.name=='nt' else 'clear')
                    # Pas besoin de choix comparé à aux dessus. Le joueur ne peux changer que son nom pas celui de l'ordi
                    player1=str(input("Nouveau nom du joueur 1: "))
                    print("Changement effectué")
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')
                                  
                if c==5:    # affichage du score de chaque joueur en fonction du jeu
                    f = open('Score.txt', 'w')  # permet d'ouvrir le fichier pour pouvoir ecrire dedans
                    # écrit le score pour le jeu de devinette
                    f.write('Devinette : ')
                    f.write ('\n')
                    f.write (player1)
                    f.write (': ' + str(score_joueur1_devinette))
                    f.write ('\n')
                    f.write ('\n')
                    # écrit le score pour le jeu du morpions
                    f.write('Morpions : ')
                    f.write ('\n')
                    f.write (player1)
                    f.write (': ' + str(score_joueur1_morpion))
                    f.write ('\n')
                    f.write ('\n')
                    # écrit le score pour le jeu des alumettes
                    f.write('Alumettes : ')
                    f.write ('\n')
                    f.write (player1)
                    f.write (': ' + str(score_joueur1_alumettes))
                    f.write ('\n')
                    f.write ('\n')
                    os.system('cls' if os.name=='nt' else 'clear')  
                    # affichage du fichier scores.txt 
                    print("Tableau des scores : ")
                    print("")
                    f = open('Score.txt','r')
                    # affiche tout le contenue 
                    message = f.read()
                    print(message)
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    f.close()
                    os.system('cls' if os.name=='nt' else 'clear')

        if n==3: # laisser l'ordi jouer avec lui meme
            os.system('cls' if os.name=='nt' else 'clear') 
            print("Bonjour joueur. Veuillez saisir votre prénom: ")
            print()
            player1 = "ordi1"
            player2 = "ordi2"
            print("Bienvenue dans le menu",player1,"et",player2)
            print()

            while c!=4:  #la boucle continuera d'afficher le menu tant que l'on ne chosit pas de "quitter"
                c=menu(n)
                if c==1:
                    os.system('cls' if os.name=='nt' else 'clear') 
                    print("Devinettes. Le but est de deviner le nombre secret de l'autre. Ce nombre est entre le nombre 1 et une borne choisit")
                    print()
                    print()
                    deviOrdi(player1,player2)
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')

                if c==2:
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Allumettes. Chacun son tour, vous devez choisir d'enlever soit 1, 2 ou 3 allumettes. Votre but est d'éviter de ramasser la dernière allumette.")
                    print()
                    print()
                    jeu_Alumettes_M_vs_M()
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')
            
                if c==3:
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Morpion. Chacun son tour, les joueurs placent sa marque. Le but du jeu est d'en alligner trois de suite.")
                    print()
                    print()
                    jeu_morpion_M_vs_M()
                    z=str(input("Taper m pour revenir au menu :")) #permet de temporiser avant de revenir au menu
                    os.system('cls' if os.name=='nt' else 'clear')

    if player1 != " " and player2 != " ":
        print("Au revoir",player1,"et",player2,". Au plaisir de vous revoir.") 
    print("A bientôt !")