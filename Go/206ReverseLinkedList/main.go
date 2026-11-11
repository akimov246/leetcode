package main

func main() {
	reverseList(reverseList(&ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 3,
				Next: &ListNode{
					Val: 4,
					Next: &ListNode{
						Val: 5,
					},
				},
			},
		},
	}))
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var helper func(prev, curr *ListNode) *ListNode
	helper = func(prev, curr *ListNode) *ListNode {
		if curr == nil {
			return prev
		}
		next := curr.Next
		curr.Next = prev
		return helper(curr, next)
	}

	return helper(nil, head)
}
