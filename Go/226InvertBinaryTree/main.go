package main

func main() {

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	var helper func(node *TreeNode)
	helper = func(node *TreeNode) {
		if node == nil {
			return
		}
		node.Left, node.Right = node.Right, node.Left
		helper(node.Left)
		helper(node.Right)
	}
	helper(root)
	return root
}
