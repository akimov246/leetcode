package main

func main() {
	removeElements(&ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 6,
				Next: &ListNode{
					Val: 3,
					Next: &ListNode{
						Val: 4,
						Next: &ListNode{
							Val: 5,
							Next: &ListNode{
								Val: 6,
							},
						},
					},
				},
			},
		},
	}, 6)

	//	removeElements(&ListNode{
	//		Val: 7,
	//		Next: &ListNode{
	//			Val: 7,
	//			Next: &ListNode{
	//				Val: 7,
	//				Next: &ListNode{
	//					Val: 7,
	//				},
	//			},
	//		},
	//	}, 7)
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
	dummy := &ListNode{}
	current := dummy

	for head != nil {
		if head.Val != val {
			current.Next = head
			current = current.Next
		}
		head = head.Next
	}
	current.Next = nil

	return dummy.Next
}
