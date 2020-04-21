class buah:
    def __init__(self, jeruk, apel, melon, semangka):
        self.jeruk = jeruk
        self.apel = apel
        self.melon = melon
        self.semangka = semangka

    def hargabuah(self):
        print(f"Hypermart:\n{self.jeruk}\n{self.apel}\n{self.melon}\n{self.semangka}\n")

class sayur:
    def __init__(self, buncis, cabai, kol, jagung):
        self.buncis = buncis
        self.cabai = cabai
        self.kol = kol
        self.jagung = jagung

    def hargasayur(self):
        print(f"Hypermart:\n{self.buncis}\n{self.cabai}\n{self.kol}\n{self.jagung}\n")

class hewani:
    def __init__(self, susu, telur, ayam, cumi):
        self.susu = susu
        self.telur = telur
        self.ayam = ayam
        self.cumi = cumi

    def hargahewani(self):
        print(f"Hypermart:\n{self.susu}\n{self.telur}\n{self.ayam}\n{self.cumi}\n")

class mie:
    def __init__(self, indomiegr, indomierbs, sedaapgr, sedaaprbs):
        self.indomiegr = indomiegr
        self.indomierbs = indomierbs
        self.sedaapgr = sedaapgr
        self.sedaaprbs = sedaaprbs

    def hargamie(self):
        print(f"Hypermart:\n{self.indomiegr}\n{self.indomierbs}\n{self.sedaapgr}\n{self.sedaaprbs}\n")