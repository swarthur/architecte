import turtle
from random import randrange,randint
from pave import pave

def ciel_nuage(h_nuage:list,heure:int,tridi:float=None):
    """Dessine des nuages

    Args:
        h_nuage (list): Contient l'ordonnée max et min où apparaiteront les nuages
        tridi (float, optional): Angle de fuite de la perspective cavalière. None par défaut.
    """
    if heure < 8 or heure > 20: # Change la couleur des nuages en fonction de l'heure
        c_nuage = "dim grey"
    else:
        c_nuage = "light grey"
    nb_nuages= randint(0,20) # Détermine aléatoirement le nombre de nuages à dessiner
    for nuage in range(nb_nuages): # Boucle afin de dessiner chaque nuage à un emplacement aléatoire
        y_nuage = randrange(h_nuage[0],h_nuage[1]) # Ordonnée du nuage (aléatoire)
        x_nuage = randrange(-400,400) # Abscisse du nuage (aléatoire)
        pave(x_nuage,y_nuage,45,30,10,tridi,c_nuage) # Dessine le nuage aux coordonnées ci-dessus de dimensions 45x30x10

def ciel_etoile():
    """Dessine des étoiles
    """
    turtle.pencolor("white") # Couleur du stylo en blanc
    nb_etoiles = randint(5,50) # Détermine aléatoirement le nombre d'étoiles à dessiner
    for etoile in range(nb_etoiles): # Boucle pour dessiner chaque étoile à un emplacement aléatoire
        pave(randint(-400,400),randint(-200,300),1,1,0,None,"white") #Dessine une étoile aléatoirement
    turtle.pencolor("black") # Couleur du stylo en noir


if __name__ == "__main__":
    turtle.bgcolor("sky blue")
    ciel_etoile()
    ciel_nuage([150,280],45)
    turtle.exitonclick()