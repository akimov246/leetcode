package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(binaryTreePaths(&TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Right: &TreeNode{
				Val: 5,
			},
		},
		Right: &TreeNode{
			Val: 3,
		},
	}))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func binaryTreePaths(root *TreeNode) []string {
	paths := make([]string, 0)
	var getPaths func(node *TreeNode, path string)
	getPaths = func(node *TreeNode, path string) {
		path += strconv.Itoa(node.Val)
		if node.Left == nil && node.Right == nil {
			paths = append(paths, path)
		} else {
			path += "->"
			if node.Left != nil {
				getPaths(node.Left, path)
			}
			if node.Right != nil {
				getPaths(node.Right, path)
			}
		}
	}
	getPaths(root, "")
	return paths
}
