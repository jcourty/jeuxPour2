import getpass
import random
import time
from Alumettes_humain_vs_humain import controller

'''
    Fonction qui permet a un joueur d'entrer un nombre et une borne 
    et le second joueur doit deviner le nombre selon les indication de plus ou moins du joueur 1
    j1 et j2 en entrée défini en str, ils reprennent les valeur du main
    retourne un entier-> les points gagnés
 '''
def devinette(j1 : str, j2 : str)->int:
    borne=int
    n=int
    i=int
    reponse=str
    p=int
    
    print(j1,"choisissez le nombre:")
    n = getpass.getpass('Choisez le nombre: ')
    print(j1,"entrez la borne max:")
    borne=int(input())
    print()
 
    while int(n)>borne : #controle que la borne est toujours supérieure au nombre
        print("Borne max trop petite par rapport à votre nombre")
        print(j1,"entrez la borne max:")
        borne=int(input())

    print(j2,"a vous de deviner!")
    print("Le nombre se trouve entre 1 et",borne)

    p=10
    i=int(input("Quelle est votre hypothèse:"))
    controller(i,1,borne)  #borne en tant que bornesup, 1 en tant que borneinf et i en tant que val dans la fonction Verif
    print()
    print("L'hypothèse de",j2,"est",i,".",j1,"quelle est votre réponse??")
    reponse=str(input("g si c'est la bonne réponse, - si le chiffre est plus petit que l'hypothèse et + si le chiffre est plus grand."))

    while reponse!="g" and p>0: #p>0 le jeu s'arrète si le joueur 2 fait plus de 10 hypothèse en plus de la première
        if reponse=="-":
            p=p-1
            print(j2,"le nombre est plus petit")
            i=int(input("retaper une hypothèse:"))
            controller(i,1,borne) #on controle que l'hypothèse est bien entre 0 et la borne
            print("La nouvelle hypothèse de",j2,"est",i,".",j1,"quelle est votre réponse??")
            reponse=str(input("g si c'est la bonne réponse, - si le chiffre est plus petit que l'hypothèse et + si le chiffre est plus grand."))
            print()

        if reponse=="+":
            p=p-1
            print(j2,"le nombre est plus grand")
            i=int(input("retaper une hypothèse:"))
            controller(i,1,borne) #on controle que l'hypothèse est entre 0 et la borne
            print("La nouvelle hypothèse de",j2,"est",i,".",j1,"quelle est votre réponse??")
            reponse=str(input("g si c'est la bonne réponse, - si le chiffre est plus petit que l'hypothèse et + si le chiffre est plus grand."))
            print()

    print("La réponse est : ", n," et vous avez donner : ", i)
    if p==0:
        print("Perdu :(. Vous n'avez pas trouvez.")
    elif int(n) == i: #si le nombre secret et le même que l'hypothèse accépter par le joueur un
        print("Félicitation! Vous avez trouver la bonne réponse!!")
        print(j2,"Vous avez",p,"point(s)")
    else:
        print("Ce n'est pas la bonne reponse ",j1,"à menti donc la partie est annulé !!")
        p = 0 

    return p


'''
    Fonction qui permet a un joueur de jouer avec l'ordinateur.
    Le joueur peut choisir qui fait deviner entre les deux.
    j1 et j2 en entrée défini en str, ils reprennent les valeur du main
    retourne un entier-> les points gagnés
 '''
