import turtle
import random
# On prépare la tortue pour tracer la figure
turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
turtle.setheading(0)
turtle.hideturtle()
turtle.speed(0)
turtle.color("black","red")
turtle.pensize(1)

def affichage(position, unite_base, trou_ici = False):
    '''Cette fonction sert à afficher le carré 2*2, de base. 
    Elle prend en paramètres l'orientation du carré sous forme d'entier, la taille de la moitié du coté d'un carré en pixels,
    ainsi qu'un booléen représentant si le trou est dans ce carré ou pas (True si oui, False sinon)'''
    turtle.pendown()
    # assert position >= 0 and position <4, "erreur position trou, nombre incorrect" #Pas besoin
    turtle.setheading(90*position + 90) #90 pour nord, 180 pour ouest, 270 pour sud; 360 pour est
    turtle.forward(unite_base)
    turtle.right(90)
    turtle.forward(unite_base)
    for i in range (2): # Une boucle for pour raccourcir le code sur le traçage de l'angle externe
        turtle.right(90)
        turtle.forward(unite_base)
        turtle.forward(unite_base)
    turtle.right(90)
    turtle.forward(unite_base)
    turtle.right(90)
    turtle.forward(unite_base)
    if trou_ici == True: # Si le trou est dans CE carré 2*2, alors on le colorie en rouge
        turtle.setheading(90*position + 90)
        turtle.begin_fill()
        for i in range(4): # Une boucle for pour raccourcir le code du traçage du carré
            turtle.forward(unite_base)
            turtle.left(90)
        turtle.end_fill()
    turtle.penup()

def solution(taille_totale, trou_x, trou_y, taille_base,trou_ici = True, chemin = []):
    '''Cette fonction sert à résoudre l'entièreté de la figure.
    Elle prends en paramètres la taille totale de la figure, les coordonnées X et Y du trou,
    et la taille de la moitié du coté d'un carré de base 2*2 en pixels,
    ainsi qu'un booléan représentant la présence du trou dans cette figure et le chemin,
    les deux derniers utilisés uniquement durant la récursion de cette fonction et ne doivent pas être altérées manuellement '''

    trou_droite = False
    trou_bas = False

    if trou_ici == True: # Si on a toujours le trou dans notre carré, on supprime le chemin précédent, afin de se recentrer sur le trou
        chemin = []

    if trou_ici == True: # Si on a toujours le trou dans notre carré, on determine le quart dans lequel il l'est
        if taille_totale/2 <= trou_x:
            trou_droite = True
        if taille_totale/2 <= trou_y:
            trou_bas = True
        if trou_droite == False and trou_bas == False:
            trou_carre = 0
        elif trou_droite == True and trou_bas == False:
            trou_carre = 3
        elif trou_droite == False and trou_bas == True:
            trou_carre = 1
        else:
            trou_carre = 2
    else:
        trou_carre = 42 # Pour que personne ne pense que le trou est ici, si il ne l'est pas
    
    if taille_totale == 2 and trou_ici == True: # Si on est dans le cas de base ET le trou est ici
        affichage(trou_carre, taille_base, trou_ici)
    
    elif taille_totale == 2: # Si on est dans le cas de base ET le trou n'est PAS ici
        if len(chemin) < 2: # Soit la figure est trop petite pour avoir une nécessité d'établir les diagonales
            affichage(chemin[-1][0]+2, taille_base)
        else:
            oppose = True # Soit on établit sur quelle diagonale principale se situe le L que l'on veut dessiner
            final = chemin[-1] # A partir des diagonales établies, on tourne donc la figure dans la direction nécessaire
            precedent = chemin[-1]
            for i in range (len(chemin)):
                if (final[0] + chemin[-(i+1)][0])%2 != 0: 
                    affichage(precedent[0]+2,taille_base)
                    oppose = False
                    break
                precedent = chemin[-(i+1)]
            
            if oppose == True: # Si la liste du chemin a été épuisée et que la diagonale principale n'a pas été étable,
            # alors on est sur la diagonale principale d'un des quarts initiaux
                affichage(chemin[0][0]+2,taille_base)
    
    else: #Si on n'est pas dans le cas de base, alors on récurse avant que le cas de base soit trouvé
        solution(taille_totale/2, trou_x, trou_y, taille_base, trou_carre == 0, chemin + [(0,trou_carre == 0)])
        turtle.setheading(270)
        turtle.forward(taille_base*taille_totale/2)
        solution(taille_totale/2, trou_x, trou_y - taille_totale/2, taille_base, trou_carre == 1, chemin + [(1,trou_carre == 1)])
        turtle.setheading(0)
        turtle.forward(taille_base*taille_totale/2)
        solution(taille_totale/2, trou_x - taille_totale/2, trou_y - taille_totale/2, taille_base, trou_carre == 2, chemin + [(2,trou_carre == 2)])
        turtle.setheading(90)
        turtle.forward(taille_base*taille_totale/2)
        solution(taille_totale/2, trou_x - taille_totale/2, trou_y, taille_base, trou_carre == 3, chemin + [(3,trou_carre == 3)])
        turtle.setheading(180)
        turtle.forward(taille_base*taille_totale/2)
        # Obligé de répeter les commandes 4 fois à cause des limitations turtle sur la méthode setheading()
            
    

