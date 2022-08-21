package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	var name string

	fmt.Print("Enter your name: ")
	fmt.Scanf("%s", &name)

	file, err := os.Open("./feminino.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	names := []string{}

	for scanner.Scan() {
		var input string = scanner.Text()
		s := strings.Split(input, ",")[0]
		s = strings.Trim(s, "\"")
		names = append(names, s)
	}

	sort.Strings(names)

	start := 0
	end := len(names) - 1

	found := binary_search(start, end, names, name)
	if found {
		return
	}

	fmt.Println("nao achou")

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

}

func binary_search(start int, end int, names []string, name string) bool {
	for start <= end {
		middle := (start + end) / 2
		middlepoint := names[middle]

		if strings.Compare(middlepoint, name) > 0 {
			end = middle - 1
		} else if strings.Compare(middlepoint, name) < 0 {
			start = middle + 1
		} else {
			fmt.Println("achou")
			return true
		}
	}
	return false
}
