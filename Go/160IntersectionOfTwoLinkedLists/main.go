package main

import "fmt"

func main() {
	var listAhead ListNode
	var listAfirst ListNode
	var listAsecond ListNode
	var listAthird ListNode
	var listAfourth ListNode
	var listBhead ListNode
	var listBfirst ListNode
	var listBsecond ListNode

	listAhead = ListNode{Val: 4, Next: &listAfirst}
	listAfirst = ListNode{Val: 1, Next: &listAsecond}
	listAsecond = ListNode{Val: 8, Next: &listAthird}
	listAthird = ListNode{Val: 4, Next: &listAfourth}
	listAfourth = ListNode{Val: 5}

	listBhead = ListNode{Val: 5, Next: &listBfirst}
	listBfirst = ListNode{Val: 6, Next: &listBsecond}
	listBsecond = ListNode{Val: 1, Next: &listAsecond}

	fmt.Println(getIntersectionNode(&listAhead, &listBhead))
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	checker := make(map[*ListNode]bool)
	for headA != nil {
		checker[headA] = true
		headA = headA.Next
	}
	for headB != nil {
		if checker[headB] {
			return headB
		}
		headB = headB.Next
	}
	return nil
}
