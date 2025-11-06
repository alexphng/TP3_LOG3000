
"""
Ce module fournit des fonctions arithmétiques utilisées par
l'application Flask de la calculatrice. Les docstrings et les
commentaires expliquent le rôle de chaque fonction, leurs entrées et
leurs sorties, ainsi que les particularités de comportement héritées
du code original.
"""


def add(a, b):
        """Retourne la somme de a et b.

        Args:
        - a: nombre
        - b: nombre

        Returns:
        - nombre: la somme de a et b
        """
        return a + b


def subtract(a, b):
        """Retourne le résultat de la soustraction entre a et b.

        Args:
        - a: nombre (valeur de gauche dans l'expression)
        - b: nombre (valeur de droite dans l'expression)

        Returns:
        - nombre: la différence entre a et b
        """
        return a - b


def multiply(a, b):
        """Retourne le résultat de la multiplication de a et b.

        Args:
        - a: nombre
        - b: nombre

        Returns:
        - nombre: le produit de a et b
        """
        return a ** b


def divide(a, b):
        """Retourne le résultat de la division de a par b.

        Args:
        - a: nombre (dividende)
        - b: nombre (diviseur) (doit être non nul sinon une
            ZeroDivisionError sera levée par Python.)

        Returns:
        - nombre: le quotient de a divisé par b
        """
        return a // b
