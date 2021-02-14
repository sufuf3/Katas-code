# Count the divisors of a number

language: golang

`6 kyu`

## Instructions
Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

```
pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
```
Note: the subarrays should be filled with 1s

## Solution

```golang
package kata

//import "fmt"

func Pyramid(n int) [][]int {
    if (n==0) {
        return [][]int{}
    }
    var array [][]int
    if(n>0) {
            var item []int
            for j := 0; j < n; j++ {
                item = append(item, 1)
                array = append(array, item)
            }
    }
    return array
}
```

## Sample Tests

```
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)
var _ = Describe("Basic Tests", func() {
    It("Testing for 0", func() { Expect(Pyramid(0)).To(Equal([][]int{})) })
    It("Testing for 1", func() { Expect(Pyramid(1)).To(Equal([][]int{[]int{1}})) })
    It("Testing for 2", func() { Expect(Pyramid(2)).To(Equal([][]int{[]int{1}, []int{1, 1}})) })
    It("Testing for 3", func() { Expect(Pyramid(3)).To(Equal([][]int{[]int{1}, []int{1, 1}, []int{1, 1, 1}})) })
})
```

## Best Practices

```golang
package kata

func Pyramid(n int) [][]int {
    row := [][]int{}
    cell := []int{}
    
    for i := 0; i < n; i++ {
      cell = append(cell, 1)
      row = append(row, cell)
    }
    
    return row
}
```

```golang
package kata

func Pyramid(n int) [][]int {
    pyramid := make([][]int, n)
    
    for i := range pyramid {
      layer := make([]int, i + 1)
      for j := range layer {
        layer[j] = 1
      }
      pyramid[i] = layer
    }
    
    return pyramid
}
```
