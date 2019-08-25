# Functional-Addition

language: Golang 1.12

## Instructions

Create a function `add(n)`/`Add(n)` which returns a function that always adds n to any number  

```
var addOne = Add(1)
addOne(3) // 4
```

## Solution

```golang
package kata

func Add(i int) func(int)int {
  return func(j int) int {
    return i + j
  }
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
var _ = It("sample test", func() {
  Expect(Add(1)(3)).To(Equal(4))
})
```

## Best Practices

