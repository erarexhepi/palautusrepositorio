HINTA = 5


class Kassapaate:
    def __init__(self):
        self.__myytyja_lounaita = 0

    def lataa(self, maksukortti, summa):
        if summa > 0:
            maksukortti.lataa(summa)

    def osta_lounas(self, maksukortti):
        if maksukortti.saldo() >= HINTA:
            maksukortti.osta(HINTA)