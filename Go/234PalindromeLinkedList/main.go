package main

import "fmt"

func main() {
	fmt.Println(isPalindrome(&ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 2,
				Next: &ListNode{
					Val: 1,
				},
			},
		},
	}))
	// fmt.Println(isPalindrome(&ListNode{
	// 	Val: 1,
	// 	Next: &ListNode{
	// 		Val: 0,
	// 		Next: &ListNode{
	// 			Val: 1,
	// 		},
	// 	},
	// }))
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	slow, fast := head, head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	var reverse func(prev, curr *ListNode) *ListNode
	reverse = func(prev, curr *ListNode) *ListNode {
		if curr == nil {
			return prev
		}
		next := curr.Next
		curr.Next = prev
		return reverse(curr, next)
	}

	p1 := head
	p2 := reverse(nil, slow)
	for p2 != nil {
		if p1.Val != p2.Val {
			return false
		}
		p1 = p1.Next
		p2 = p2.Next
	}
	return true
}
