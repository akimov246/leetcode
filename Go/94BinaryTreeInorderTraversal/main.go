package main

import "fmt"

func main() {
	fmt.Println(inorderTraversal(&TreeNode{
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

func inorderTraversal(root *TreeNode) []int {
	var values []int
	traversal(root, &values)
	return values
}

func traversal(root *TreeNode, values *[]int) {
	if root != nil {
		traversal(root.Left, values)
		*values = append(*values, root.Val)
		traversal(root.Right, values)
	}
}
