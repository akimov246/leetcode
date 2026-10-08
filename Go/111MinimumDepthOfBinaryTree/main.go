package main

import "fmt"

func main() {
	fmt.Println(minDepth(&TreeNode{
		Val: 3,
		Left: &TreeNode{
			Val: 9,
		},
		Right: &TreeNode{
			Val: 20,
			Left: &TreeNode{
				Val: 15,
			},
			Right: &TreeNode{
				Val: 7,
			},
		},
	}))

	fmt.Println(minDepth(&TreeNode{
		Val: 2,
		Right: &TreeNode{
			Val: 3,
			Right: &TreeNode{
				Val: 4,
				Right: &TreeNode{
					Val: 5,
					Right: &TreeNode{
						Val: 6,
					},
				},
			},
		},
	}))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	if root.Left == nil && root.Right == nil {
		return 1
	}

	if root.Left == nil {
		return 1 + minDepth(root.Right)
	}

	if root.Right == nil {
		return 1 + minDepth(root.Left)
	}

	return 1 + min(minDepth(root.Left), minDepth(root.Right))
}
