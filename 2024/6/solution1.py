import argparse

class Guard:
    directions: list[list[int]] = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dx: int = 0
    dy: int = 0

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.direction_index = -1
        self.change_direction()

    def change_direction(self) -> None:
        self.direction_index = (self.direction_index + 1) % len(self.directions)
        self.dx, self.dy = self.directions[self.direction_index]

    def next_move(self) -> tuple[int, int]:
        return self.x + self.dx, self.y + self.dy

    def move(self) -> None:
        self.x += self.dx
        self.y += self.dy

    def current_location(self) -> tuple[int, int]:
        return self.x, self.y

class Maze:

    def __init__(self, maze: list[list[str]]):
        self.maze = maze
        self.r: int = len(maze)
        self.c: int = len(maze[0])

        for i in range(self.r):
            for j in range(self.c):
                if maze[i][j] == "^":
                    self.guard: Guard = Guard(i, j)

    @classmethod
    def initialize_maze(cls, filename):
        with open(filename, "r") as file:
            maze = [list(_.strip()) for _ in file.readlines()]
        return Maze(maze)

    def start(self):
        while not self.is_complete():
            a, b = self.guard.current_location()
            self.maze[a][b] = "X"

            while True:
                x, y = self.guard.next_move()
                if self.is_next_move_valid() and self.maze[x][y] == "#":
                    self.guard.change_direction()
                else:
                    break
            self.guard.move()

    def is_complete(self) -> bool:
        x, y = self.guard.current_location()
        return x < 0 or self.r <= x or y < 0 or self.c <= y

    def is_next_move_valid(self) -> bool:
        x, y = self.guard.next_move()
        return (0 <= x and x < self.r) and (0 <= y and y < self.c)

    def count(self) -> int:
        c: int = 0
        for i in range(self.r):
            for j in range(self.c):
                c += (self.maze[i][j] == "X")
        return c

    def print(self) -> None:
        print("---")
        for i in range(self.r):
            print(''.join(self.maze[i]))
        print("---")


def main(filename: str):
    maze: Maze = Maze.initialize_maze(filename)
    maze.start()
    maze.print()
    print(maze.count())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename")
    args = parser.parse_args()

    main(args.input_filename)
