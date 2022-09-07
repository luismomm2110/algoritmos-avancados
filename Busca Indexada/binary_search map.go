package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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

	names := make(map[string]bool)

	for scanner.Scan() {
		var input string = scanner.Text()
		s := strings.Split(input, ",")[0]
		s = strings.Trim(s, "\"")
		names[s] = true
	}

	_, found := names[name]
	if found {
		fmt.Println("achou")
		return
	}

	fmt.Println("nao achou")

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

}
