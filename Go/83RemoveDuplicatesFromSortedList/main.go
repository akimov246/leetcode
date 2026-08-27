package main

import "fmt"

func main () {
	node4 := &ListNode{Val: 3}
	node3 := &ListNode{Val: 3, Next: node4}
	node2 := &ListNode{Val: 2, Next: node3}
	node1 := &ListNode{Val: 1, Next: node2}
	head := &ListNode{Val: 1, Next: node1}
	fmt.Println(deleteDuplicates(head))
}

type ListNode struct {
	Val int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	current := head
	
	for current != nil && current.Next != nil {
		if current.Val == current.Next.Val {
			current.Next = current.Next.Next
		} else {
			current = current.Next
		}
	}
	return head
}