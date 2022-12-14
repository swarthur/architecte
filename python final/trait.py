import turtle

def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.penup()

if __name__ == '__main__':
    # dessine deux traits
    trait(-50,-50,100,100)
    trait(0, 100, 0, -100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
