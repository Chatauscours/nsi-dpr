import turtle
# déplace la tortue aux coordonnées
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
# orientation intiale de la tête :
#vers la droite de l’écran
turtle.setheading(0)
turtle.hideturtle() # on cache la tortue
turtle.speed(0) # on accélère la tortue
turtle.color("black","red")
turtle.pensize(1)

def affichage(position, unite_base, trou_ici = False):
    turtle.pendown()
    # assert position >= 0 and position <4, "erreur position trou, nombre incorrect" #Pas besoin
    turtle.setheading(90*position + 90) #90 pour nord, 180 pour ouest, 270 pour sud; 360 pour est
    turtle.forward(unite_base)
    turtle.right(90)
    turtle.forward(unite_base)
    for i in range (2):
        turtle.right(90)
        turtle.forward(unite_base)
        turtle.forward(unite_base)
    turtle.right(90)
    turtle.forward(unite_base)
    turtle.right(90)
    turtle.forward(unite_base)
    if trou_ici == True:
        turtle.setheading(90*position + 90)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(unite_base)
            turtle.left(90)
        turtle.end_fill()
    turtle.penup()

def solution(taille_totale, trou_x, trou_y, taille_base,trou_ici = True, chemin = []):
    trou_droite = False
    trou_bas = False

    if trou_ici == True:
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
        trou_carre = 42 #Pour que personne ne pense qu'il soit ici
    
    print(taille_totale)
    if taille_totale == 2 and trou_ici == True: #Si on est dans le cas de base ET le trou est ici
        affichage(trou_carre, taille_base, trou_ici)
    
    elif taille_totale == 2: #Si on est dans le cas de base ET le trou n'est PAS ici
        if len(chemin) < 2:
            affichage(int(chemin[-1])+2, taille_base)
        elif int(chemin[-1]) - int(chemin[-2]) == 2 or int(chemin[-1]) - int(chemin[-2]) == -2 and trou_ici == False: ### A MODIFIER STAT
            #Si ils sont de cotés opposés
            affichage(int(chemin[-1]),taille_base)
        else:
            affichage(int(chemin[-1])+2,taille_base)
    
    else: #Si on n'est pas dans le cas de base
        solution(taille_totale/2, trou_x, trou_y, taille_base, trou_carre == 0, chemin + [("0",trou_carre == 0)])
        turtle.setheading(270)
        turtle.forward(taille_base*taille_totale/2)
        solution(taille_totale/2, trou_x, trou_y - taille_totale/2, taille_base, trou_carre == 1, chemin + [("1",trou_carre == 1)])
        turtle.setheading(0)
        turtle.forward(taille_base*taille_totale/2)
        solution(taille_totale/2, trou_x - taille_totale/2, trou_y - taille_totale/2, taille_base, trou_carre == 2, chemin + [("2",trou_carre == 2)])
        turtle.setheading(90)
        turtle.forward(taille_base*taille_totale/2)
        solution(taille_totale/2, trou_x - taille_totale/2, trou_y, taille_base, trou_carre == 3, chemin + [("3",trou_carre == 3)])
        turtle.setheading(180)
        turtle.forward(taille_base*taille_totale/2)
    

def demarrage():
    n = 3
    x = 1
    y = 2
    base = 50
    #à modifier le code au dessus en imput

    total = 2**n
    solution(total, x, y, base)



### -------- ###
demarrage()

continuer=True
while continuer==True:
    if turtle.exitonclick():
        turtle.bye()
        continuer=False
