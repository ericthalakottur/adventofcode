package main

import (
	"fmt"
	"os"
)

func sumOfNumbers(l int, r int) int {
	return (r*(r+1))/2 - (l*(l-1))/2
}

func main() {
	ip, err := os.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}
	ip = ip[:len(ip)-1]

	var fileSystem []int
	var fileIndex, totalFileSystemSize int

	for i, val := range ip {
		size := int(val - byte('0'))
		fileSystem = append(fileSystem, size)
		if i%2 == 0 {
			totalFileSystemSize += size
			fileIndex = i
		}
	}

	j := 0
	var size, answer int
	for i := 0; i < totalFileSystemSize; i++ {
		var currentFileIndex int

		if j%2 == 0 {
			size = fileSystem[j]
			currentFileIndex = j / 2
			j++
		} else {
			freeSpace := fileSystem[j]
			size = min(freeSpace, fileSystem[fileIndex])

			fileSystem[fileIndex] -= size
			fileSystem[j] -= size
			currentFileIndex = fileIndex / 2

			if fileSystem[fileIndex] <= 0 {
				fileIndex -= 2
			}
			if fileSystem[j] <= 0 {
				j++
			}
		}

		answer += currentFileIndex * sumOfNumbers(i, i+size-1)
		i += size - 1
	}

	fmt.Printf("Answer: %d\n", answer)
}
