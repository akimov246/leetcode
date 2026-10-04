package main

import "fmt"

func main() {
	fmt.Println(isSymmetric(&TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
			},
			Right: &TreeNode{
				Val: 4,
			},
		},
		Right: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 4,
			},
			Right: &TreeNode{
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

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	var isMirror func(l, r *TreeNode) bool

	isMirror = func(l, r *TreeNode) bool {
		if l == nil && r == nil {
			return true
		}

		if l == nil || r == nil {
			return false
		}

		if l.Val != r.Val {
			return false
		}

		return isMirror(l.Left, r.Right) && isMirror(l.Right, r.Left)
	}

	return isMirror(root.Left, root.Right)
}
