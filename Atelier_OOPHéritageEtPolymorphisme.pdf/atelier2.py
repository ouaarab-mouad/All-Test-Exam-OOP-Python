""" partie 1 :  ----------------------------------------------------------------------------------------------------"""
import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x=x
        self.__y=y
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance_from_xy(self, x, y):
        return math.sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


# exemple d'execution : 
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))


""" partie 2 :  -------------------------------------------------------------------------------------------------------"""

class TriangleError(Exception):
    pass

class Triangle:
    def __init__(self, point1, point2, point3):
        # Vérification si les points forment un triangle
        if self._is_triangle(point1, point2, point3):
            self.__points = [point1, point2, point3]
        else:
            raise TriangleError("Les points donnés ne forment pas un triangle valide.")

    def _is_triangle(self, point1, point2, point3):
        # Vérification de l'inégalité triangulaire
        # (la somme de deux côtés est toujours supérieure au troisième côté)
        side1 = point1.distance_from_point(point2)
        side2 = point2.distance_from_point(point3)
        side3 = point3.distance_from_point(point1)
        return (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2)

    def perimeter(self):
        perimeter = 0
        for i in range(3):
            # Calcul de la distance entre chaque paire de points
            perimeter += self.__points[i].distance_from_point(self.__points[(i+1) % 3])
        return perimeter

# Exemple d'utilisation
try:
    # Création des points
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(0, 3)

    # Création du triangle
    triangle = Triangle(p1, p2, p3)

    # Calcul du périmètre
    print("Périmètre du triangle:", triangle.perimeter())  # Output: Périmètre du triangle: 12.0
except TriangleError as e:
    print(e)

