package main

import (
	"log"
	"math"
)

//#region section1
func hello() {
	println("Hello!")
}

func sum(x, y int) int {
	return x + y
}

func swap(x, y int) (int, int) {
	return y, x
}

func section1() {
	a, b := swap(10, 20)
	println(a, b)
	println(sum(5, 6))
	hello()

	multiply := func(x, y int) int {
		return x * y
	}

	println(multiply(3, 6))
}

//#endregion

func main() {
	section1()
	log.Println("section 1:6")
	for i := 0; i < 10; i++ {
		if i > 5 {
			log.Println(math.Pow(2, float64(i)), i)
		} else {
			log.Println(math.Pow(3, float64(i)), i)
		}
	}
}
