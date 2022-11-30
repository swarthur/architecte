import turtle
from rectangle import rectangle
from sol import sol

def porte(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte de 30 pixels de large pour 50 pixels de hauteur
    '''
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    rectangle(x,y,30,50)
    turtle.end_fill()



if __name__ == '__main__':
    sol(0)
    porte(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()