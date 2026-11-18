package main

func main() {

}

type MyQueue struct {
	data []int
	tmp  []int
}

func Constructor() MyQueue {
	return MyQueue{}
}

func (this *MyQueue) Push(x int) {
	for len(this.data) > 0 {
		this.tmp = append(this.tmp, this.data[len(this.data)-1])
		this.data = this.data[:len(this.data)-1]
	}
	this.data = append(this.data, x)
	for len(this.tmp) > 0 {
		this.data = append(this.data, this.tmp[len(this.tmp)-1])
		this.tmp = this.tmp[:len(this.tmp)-1]
	}
}

func (this *MyQueue) Pop() int {
	popElement := this.data[len(this.data)-1]
	this.data = this.data[:len(this.data)-1]
	return popElement
}

func (this *MyQueue) Peek() int {
	return this.data[len(this.data)-1]
}

func (this *MyQueue) Empty() bool {
	return len(this.data) == 0
}