def deviBot(j1 : str, j2 : str)->int:
    borne=int #la borne max
    n=int  #le nombre a deviner
    i=int #l'hypothèse
    st=int #stocker l'hypothèse
    reponse=str
    p=int #les points
    role=int #pour savoir si qui devine entre les joueurs

    print("1-L'ordi doit trouver le nombre")
    print("2-Le joueur doit trouver le nombre")
    role=int(input("Entrer votre choix :"))
    print()

    if role==1:
        print(j1,"choisissez le nombre:")
        n = getpass.getpass('Choisez le nombre: ')
        print(j1,"entrez la borne max:")
        borne=int(input())
        print()
        while int(n)>borne : #controle que la borne est toujours supérieure au nombre
            print("Borne max trop petite par rapport à votre nombre")
            print(j1,"entrez la borne max:")
            borne=int(input())
        print(j2,"a vous de deviner!")
        print("Le nombre se trouve entre 1 et",borne)

        p=10
        i=random.randint(1,borne)
        st=i
        print("L'hypothèse de",j2,"est",i,".",j1,"quelle est votre réponse??")
        reponse=str(input("g si c'est la bonne réponse, - si le chiffre est plus petit que l'hypothèse et + si le chiffre est plus grand."))
        print()
        while reponse!="g" and p>0: #p>0 le jeu s'arrète si le joueur 2 fait plus de 10 hypothèse en plus de la première
            if reponse=="-":
                p=p-1
                i=random.randint(1,st) #pour que l'ordinateur prenne un nombre plus petit que le premier 
                st=i #on reprend la valeur que l'ordi vient de redonner
                print("La nouvelle hypothèse de",j2,"est",i,".",j1,"quelle est votre réponse??")
                reponse=str(input("g si c'est la bonne réponse, - si le chiffre est plus petit que l'hypothèse et + si le chiffre est plus grand."))
                print()

            if reponse=="+":
                p=p-1
                i=random.randint(st,borne) #pour que l'ordinateur prenne un nombre plus grand que le premier 
                st=i #on reprend la valeur que l'ordi vient de redonner
                controller(i,1,borne) #on controle que l'hypothèse est entre 0 et la borne
                print("La nouvelle hypothèse de",j2,"est",i,".",j1,"quelle est votre réponse??")
                reponse=str(input("g si c'est la bonne réponse, - si le chiffre est plus petit que l'hypothèse et + si le chiffre est plus grand."))
                print()

        print("La réponse est : ", n," et le joueur 2 à donner : ", i)
        if p==0:
            print("Joueur 2 à perdu.")
        elif int(n) == i: #si le nombre secret et le même que l'hypothèse accépter par le joueur un
            print("Félicitation! Joueur 2 à trouver la bonne réponse!!")
            print(j2,"L'ordi gagne",p,"point(s)")
        else:
            print("Ce n'est pas la bonne reponse ",j1,"à menti donc la partie est annulé !!")
            p = 0
    if role==2:
        print(j2,"choisissez le nombre:")
        n =random.randint(1,100)
        print(j1,"entrez la borne max:")
        borne=random.randint(n+1,n+12) #l'ordinateur peut choisir une borne entre une tranche de son nombre+1 et 11 au dessus.
        print()

        #Pas besoin de borne de controle car on oblige l'ordinateur a choisir que des nombre au dessus de son premier choix.
        print(j2,"a choisi son nombre.", j1,"c'est a vous de deviner!")
        print("Le nombre se trouve entre 1 et",borne)

        p=10
        i=int(input("Quelle est votre hypothèse:"))
        controller(i,1,borne)  #borne en tant que bornesup, 1 en tant que borneinf et i en tant que val dans la fonction Verif
        print()
        print("L'hypothèse de",j1,"est",i,".",j2,"quelle est votre réponse??")
        if i>n:
            reponse="-"
        elif i<n:
            reponse="+"
        else:
            reponse="g"
        
        while reponse!="g" and p>0: #p>0 le jeu s'arrète si le joueur 2 fait plus de 10 hypothèse en plus de la première
            if reponse=="-":
                p=p-1
                print(j1,"le nombre est plus petit")
                i=int(input("retaper une hypothèse:"))
                controller(i,1,borne) #on controle que l'hypothèse est bien entre 0 et la borne
                print("La nouvelle hypothèse de",j1,"est",i,".",j2,"quelle est votre réponse??")
                print()
                if i>n:
                    reponse="-"
                elif i<n:
                    reponse="+"
                else:
                    reponse="g"

            if reponse=="+":
                p=p-1
                print(j1,"le nombre est plus grand")
                i=int(input("retaper une hypothèse:"))
                controller(i,1,borne) #on controle que l'hypothèse est entre 0 et la borne
                print("La nouvelle hypothèse de",j1,"est",i,".",j2,"quelle est votre réponse??")
                print()
                if i>n:
                    reponse="-"
                elif i<n:
                    reponse="+"
                else:
                    reponse="g"

        print("La réponse est : ", n," et",j1, "à donner : ", i)
        if p==0:
            print(j1,"à perdu.")
        elif int(n) == i: #si le nombre secret et le même que l'hypothèse accépter par le joueur un
            print("Félicitation!", j1, "à trouver la bonne réponse!!")
            print(j1,"gagne",p,"point(s)")
        else:
            print("Ce n'est pas la bonne reponse ",j2,"à menti donc la partie est annulé !!")
            p = 0

    return p

