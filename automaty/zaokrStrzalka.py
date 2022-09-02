import arcade

class zaokr:
    kolor = arcade.color.WHITE

    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n


    def rysuj(self):
        arcade.draw_arc_outline(self.a, self.b, self.c, self.d,
                                self.kolor, self.e, self.f)
        point_list = ((self.g, self.h),
                      (self.i, self.j),
                      (self.k, self.l),
                      (self.m, self.n))
        arcade.draw_line_strip(point_list, self.kolor, 0.5)

    def ustaw_aktywny(self):
        self.kolor = arcade.color.AO

    def ustaw_nieaktywny(self):
        self.kolor = arcade.color.WHITE