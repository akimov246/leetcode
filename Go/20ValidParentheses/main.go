package main

import "slices"

func main() {
	isValid("()[]{}")
}

func isValid(s string) bool {
	if len(s)%2 != 0 {
		return false
	}
	runes := []rune(s)
	stack := make([]rune, 0)

	for _, r := range runes {
		switch {
		case slices.Contains([]rune{'(', '{', '['}, r):
			stack = append(stack, r)
		case r == ')':
			if s, ok := pop(&stack); s != '(' || !ok {
				return false
			}
		case r == '}':
			if s, ok := pop(&stack); s != '{' || !ok {
				return false
			}
		case r == ']':
			if s, ok := pop(&stack); s != '[' || !ok {
				return false
			}
		}
	}

	if len(stack) != 0 {
		return false
	}
	return true
}

func pop(runes *[]rune) (rune, bool) {
	if len(*runes) == 0 {
		return 0, false
	}
	lastRune := (*runes)[len(*runes)-1]
	*runes = (*runes)[:len(*runes)-1]
	return lastRune, true
}
