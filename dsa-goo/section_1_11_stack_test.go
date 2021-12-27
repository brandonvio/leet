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

}

func (s *Stack) Pop() int {
	return 0
}

func TestSection1_11(t *testing.T) {
	Convey("Stack...", t, func() {
		s := Stack{}
		s.Push(0)
		s.Push(11)
		s.Push(12)
		s.Push(133)
		s.Push(145)

		log.Println(s.Pop())
		log.Println(s.Pop())
		log.Println(s.Pop())
		log.Println(s.Pop())
		log.Println(s.Pop())
	})
}
