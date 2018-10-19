import random

tiles = dict()
empty_temp = dict()
mines = list()
mine_num = 10
rows = 10
cols = 10
known_tiles = set()


class Tile:
    def __init__(self, coordinate, attr=' ', icon=' ', revealed=False):
        self.coordinate_x, self.coordinate_y = coordinate
        self.icon = icon
        self.attr = attr
        self.outer = list()
        self.revealed = revealed

    def get_outer_tiles(self):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if 0 <= self.coordinate_x + i < cols and 0 <= self.coordinate_y + j < rows:
                    if (self.coordinate_x + i, self.coordinate_y + j) != (self.coordinate_x, self.coordinate_y):
                        self.outer.append((self.coordinate_x + i, self.coordinate_y + j))
        return self.outer

    def reveal(self):
        self.icon = self.attr
        self.revealed = True

    def get_coordinates(self):
        return self.coordinate_x, self.coordinate_y

    def get_icon(self):
        return self.icon

    def get_attr(self):
        return self.attr

    def place_mine(self):
        self.attr = '*'

    def is_mine(self):
        return self.get_coordinates() in mines

    def configure_attr(self):
        if not self.is_mine():
            temp = 0
            for i in self.get_outer_tiles():
                if i in mines:
                    temp += 1
            self.attr = str(temp)


def config_num():
    for i in empty_temp.values():
        i.configure_attr()


def create_tiles():
    for i in range(rows):
        for j in range(cols):
            empty_temp.update({(i, j): Tile((i, j))})
    for i in range(mine_num):
        x, y = random.randint(0, 9), random.randint(0, 9)
        mines.append((x, y))
        empty_temp.get((x, y)).place_mine()
    config_num()


def print_board():
    print('    {}'.format('   '.join(str(x) for x in range(10))))
    print('-------------------------------------------')
    for i in range(rows):
        s = ' {}|'.format(i)
        for j in range(cols):
            s += ' {} |'.format(empty_temp.get((i, j)).get_attr())
        print(s)
        print('-------------------------------------------')


create_tiles()
print_board()
