package main

import "fmt"

func main() {
	fmt.Println(postorderTraversal(&TreeNode{
		Val: 1,
		Right: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
			},
		},
	}))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postorderTraversal(root *TreeNode) []int {
	traversal := make([]int, 0)
	var helper func(node *TreeNode)
	helper = func(node *TreeNode) {
		if node != nil {
			helper(node.Left)
			helper(node.Right)
			traversal = append(traversal, node.Val)
		}
	}
	helper(root)
	return traversal
}
