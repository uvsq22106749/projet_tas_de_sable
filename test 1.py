from tkinter import*
# crée une grille, l'affiche sur une fenêtre:
class Sandpile:
    def __init__(self, wn, grid):
        self.window = wn
        self.grid = grid
        self.canvas = Canvas(wn, bg='white')
        self.canvas.pack(fill=BOTH, expand=1)

        colors = {0: 'white',
                1: 'purple',
                2: 'purple',
                3: 'white'}

        x = 10
        y = 10
        d = 5

        for row in self.grid:
            for value in row:
                clr = colors[value]
                self.canvas.create_rectangle(
                    x, y, x + d, y + d,
                    outline=clr,
                    fill=clr)
                x += 5
            x = 10
            y += 5


class Grid:
    def __init__(self, size, center):
        self.size = size  # lignes et colonnes
        self.center = center  # valeur de depart au centre de la grille
        self.grid = [[0] * self.size for i in range(self.size)]
        self.grid[self.size // 2][self.size // 2] = self.center

    # print the grid:
    def show(self, msg):
        print('  ' + msg + ':')
        for row in self.grid:
            print(' '.join(str(x) for x in row))
        print()
        return

    # repartit les tas de sable:
    def abelian(self):
        while True:
            found = False
            for r in range(self.size):
                for c in range(self.size):
                    if self.grid[r][c] > 3:
                        self.distribute(self.grid[r][c], r, c)
                        found = True
            if not found:
                return

    # distribue le sable d'un tas seul vers ses voisins:
    def distribute(self, nbr, row, col):
        qty, remain = divmod(nbr, 4)
        self.grid[row][col] = remain
        for r, c in [(row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1)]:
            self.grid[r][c] += qty
        return

    # affiche la grille venant de tkinter:
    def display(self):
        root = Tk()
        root.title('Sandpile')
        root.geometry('700x700+100+50')
        sp = Sandpile(root, self.grid)
        root.mainloop()
# montre les résultats dans une grande fenêtre
g = Grid(131, 25000)
g.abelian()  # disperse le sable
g.display()  # affiche le résultat
