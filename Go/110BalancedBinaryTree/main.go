package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(isBalanced(&TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val: 8,
				},
			},
			Right: &TreeNode{
				Val: 5,
			},
		},
		Right: &TreeNode{
			Val: 3,
			Left: &TreeNode{
				Val: 6,
			},
		},
	}))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}

	var maxDepth func(node *TreeNode) int
	maxDepth = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		return 1 + max(maxDepth(node.Left), maxDepth(node.Right))
	}

	l := maxDepth(root.Left)
	r := maxDepth(root.Right)
	diff := math.Abs(float64(l - r))

	return diff < 2 && isBalanced(root.Left) && isBalanced(root.Right)
}
