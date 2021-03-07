# Multiplication table

language: golang

`6 kyu`

## Instructions
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

```
1 2 3
2 4 6
3 6 9
```

for given example, the return value should be: `[[1,2,3],[2,4,6],[3,6,9]]`

## Solution

```golang
package multiplicationtable

func MultiplicationTable(size int) [][]int {
  answer:= make([][]int, size)
  for i := 0; i<size; i++{ 
    answer[i] = make([]int, size)
    for j :=0; j<size; j++{
      if j==0 {
        answer[i][j] = i+1
      } else {
        answer[i][j] = (i+1)*(j+1)
      }
    }
  }
  return answer
}
```

## Sample Tests

```
package multiplicationtable_test

import (
  "math/rand"
  "time"

  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/multiplicationtable"
)

var _ = Describe("Sample Tests", func() {
  It("Sample Tests", func() {
    Expect(MultiplicationTable(1)).To(Equal([][]int{{1}}))
    Expect(MultiplicationTable(2)).To(Equal([][]int{{1, 2}, {2, 4}}))
    Expect(MultiplicationTable(3)).To(Equal([][]int{{1, 2, 3}, {2, 4, 6}, {3, 6, 9}}))
  })
})

var _ = Describe("Test Suite", func() {
  It("Fixed Tests", func() {
    Expect(MultiplicationTable(1)).To(Equal([][]int{{1}}))
    Expect(MultiplicationTable(2)).To(Equal([][]int{{1, 2}, {2, 4}}))
    Expect(MultiplicationTable(3)).To(Equal([][]int{{1, 2, 3}, {2, 4, 6}, {3, 6, 9}}))
  })
  It("Random Tests", func() {
    for i := 0; i < 100; i++ {
      randomInput := rand.Intn(99) + 1 
      expected := reference(randomInput)
      Expect(MultiplicationTable(randomInput)).To(Equal(expected))
    }
  })
})

func init() {
  rand.Seed(time.Now().UnixNano())
}

func reference(size int) [][]int {
  table := make([][]int, size)
  for i := range table {
    table[i] = make([]int, size)
  }

  for i := 0; i < size; i++ {
    for j := 0; j < size; j++ {
      table[i][j] = (i + 1) * (j + 1)
    }
  }
  return table
}
```

## Best Practices

```golang
package multiplicationtable

func MultiplicationTable(size int) [][]int {
  res := make([][]int, size)
  for i := 0 ; i < size ; i ++ {
    for x := 1 ; x < size + 1 ; x ++ {
      res[i] = append(res[i], (i + 1) * x)
      }}
  return res
}
```
