import arcade
from kolko import Kolko, finalKolko
from strzalka import Strzalka
from zaokrStrzalka import zaokr
from tekst import Tekst
from odpowiedz import Odp

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    czas = 0
    aktywny_indeks = 0
    koniec = False

    #słowo, które będziemy sprawdzać
    slowo = "aaaaabba"

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.kolka = [Kolko(100,500,20), Kolko(300,500,20), Kolko(500,500,20), finalKolko(700,500,20)]
        #self.mini = Kolko(700,500,15)
        self.kolka[self.aktywny_indeks].ustaw_aktywny()
        self.aktywne_kolko = self.kolka[0]

        self.strzalka = [Strzalka(120,500,260,500,260,495,280,500,260,505,260,500),
                         Strzalka(320,500,460,500,460,495,480,500,460,505,460,500),
                         Strzalka(520,500,660,500,660,495,680,500,660,505,660,500),
                         zaokr(720,500,-50,-80,-335,-45, 700,520,705,530,695,530,700,520)]
        self.strzalka[self.aktywny_indeks].ustaw_nieaktywny()

        self.zaokrStrzalka = [zaokr(80,500,60,60,45,315, 100, 480, 105, 470, 95, 470, 100, 480),
                              zaokr(200, 480, 200, 100, 185, 360, 100, 480, 105, 470, 95, 470, 100, 480),
                              zaokr(300, 480, 400, 200, 185, 360, 100, 480, 105, 470, 95, 470, 100, 480),
                              zaokr(400,480,600,300,185,360, 100,480,105,470,95,470,100,480)]
        self.zaokrStrzalka[self.aktywny_indeks].ustaw_nieaktywny()

        for k, kolko in enumerate(self.kolka):
            if k==3:
                kolko.ustawA(kolko, self.strzalka[k])
            else:
                kolko.ustawA(self.kolka[k + 1], self.strzalka[k])

        for k, kolko in enumerate(self.kolka):
            kolko.ustawB(self.kolka[0], self.zaokrStrzalka[k])

        self.odp1 = Odp("Słowo jest akceptowalne", 170)
        self.odp2 = Odp("Slowo nie jest akceptowalne", 150)

        self.tekst = [Tekst("q0", 100, 500), Tekst("q1", 300, 500), Tekst("q2", 500, 500), Tekst("q4", 700, 500),
                      Tekst("a", 200, 510), Tekst("a", 400, 510), Tekst("a", 600, 510),
                      Tekst("b", 200, 420), Tekst("b", 300, 370), Tekst("b", 400, 320), Tekst("b", 40, 500),
                      Tekst("Automat skończony deterministyczny, którego słowa są zakończone sekwencją aaa.", 400, 570),
                      Tekst("Sprawdzane słowo:  "+self.slowo, 400, 220)]

    def on_draw(self):
        for k in self.kolka:
            k.rysuj()
        for s in self.strzalka:
            s.rysuj()
        for z in self.zaokrStrzalka:
            z.rysuj()
        for t in self.tekst:
            t.rysuj()
        self.odp1.rysuj()
        self.odp2.rysuj()

    def on_update(self, delta_time):
        self.czas = self.czas + delta_time
        if self.koniec:
            self.czas = 0
        if self.czas>=2:
            self.wylaczStrzalki()
            self.aktywne_kolko = self.aktywne_kolko.przejdzDalej(self.slowo[self.aktywny_indeks])
            self.aktywny_indeks += 1
            if self.aktywny_indeks==len(self.slowo):
                self.koniec = True
                if isinstance(self.aktywne_kolko, finalKolko):
                    self.odp1.aktywny()
                else:
                    self.odp2.aktywny()
            self.czas = 0

    def wylaczStrzalki(self):
        for s in self.strzalka:
            s.ustaw_nieaktywny()
        for z in self.zaokrStrzalka:
            z.ustaw_nieaktywny()



def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()