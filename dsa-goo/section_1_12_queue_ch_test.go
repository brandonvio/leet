package main

import (
	. "github.com/smartystreets/goconvey/convey"
	"testing"
)

type Queue2 struct {
	items chan int
}

func (s *Queue2) Enqueue(item int) {
	s.items <- item
}

func (s *Queue2) Deque() int {
	return <- s.items
}


func TestSection1_12_1(t *testing.T) {
	s := Queue2{
		items: make(chan int, 16),
	}

	Convey("Queue2...", t, func() {

		s.Enqueue(0)
		s.Enqueue(11)
		s.Enqueue(12)
		s.Enqueue(133)
		s.Enqueue(145)

		So(s.Deque(), ShouldEqual, 0)
		So(s.Deque(), ShouldEqual, 11)
		So(s.Deque(), ShouldEqual, 12)
		So(s.Deque(), ShouldEqual, 133)
		So(s.Deque(), ShouldEqual, 145)
	})
}
