#!/usr/bin/python3
"""
Module qui définit une classe Square représentant un carré.

La classe permet de créer un carré avec une taille de côté
donnée, en effectuant des validations,
et fournit une méthode pour calculer l'aire du carré.

Classe:
    Square: Classe représentant un carré avec un côté de taille donnée.

Attributs:
    size (int): Taille du côté du carré, doit être un entier
    positif ou égal à zéro.

Méthodes:
    __init__(size=0): Initialise un carré avec une taille donnée et
    effectue des validations.
    area(): Calcule et retourne l'aire du carré.
"""


class Square:
    """
    Classe représentant un carré avec une taille de côté donnée.

    Attributs:
        __size (int): Taille du côté du carré, doit être un entier >= 0.

    Méthodes:
        __init__(size=0): Initialise un carré avec une taille de côté et
        effectue les validations.
        area(): Calcule et retourne l'aire du carré.
    """

    def __init__(self, size=0):
        """
        Initialise un carré avec une taille donnée.

        Paramètres:
            size (int): Taille du côté du carré. Par défaut, 0.

        Lève:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Retourne:
            int: L'aire du carré, calculée comme le carré de la taille du côté.

        Lève:
            ValueError: Si la taille du carré est invalide (inférieure à 0).
        """
        return self.__size ** 2
