package main

import (
	. "github.com/smartystreets/goconvey/convey"
	"testing"
)

type BinaryTree struct {
	items chan int
}

func (s *BinaryTree) Enqueue(item int) {
	s.items <- item
}

func (s *BinaryTree) Deque() int {
	return <- s.items
}


func TestSection1_13(t *testing.T) {
	s := BinaryTree{
		items: make(chan int, 16),
	}

	Convey("Queue2...", t, func() {
		s.Enqueue(1)
	})
}
