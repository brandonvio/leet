package main

import (
	"fmt"
	"log"
	"math"
	"strconv"
	"testing"

	. "github.com/smartystreets/goconvey/convey"
)

func TestSection1_6(t *testing.T) {

	// Only pass t into top-level Convey calls
	// Convey("Given some integer with a starting value", t, func() {
	// 	x := 1

	// 	Convey("When the integer is incremented", func() {
	// 		x++

	// 		Convey("The value should be greater by one", func() {
	// 			So(x, ShouldEqual, 2)
	// 		})
	// 	})
	// })

	Convey("For loops and if statements...", t, func() {
		log.Println("section 1:6")
		for i := 0; i < 10; i++ {
			if i > 5 {
				log.Println("2 to the power of "+strconv.Itoa(i), math.Pow(2, float64(i)))
			} else {
				log.Println("3 to the power of "+strconv.Itoa(i), math.Pow(3, float64(i)))
				log.Println("5 to the power of "+strconv.Itoa(i), math.Pow(5, float64(i)))
			}
		}
		So(true, ShouldEqual, true)
	})

	Convey("Switch as a control structure...", t, func() {
		getPrice := func(item string) int {
			price := 0
			switch item {
			case "apple", "carrot":
				price = 10
			case "orange":
				price = 20
			}
			return price
		}
		price := getPrice("apple")
		So(price, ShouldEqual, 10)

		price = getPrice("orange")
		So(price, ShouldEqual, 20)

		price = getPrice("carrot")
		So(price, ShouldEqual, 10)

		price = getPrice("phone")
		So(price, ShouldEqual, 0)
	})
}

func TestSection1_7(t *testing.T) {
	Convey("Slices...", t, func() {
		numbers := []int{1, 1, 2, 3, 5, 8, 13}
		So(numbers[3], ShouldEqual, 3)
		So(len(numbers), ShouldEqual, 7)
		for index, value := range numbers {
			log.Println("Index:", index, "Value:", value)
		}
		for _, value := range numbers {
			log.Println("Value:", value)
		}
		numbers = append(numbers, 100, 9)
		So(numbers[len(numbers)-1], ShouldEqual, 9)
		So(numbers[len(numbers)-2], ShouldEqual, 100)
	})

	Convey("Maps...", t, func() {
		user := map[string]string{
			"name":  "Brandon",
			"email": "haleysdad@gmail.com",
		}
		log.Println(user)
		So(user["name"], ShouldEqual, "Brandon")
		So(user["email"], ShouldEqual, "haleysdad@gmail.com")
		var hasAge bool
		age, ok := user["age"]
		if ok {
			hasAge = true
		} else {
			hasAge = false
		}
		So(hasAge, ShouldEqual, false)
		So(age, ShouldEqual, "")
		So(user["Name"], ShouldEqual, "")

		for key, value := range user {
			log.Println("Key:", key, "Value:", value)
		}
	})

	Convey("Functions as variables...", t, func() {
		multiply := func(x, y int) int {
			return x * y
		}
		result := multiply(3, 6)
		So(result, ShouldEqual, 18)
	})
}

// Section 1.8 "Structs and Methods..."
type User struct {
	Name, Role, Email string
	Age               int
}

func (u *User) Salary() (int, error) {
	salary := 0
	var err error

	switch u.Role {
	case "Developer":
		salary, err = 100, nil
	case "Architect":
		salary, err = 200, nil
	default:
		salary = 0
		err = fmt.Errorf("I'm not able to handle '%s' role", u.Role)
	}
	return salary, err
}

func (u *User) UpdateEmail(email string) {
	u.Email = email
}

func (u *User) ToString() string {
	salary, _ := u.Salary()
	return fmt.Sprintf("Name:%s, Role:%s, Age:%d, Salary:%d", u.Name, u.Role, u.Age, salary)
}

func TestSection1_8(t *testing.T) {
	Convey("Structs and Methods...", t, func() {
		brandon := User{Name: "Brandon", Role: "Architect", Email: "haleysdad@gmail.com", Age: 48}
		So(brandon.Name, ShouldEqual, "Brandon")
		So(brandon.Role, ShouldEqual, "Architect")
		So(brandon.Age, ShouldEqual, 48)
		So(brandon.Email, ShouldEqual, "haleysdad@gmail.com")
		salary, err := brandon.Salary()

		So(err, ShouldBeNil)
		So(salary, ShouldEqual, 200)
		log.Println(brandon)
		brandon.UpdateEmail("brandonvio@outlook.com")
		So(brandon.Email, ShouldEqual, "brandonvio@outlook.com")
		log.Println(brandon)

		haley := User{Name: "Haley", Role: "Developer", Age: 17}
		So(haley.Name, ShouldEqual, "Haley")
		So(haley.Role, ShouldEqual, "Developer")
		So(haley.Age, ShouldEqual, 17)
		salary, err = haley.Salary()
		So(err, ShouldBeNil)
		So(salary, ShouldEqual, 100)
	})
}

func TestSection1_9(t *testing.T) {
	Convey("Error handling...", t, func() {
		haley := User{Name: "user", Role: "User", Age: 18}
		So(haley.Name, ShouldEqual, "user")
		So(haley.Role, ShouldEqual, "User")
		So(haley.Age, ShouldEqual, 18)
		salary, err := haley.Salary()

		So(err.Error(), ShouldEqual, "I'm not able to handle 'User' role")
		So(salary, ShouldEqual, 0)

		salary, err = haley.Salary()
		if err != nil {
			So(salary, ShouldEqual, 0)
			log.Println("Error handling...")
		}
		userString := haley.ToString()
		log.Println(userString)
	})
}
