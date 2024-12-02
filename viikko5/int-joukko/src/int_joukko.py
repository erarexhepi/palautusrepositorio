KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or OLETUSKASVATUS

        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise ValueError("Kapasiteetin on oltava positiivinen kokonaisluku.")
        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko < 0:
            raise ValueError("Kasvatuskoon on oltava positiivinen kokonaisluku.")

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, numero):
        return numero in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, numero):
        if self.kuuluu(numero):
            return False

        if self.alkioiden_lkm == len(self.ljono):
            self._kasvata_listaa()

        self.ljono[self.alkioiden_lkm] = numero
        self.alkioiden_lkm += 1
        return True

    def _kasvata_listaa(self):
        vanha_lista = self.ljono
        self.ljono = self._luo_lista(len(vanha_lista) + self.kasvatuskoko)
        self._kopioi_lista(vanha_lista, self.ljono)

    def poista(self, numero):
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == numero:
                self._siirra_vasemmalle(i)
                self.alkioiden_lkm -= 1
                return True
        return False

    def _siirra_vasemmalle(self, indeksi):
        for i in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0

    def _kopioi_lista(self, alkuperainen, uusi):
        for i in range(len(alkuperainen)):
            uusi[i] = alkuperainen[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdistetty = IntJoukko()
        for numero in a.to_int_list():
            yhdistetty.lisaa(numero)
        for numero in b.to_int_list():
            yhdistetty.lisaa(numero)
        return yhdistetty

    @staticmethod
    def leikkaus(a, b):
        yhteiset = IntJoukko()
        for numero in a.to_int_list():
            if numero in b.to_int_list():
                yhteiset.lisaa(numero)
        return yhteiset

    @staticmethod
    def erotus(a, b):
        erotusjoukko = IntJoukko()
        for numero in a.to_int_list():
            erotusjoukko.lisaa(numero)
        for numero in b.to_int_list():
            erotusjoukko.poista(numero)
        return erotusjoukko

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
