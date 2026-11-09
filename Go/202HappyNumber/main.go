package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	fmt.Println(isHappy(19))
	fmt.Println(isHappy(2))
}

func isHappy(n int) bool {
	set := make(map[int]struct{})

	for {
		if _, exists := set[n]; exists {
			return false
		}
		set[n] = struct{}{}
		sumOfSquares := 0
		for _, digitRune := range strconv.Itoa(n) {
			digitFloat64, _ := strconv.ParseFloat(string(digitRune), 64)
			sumOfSquares += int(math.Pow(digitFloat64, 2))
		}
		if sumOfSquares == 1 {
			return true
		}
		n = sumOfSquares
	}
}
