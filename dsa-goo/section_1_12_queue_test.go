package main

import (
	. "github.com/smartystreets/goconvey/convey"
	"log"
	"testing"
)

type Queue struct {
	items []int
}

func (s *Queue) Enqueue(item int) {
	s.items = append(s.items, item)
}

func (s *Queue) Deque() int {
	left := len(s.items)
	if left == 0 {
		return -1
	}
	item, items := s.items[0], s.items[1:]
	log.Println(item, items)
	s.items = items
	return item
}

func TestSection1_12(t *testing.T) {
	Convey("Queue...", t, func() {
		s := Queue{}
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
		So(s.Deque(), ShouldEqual, -1)
		So(s.Deque(), ShouldEqual, -1)
	})
}
