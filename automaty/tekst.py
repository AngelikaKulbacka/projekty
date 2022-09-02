import arcade

class Tekst:
    kolor = arcade.color.WHITE

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def rysuj(self):
        arcade.draw_text(self.a, self.b, self.c, self.kolor, 12, width=700, align="center", anchor_x="center", anchor_y="center")