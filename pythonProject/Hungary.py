

from keres import *


"""
7.feladat
Az ábrán látható tíz mezőből álló táblára három zöld és 3 piros elem...


"""

class Hungary(Feladat):



    def __init__(self, k, c):
        self.kezdo = k
        self.cél = c
        self.denied = [(1,0), (1,2), (2,2), (3,0), (3,2)]

    def célteszt(self, állapot):
        return állapot == self.cél

    def rákövetkező(self, állapot):
        children = []
        ps = []
        for index, state in enumerate(állapot):
            possible_moves = self.generate_possible_moves(state[1], állapot)
            #print(possible_moves)
            print("state", állapot)

            if len(possible_moves) > 0:
                results = self.__operator(állapot[:], possible_moves, index)
            else:
                pass
                #print(állapot)
            #ps.append(results)


        #for x in ps:
         #   for row in x:
         #       for y in row:
        #          print(y)
        #       print()
        return children


    """
        Operátor: Mozdít
        O = üres    
        " " = nem lehet lépni
        P = piros
        Z = zöld
        Akkor alkalmazható ha a következő mező üres illetve nem gátolják egyéb négyzetek a mozgásban
    """
    def __operator(self, állapot, move, index):
        results = []
        current_state = állapot[:]

        current_state[index][1] = move[0]
        #print(current_state)



        return results



    def generate_possible_moves(self, from_position, állapot):
        x,y = from_position
        return list(filter(lambda pos: 0<=pos[0]<5 and 0<=pos[1]<3 and pos not in self.denied and pos not in list(map(lambda x: x[1], állapot[:])), [(x-1,y),(x+1,y),(x, y-1),(x, y+1)]))



def mellekhatas(number):
    number = 2


if __name__ == "__main__" :

    number = 10
    print(number)
    mellekhatas(2)
    print(number)

    k = (
        ["Z", (0,0)],
        ["Z", (0,1)],
        ["Z", (0,2)],

        ["P", (4, 0)],
        ["P", (4, 1)],
        ["P", (4, 2)],
    )
    c = (
        ["P", (0, 0)],
        ["P", (0, 1)],
        ["P", (0, 2)],

        ("Z", (4, 0)),
        ("Z", (4, 1)),
        ("Z", (4, 2)),

    )

    hungary = Hungary(k,c)


    result = szélességi_gráfkeresés(hungary)
    print(result)
    utam = result.út()
    utam.reverse()
    print(utam)



