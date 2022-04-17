package main

import (
	"fmt"
	"reflect"
)

var (
	//name, course string
	//module, clip int
	name, course = "Nigel Poulton", "Getting Started with Kubernetes"
	module, clip = 4, 2
)

func main() {
	fmt.Println("Name and course are set to", name, "and", course, ".")
	fmt.Println("module and clip are set to", module, "and", clip, ".")
	fmt.Println("Name is of type", reflect.TypeOf(name))
	fmt.Println("Module is of type", reflect.TypeOf(module))
}
