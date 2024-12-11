import copy
import argparse
import concurrent.futures

maze: list[list[str]] = []

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
        self.visited: list[list[int]] = [[0] * self.c for _ in range(self.r)]

        for i in range(self.r):
            for j in range(self.c):
                if maze[i][j] == "^" or maze[i][j] == "S":
                    self.guard: Guard = Guard(i, j)

    def solve(self):
        while not self.is_complete():
            a, b = self.guard.current_location()
            self.maze[a][b] = "X"
            moves: int = 0

            while True:
                x, y = self.guard.next_move()
                moves += 1
                if moves >= self.r * self.c:
                    break
                if self.is_next_move_valid() and self.maze[x][y] in ("#", "O") \
                    and not self.is_cycle():
                    self.guard.change_direction()
                else:
                    break

            if self.is_next_move_valid() and self.is_cycle():
                break
            if moves >= self.r * self.c:
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

    def is_cycle(self) -> bool:
        x, y = self.guard.next_move()
        if self.maze[x][y] in ("#", "O"):
            return False
        if self.guard.dx == -1 and self.guard.dy == 0:
            if self.visited[x][y] & int("0010", 2):
                return True
            self.visited[x][y] = int("0010", 2)
        elif self.guard.dx == 0 and self.guard.dy == 1:
            if self.visited[x][y] & int("1000", 2):
                return True
            self.visited[x][y] = int("1000", 2)
        elif self.guard.dx == 1 and self.guard.dy == 0:
            if self.visited[x][y] & int("0001", 2):
                return True
            self.visited[x][y] = int("0001", 2)
        else:
            if self.visited[x][y] & int("0100", 2):
                return True
            self.visited[x][y] = int("0100", 2)
        return False


    def print(self) -> None:
        print("---")
        for i in range(self.r):
            print(''.join(self.maze[i]))
        print("---")

def run_program(possibility: tuple[int, int]) -> bool:
    global maze

    x, y = possibility
    maze_copy = copy.deepcopy(maze)
    maze_copy[x][y] = "O" if maze_copy[x][y] != "^" else "S"

    m: Maze = Maze(maze_copy)
    m.solve()
    return m.is_complete()

def main(filename: str):
    global maze

    answer: int = 0

    with open(filename, "r") as file:
        maze = [list(_.strip()) for _ in file.readlines()]

    solved_maze: Maze = Maze(copy.deepcopy(maze))
    solved_maze.solve()
    possibilities: list[tuple[int, int]] = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if solved_maze.maze[i][j] == "X":
                possibilities.append((i, j))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _, is_complete in zip(possibilities, executor.map(run_program, possibilities)):
            if not is_complete:
                answer += 1

    print(answer)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename")
    args = parser.parse_args()

    main(args.input_filename)