def demarrage():
    '''Cette fonction sert à initier le programme à l'aide d'une interface console avec l'utilisateur'''
    print("Lors du démarrage du programme, l'utilisateur peut toujour entrez le mot 'abort' afin d'interrompre le démarrage.")
    # Pour laisser un chemin de sortie, toujours, avec les boucles while que l'on aura
    t_bon = False
    while t_bon == False: # Boucle while pour forcer l'utilisateur à faire un choix correct
        taille = input("Quelle voulez vous que la valeur de n soit, avec la taille du coté du carré de la figure égale à 2**n? ...    ")
        if taille == "abort":
            turtle.bye()
            return "Interrompu par l'utilisateur"
        elif taille.isnumeric() != True or float(taille)//1 != float(taille): # On vérifie ici si taille est bien un entier
            print("!!! n doit être un entier positif !!!")
        elif int(taille) > 4: # Un petit message d'avertissement, car la tortue est lente
            att = input("Attention! Pour n supérieur à 4 il risque d'avoir des temps d'executions considérables. Continuer? Y/N ...   ")
            if att == "Y" or att == "y":
                total = 2**int(taille)
                t_bon = True # Si tout est bon, on sort de la boucle
            elif att == "abort":
                turtle.bye()
                return "Interrompu par l'utilisateur"
            elif att != "N" or att != "n":
                print("Réponse incohérante, considérée comme un non.") # Pour éviter une autre boucle while agressive
        else:
            total = 2**int(taille)
            t_bon = True # Si tout est bon, on sort de la boucle
            
        
    rand = input("Voulez vous customiser les coordonnées du trou? Y/N ...    ")
    if rand == 'abort':
        turtle.bye()
        return "Interrompu par l'utilisateur"
    elif rand == "N" or rand == "n":
        x = random.randint(0,total-1) # On va utiliser la bibliotheque random pour choisir le coordonnées aléatoirement
        y = random.randint(0,total-1)
    elif rand == "Y" or rand == "y":
        print("Les coordonnées sont définies de haut en bas et droite à gauche, en commençant par 0 et en se terminant par 2**n-1")
        x_bon = False
        while x_bon == False: # Boucle while pour forcer l'utilisateur à faire un choix correct
            x = input("Quelle coordonnée X du trou voulez vous? ...    ")
            if x == 'abort':
                turtle.bye()
                return "Interrompu par l'utilisateur"
            elif x.isnumeric() != True or float(x)//1 != float(x): # On vérifie ici si x est bien un entier
                print("!!! La coordonnée x doit être un entier !!!")
            elif int(x) < 0:
                print("!!! La coordonnée x doit être positive !!!")
            elif int(x) > total-1: # Car les coordonnées commencent à 0
                print("!!! La coordonnée x doit être inférieure à 2**n-1, soit disant: ", total-1, " !!!")
            else:
                x_bon = True
        
        y_bon = False
        while y_bon == False: # Boucle while pour forcer l'utilisateur à faire un choix correct
            y = input("Quelle coordonnée Y du trou voulez vous? ...    ")
            if y == 'abort':
                turtle.bye()
                return "Interrompu par l'utilisateur"
            elif y.isnumeric() != True or float(y)//1 != float(y): # On vérifie ici si y est bien un entier
                print("!!! La coordonnée y doit être un entier positif !!!")
            elif int(y) > total-1:
                print("!!! La coordonnée y doit être inférieure à 2**n-1, soit disant: ", total-1, " !!!")
            else:
                y_bon = True
    else:
        print("Réponse incohérante, considérée comme un non.") # Pour éviter une autre boucle while
        x = random.randint(0,total-1)
        y = random.randint(0,total-1)
    
    b_bon = False
    while b_bon == False: # Boucle while pour forcer l'utilisateur à faire un choix correct
        base = input("Quelle taille en pixels voulez vous de chaque partie de la figure (recommendé 20 pour n inférieur à 5) ...    ")
        # A vrai dire, c'est la taille de la moitié d'un carré basique 2*2, donc d'un mini carré 1*1 consitituant les 2*2...
        if base == 'abort':
            turtle.bye()
            return "Interrompu par l'utilisateur"
        elif base.isnumeric() != True or float(base)//1 != float(base): #On vérifie ici si base est bien un entier
            print("!!! Le nombre de pixels doit être un entier positif !!!")
        else:
            b_bon = True
    
    solution(total, int(x), int(y), int(base)) # Et on lance la solution avec les donnés entrées par l'utilisateur



### -------- ###

demarrage() # On lance le programme

continuer=True # Assure la fermeture de turtle
while continuer==True:
    if turtle.exitonclick():
        turtle.bye()
        continuer=False