package main

import "fmt"

func main() {
	fmt.Println(preorderTraversal(&TreeNode{
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

func preorderTraversal(root *TreeNode) []int {
	traversal := make([]int, 0)
	var helper func(node *TreeNode)
	helper = func(node *TreeNode) {
		if node != nil {
			traversal = append(traversal, node.Val)
			helper(node.Left)
			helper(node.Right)
		}
	}
	helper(root)
	return traversal
}
