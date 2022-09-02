import arcade

class Odp:
    kolor = arcade.color.BLACK

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def rysuj(self):
        arcade.draw_text(self.a, 400, self.b, self.kolor, 12, width=700, align="center", anchor_x="center", anchor_y="center")

    def aktywny(self):
        self.kolor = arcade.color.WHITE