


from keres import *

"""
Adott 8 különboző méretű korong ...
"""
class PuckSorting(Feladat):

    def __init__(self, k, c):
        self.kezdo = k
        self.cél = c


    def célteszt(self, állapot):
        return állapot == self.cél

    def rákövetkező(self, állapot):
        children = []
        #Operátorok alkalmazása az összes lehetséges következő állapot előállításához
        for amount in range(1, 9):
            children.append(self.__operator(állapot, amount))
        return children


    #Operátors
    def __operator(self, állapot, amount):
        állapot = list(állapot)
        fixed = állapot[amount:]
        raised_and_reversed = állapot[0:amount][::-1]
        állapot = raised_and_reversed + fixed
        return (f"Leemel {amount} darabot és megfordít.", tuple(állapot))


if __name__ == "__main__":


    k = (6,7,3,2,8,5,4,1)
    c = (1,2,3,4,5,6,7,8)

    puck_sorting = PuckSorting(k,c)

    print("Szélességi fakeresés")
    result = szélességi_fakeresés(puck_sorting)
    print(result)
    utam = result.út()
    utam.reverse()
    print(utam)











