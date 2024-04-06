from keres import *
from itertools import product

class ChessKnight(Feladat):

    def __init__(self, k, c):
        self.denied = [(0, 0), (7, 0), (0, 7), (7, 7)]
        self.kezdo = k if k not in self.denied and 0<=k[0]<8 and 0<=k[1]<8 else (0,1)
        self.cél = c
        self.table = [["O" for x in range(0,8)] for y in range(0,8)]
        self.table_states = []

    def célteszt(self, állapot):
        return állapot == self.cél

    def rákövetkező(self, állapot):


        if állapot in self.denied:
            return []
        self.set_table(állapot)
        return self.generate_knight_moves(current_position=list(állapot))


    def generate_knight_moves(self, current_position):

        x, y, visited = current_position
        moves = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
        moves = [(f"Lépek-->({x},{y})",(x, y, False)) for x, y in moves if x >= 0 and y >= 0 and x < 8 and y < 8 and (x,y) not in self.denied]
        return moves


    def set_table(self, állapot):
        x,y,visited = állapot

        current_table_state = self.table
        current_table_state[x][y] = "X"

        self.table = current_table_state
        self.table_states.append(current_table_state)



    def print_table(self):
        for x in self.table:
            print(x)


    def print_table_states(self):
        for x in self.table_states:
            for y in x:
                print(y)
            print("\n")


if __name__ == "__main__":
    chess_knight = ChessKnight((0,1, True), (0,1,False));


    print("Mélységi fakeresés")
    result = mélységi_fakeresés(chess_knight)
    utam = result.út()
    utam.reverse()
    print(utam)

    chess_knight = ChessKnight((0, 1, True), (0, 1, False));
    chess_knight.print_table()
    print("Szélességi gráfkeresés")
    result = szélességi_gráfkeresés(chess_knight)
    utam = result.út()
    utam.reverse()
    print(utam)


    #chess_knight.print_table_states()

    with open("states.txt", "w") as file:
        for state in chess_knight.table_states:
            for row in state:
                string_list = "[" + ' '.join(str(x) for x in row) + "]\n"
                file.write(string_list)

            file.write("\n\n")


    file.close()

