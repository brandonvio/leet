package main

import (
	. "github.com/smartystreets/goconvey/convey"
	"log"
	"testing"
)

type Stack struct {
	items []int
}

func (s *Stack) Push(item int) {
	s.items = append(s.items, item)

}

func (s *Stack) Pop() int {
	left := len(s.items)
	if left == 0 {
		return -1
	}
	item, items := s.items[left - 1], s.items[0:left - 1]
	log.Println(item, items)
	s.items = items
	return item
}

func TestSection1_11(t *testing.T) {
	Convey("Stack...", t, func() {
		s := Stack{}
		s.Push(0)
		s.Push(11)
		s.Push(12)
		s.Push(133)
		s.Push(145)

		So(s.Pop(), ShouldEqual, 145)
		So(s.Pop(), ShouldEqual, 133)
		So(s.Pop(), ShouldEqual, 12)
		So(s.Pop(), ShouldEqual, 11)
		So(s.Pop(), ShouldEqual, 0)
		So(s.Pop(), ShouldEqual, -1)
		So(s.Pop(), ShouldEqual, -1)
	})
}

