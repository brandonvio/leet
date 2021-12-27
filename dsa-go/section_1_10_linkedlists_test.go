package main

import (
	"log"
	"testing"

	. "github.com/smartystreets/goconvey/convey"
)

type Node struct {
	value int
	next  *Node
	prev  *Node
}

type List struct {
	head *Node
	tail *Node
}

func (l *List) First() *Node {
	return l.head
}

func (l *List) Last() *Node {
	return l.tail
}

func (l *List) Find(value int) *Node {
	n := l.First()
	for {
		if n.value == value {
			return n
		}

		n = n.Next()
		if n == nil {
			break
		}
	}
	return nil
}

func (n *Node) Next() *Node {
	return n.next
}

func (n *Node) Prev() *Node {
	return n.prev
}

func (l *List) Push(value int) {
	node := &Node{value: value}
	if l.head == nil {
		l.head = node
	} else {
		l.tail.next = node
		node.prev = l.tail
	}
	l.tail = node
}

func (l *List) Push2(value int) {
	node := &Node{value: value}
	if l.head == nil {
		l.head = node
	} else {
		iterator := l.head
		for ; iterator.next != nil; iterator = iterator.next {
		}
		iterator.next = node
		node.prev = iterator
		l.tail = node
	}
}

func TestSection1_10(t *testing.T) {
	Convey("Linked lists...", t, func() {
		l := &List{}
		l.Push2(1)
		l.Push2(2)
		l.Push2(3)
		l.Push(20)
		l.Push(21)
		l.Push(25)

		n := l.First()
		So(n.value, ShouldEqual, 1)
		n = n.Next()
		So(n.value, ShouldEqual, 2)
		n = n.Next()
		So(n.value, ShouldEqual, 3)

		n = l.First()
		for {
			log.Println(n.value)
			n = n.Next()
			if n == nil {
				break
			}
		}

		n = l.Last()
		for {
			log.Println(n.value)
			n = n.Prev()
			if n == nil {
				break
			}
		}

		n = l.Find(20)
		So(n.value, ShouldEqual, 20)

		n = l.Find(30)
		So(n, ShouldEqual, nil)
	})
}
