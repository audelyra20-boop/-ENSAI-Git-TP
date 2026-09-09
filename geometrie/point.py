from __future__ import annotations
import math


class Point:

    """
    Classe abstraite représentant un Point.

    Attributes:
        x(float) : coordonée en abscisse
        y(float) : coordonnée en ordonnee

    Methodes:
    r(): coordonnée polaire, rayon
    t(): cooordonnée polaire, angle
    distance(Point p): distance entre deux points
    homothetie(k): homothetie de rapport k
    translation(dx, dy): translation de dx en x et dy en x
    
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def r(self):
        return math.sqrt(self.x**2 + self.y**2)

    def t(self):
        if self.x == 0:
            return "Angle non défini"

        return math.atan2(self.y, self.x)

    def __str__(self):
        return f"({self.x},{self.y})"

    def distance(self, p: Point) -> float:
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __eq__(self, autre_point: Point) -> bool:
        return self.x == autre_point.x and self.y == autre_point.y

    def homothetie(self, k):
        self.x *= k
        self.y *= k

    def translation(self, dx, dy):
        self.x += dx
        self.y += dy


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1)
    print(f"Distance entre p1 et p2 : {p1.distance(p2)}")
    print(f"p1 est égal à p2 : {p1 == p2}")
