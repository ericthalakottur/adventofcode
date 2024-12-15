package main

import (
	"bufio"
	"fmt"
	"os"
)

var directions = [...][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

func isValid(x int, y int, n int, m int) bool {
	return (0 <= x && x < n) && (0 <= y && y < m)
}

func solve(x int, y int, n int, m int, grid []string, visited [][]bool) (int, int) {
	fenceCount := 0
	area := 1
	visited[x][y] = true

	for i := range len(directions) {
		dx, dy := directions[i][0], directions[i][1]
		if !isValid(x+dx, y+dy, n, m) {
			fenceCount++
			continue
		}
		if grid[x][y] != grid[x+dx][y+dy] {
			fenceCount++
			continue
		}
		if visited[x+dx][y+dy] {
			continue
		}
		a, b := solve(x+dx, y+dy, n, m, grid, visited)
		area += a
		fenceCount += b
	}

	return area, fenceCount
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var grid []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		grid = append(grid, scanner.Text())
	}

	n, m := len(grid), len(grid[0])
	visited := make([][]bool, n)
	for i := range n {
		visited[i] = make([]bool, m)
	}

	answer := 0
	for i := range n {
		for j := range m {
			if !visited[i][j] {
				a, b := solve(i, j, n, m, grid, visited)
				answer += a * b
			}
		}
	}
	fmt.Println(answer)
}
