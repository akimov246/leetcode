package main

import "fmt"

func main() {
	var head ListNode
	var first ListNode
	var second ListNode
	var third ListNode

	head = ListNode{Val: 3, Next: &first}
	first = ListNode{Val: 2, Next: &second}
	second = ListNode{Val: 0, Next: &third}
	third = ListNode{Val: -4, Next: &first}

	fmt.Println(hasCycle(&head))
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	checker := make(map[*ListNode]bool)

	for head != nil {
		if checker[head] {
			return true
		}
		checker[head] = true
		head = head.Next
	}
	return false
}
