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

unite_base = 50

def affichage(position, trou_ici = False):
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

def solution(taille_totale, trou_x, trou_y, taille_base,trou_ici = True, chemin = ""):
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
        elif trou_droite == False and trou_bas == False:
            trou_carre = 1
        else:
            trou_carre = 2
    print(taille_totale)
    if taille_totale == 2 and trou_ici == True:
        affichage(trou_carre, trou_ici)
    elif taille_totale == 2: 
        if int(chemin[-1]) - int(chemin[-2]) == 2 or int(chemin[-1]) - int(chemin[-2]) == -2: 
            #Si ils sont de cotés opposés
            affichage(chemin[-1])
        else:
            affichage(chemin[-1]+2)
    else:
        solution(taille_totale/2, trou_x, trou_y, taille_base, trou_ici == 0, chemin + "0")
        solution(taille_totale/2, trou_x, trou_y - taille_totale/2, taille_base, trou_ici == 1, chemin + "1")
        solution(taille_totale/2, trou_x - taille_totale/2, trou_y - taille_totale/2, taille_base, trou_ici == 2, chemin + "2")
        solution(taille_totale/2, trou_x - taille_totale/2, trou_y, taille_base, trou_ici == 3, chemin + "3")
    

def demarrage():
    n = 2
    x = 2
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