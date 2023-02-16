class Jatekos:
    def __init__(self, r:str):
        v = r.strip().split(';')
        self.nev:str = v[0]
        self.mag:int = int(v[1])
        self.suly:int = int(v[2])
        self.palyan:int = int(v[3])
        self.perc:int = int(v[4])
        self.gol:int = int(v[5])
        self.sarga:int = int(v[6])
        self.piros:int = int(v[7])