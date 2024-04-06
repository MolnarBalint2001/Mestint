

from keres import *
class Hanoi(Feladat):
    def __init__(self, k, c):
        self.kezdo = k
        self.cél = c
    def célteszt(self, állapot):
        return állapot == self.cél
    def rákövetkező(self, állapot):
        gyerek_cs = list()
        for melyiket in range(0,3):
            for hova in ['P', 'Q', 'R']:
                flag = True     # feltételezzük, hogy az operátor alkalmazható
                # az operátor alkalmazási előfeltételének a vizsgálata
                if állapot[melyiket] != hova:
                    for i in range(0, melyiket):
                        if állapot[i] != állapot[melyiket] and állapot[i] != hova:
                            flag = True
                        else:
                            flag = False
                            break
                else:
                    flag = False
                # az operátor alkalmazási függvénye
                if flag:
                    tmp = list(állapot)
                    tmp[melyiket] = hova
                    e = tuple(tmp)
                    gyerek_cs.append((" "+str(melyiket)+"-->"+hova, e))
        return gyerek_cs

if __name__ == "__main__":
    ha = Hanoi(('P', 'P', 'P'), ('R', 'R', 'R'))
    print("Szélességi fakeresés")
    result = szélességi_fakeresés(ha)
    utam = result.út()
    utam.reverse()
    print(utam)
