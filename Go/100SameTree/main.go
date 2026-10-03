package main

import (
	"fmt"
)

func main() {
	fmt.Println(isSameTree(&TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
		},
		Right: &TreeNode{
			Val: 3,
		},
	},
		&TreeNode{
			Val: 1,
			Left: &TreeNode{
				Val: 2,
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

type Stack []StackElement

type StackElement struct {
	node  *TreeNode
	side  int8
	level int64
}

func (stack *Stack) pop() StackElement {
	element := (*stack)[len(*stack)-1]
	*stack = (*stack)[:len(*stack)-1]
	return element
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	var level int64
	var pStack = make(Stack, 0)
	var qStack = make(Stack, 0)
	if p != nil {
		pStack = append(pStack, StackElement{node: p, side: 0, level: level})
	}
	if q != nil {
		qStack = append(qStack, StackElement{node: q, side: 0, level: level})
	}

	for len(pStack) > 0 || len(qStack) > 0 {
		var pElement StackElement
		var qElement StackElement
		if len(pStack) > 0 {
			pElement = pStack.pop()
			if pElement.node.Right != nil {
				pStack = append(pStack, StackElement{node: pElement.node.Right, side: 1, level: level})
			}
			if pElement.node.Left != nil {
				pStack = append(pStack, StackElement{node: pElement.node.Left, side: 2, level: level})
			}
		}
		if len(qStack) > 0 {
			qElement = qStack.pop()
			if qElement.node.Right != nil {
				qStack = append(qStack, StackElement{node: qElement.node.Right, side: 1, level: level})
			}
			if qElement.node.Left != nil {
				qStack = append(qStack, StackElement{node: qElement.node.Left, side: 2, level: level})
			}
		}
		if pElement.node == nil || qElement.node == nil || pElement.node.Val != qElement.node.Val || pElement.side != qElement.side || pElement.level != qElement.level {
			return false
		}
		level++
	}
	return true
}