'''
    Fonction qui permet de laisser jouer l'ordinateur contre lui même.
    Le joueur peut choisir qui fait deviner entre les "deux" ordinateur.
    j1 et j2 en entrée défini en str, ils reprennent les valeur du main
    retourne un entier-> les points gagnés
 '''
def deviOrdi(j1 : str, j2 : str)->int:
    bornemax=int #la borne max
    bornemin=int
    n=int  #le nombre a deviner
    i=int #l'hypothèse
    reponse=str
    p=int #les points
    role=int #pour savoir si qui devine entre les joueurs

    print("Choisir quel joueur fait deviner")
    print("1- Ordi1 donne le nombre et le 2 doit trouver ")
    print("2- Ordi2 donne le nombre et le 1 doit trouver")
    role=int(input("Entrer votre choix :"))
    print()

    if role==1:
        j1="Ordi1"
        j2="Ordi2"
    elif role==2:
        j1="Ordi2"
        j2="Ordi1"
        
    print(j1,"choisi son nombre:")
    n =random.randint(1,100)
    print(j1,"choisi la borne max:")
    bornemax=random.randint(n+1,n+12) #l'ordinateur peut choisir une borne entre une tranche de son nombre+1 et 11 au dessus.
    bornemin=1


    #Pas besoin de borne de controle car on oblige l'ordinateur à choisir que des nombre au dessus de son premier choix.
    print(j1,"a choisi son nombre. A",j2,"de deviner!")
    print()
    print("Le nombre se trouve entre",bornemin,"et",bornemax)
    time.sleep(2)

    
    i=random.randint(bornemin,bornemax)
    print()
    print("L'hypothèse de", j2,"est",i,".",j1,",quelle est votre réponse??")
    time.sleep(2)
    if i>n:
        reponse="-"
    elif i<n:
        reponse="+"
    else:
        reponse="g"

    p=10
    while reponse!="g": #p>0 le jeu s'arrète si le joueur 2 fait plus de 10 hypothèse en plus de la première
        if reponse=="-":
            p=p-1
            print("le nombre est plus petit")
            time.sleep(2)
            print()
            bornemax=i-1
            i=random.randint(bornemin,bornemax)
            print("L'hypothèse de", j2,"est",i,".",j1,",quelle est votre réponse??")
            time.sleep(2)
            if i>n:
                reponse="-"
            elif i<n:
                reponse="+"
            else:
                reponse="g"

        if reponse=="+":
            p=p-1
            print("le nombre est plus grand")
            time.sleep(2)
            print()
            bornemin=i+1
            i=random.randint(bornemin,bornemax)
            print("L'hypothèse de", j2,"est",i,".",j1,",quelle est votre réponse??")
            time.sleep(2)
            if i>n:
                reponse="-"
            elif i<n:
                reponse="+"
            else:
                reponse="g"
            
        if p==0:
            reponse="g"
    if p==0:
        print(j2,"à perdu. Ses points sont à 0.")
        print("Le nombre qu'il fallait trouver etait :",n)
    else:
        print("La réponse est : ", n," et",j2, "à donner : ", i)
        print("Félicitation!", j2, "à trouver la bonne réponse!!")
        print(j2,"gagne",p,"point(s)")
    return p