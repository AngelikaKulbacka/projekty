import arcade


class Kolko:
    kolor = arcade.color.WHITE

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def rysuj(self):
        arcade.draw_circle_outline(self.x, self.y, self.r, self.kolor)

    def ustaw_aktywny(self):
        self.kolor = arcade.color.AO

    def ustaw_nieaktywny(self):
        self.kolor = arcade.color.WHITE

    def ustawA(self, a, strzalkaA):
        self.a = a
        self.strzalkaA = strzalkaA

    def ustawB(self, b, strzalkaB):
        self.b = b
        self.strzalkaB = strzalkaB

    def przejdzDalej(self, literka):
        self.ustaw_nieaktywny()
        if literka=='a':
            self.a.ustaw_aktywny()
            self.strzalkaA.ustaw_aktywny()
            return self.a
        else:
            self.b.ustaw_aktywny()
            self.strzalkaB.ustaw_aktywny()
            return self.b

class finalKolko(Kolko):
    def rysuj(self):
        arcade.draw_circle_outline(self.x, self.y, self.r, self.kolor)
        arcade.draw_circle_outline(self.x, self.y, self.r-5, self.kolor)