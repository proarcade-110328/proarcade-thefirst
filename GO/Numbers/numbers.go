package main

import "fmt"

func main() {
	fmt.Println("Enter any number.")
	var input int
	fmt.Scan(&input)
	i := 1
	for i <= input {
		if i%15 == 0 {
			fmt.Println("FizzBuzz")
		} else if i%5 == 0 {
			fmt.Println("Buzz")
		} else if i%3 == 0 {
			fmt.Println("Fizz")
		} else {
			fmt.Println(i)
		}
		i += 1
	}
}
