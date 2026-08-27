package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	list1Node2 := &ListNode{Val: 4}
	list1Node1 := &ListNode{Val: 2, Next: list1Node2}
	list1 := &ListNode{Val: 1, Next: list1Node1}

	list2Node2 := &ListNode{Val: 4}
	list2Node1 := &ListNode{Val: 3, Next: list2Node2}
	list2 := &ListNode{Val: 1, Next: list2Node1}
	fmt.Println(mergeTwoLists(list1, list2))
	fmt.Println(mergeTwoLists(nil, &ListNode{}))
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	head := &ListNode{}
	tail := head

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			tail.Next = list1
			list1 = list1.Next
		} else {
			tail.Next = list2
			list2 = list2.Next
		}
		tail = tail.Next
	}

	if list1 != nil {
		tail.Next = list1
	} else {
		tail.Next = list2
	}

	return head.Next
}

func (node *ListNode) String() string {
	s := make([]string, 0)
	for node != nil {
		s = append(s, strconv.Itoa(node.Val))
		node = node.Next
	}
	return strings.Join(s, " → ")
}
