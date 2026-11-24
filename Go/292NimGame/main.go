package main

import "fmt"

func main() {
	fmt.Println(canWinNim(4))
}

func canWinNim(n int) bool {
	return n%4 != 0
}
