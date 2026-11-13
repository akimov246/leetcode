package main

import "fmt"

func main() {
	obj := Constructor()
	obj.Push(1)
	obj.Push(2)
	obj.Push(3)
	fmt.Println(obj.Pop())
}

type MyStack struct {
	data []int
}

func Constructor() MyStack {
	return MyStack{}
}

func (this *MyStack) Push(x int) {
	this.data = append(this.data, x)
	for range len(this.data) - 1 {
		this.data = append(this.data, this.data[0])
		this.data = this.data[1:]
	}
}

func (this *MyStack) Pop() int {
	topElement := this.data[0]
	this.data = this.data[1:]
	return topElement
}

func (this *MyStack) Top() int {
	return this.data[0]
}

func (this *MyStack) Empty() bool {
	return len(this.data) == 0
}
