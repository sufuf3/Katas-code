# Count the divisors of a number

language: golang

## Instructions
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples
```
divisors(4)  == 3  //  1, 2, 4
divisors(5)  == 2  //  1, 5
divisors(12) == 6  //  1, 2, 3, 4, 6, 12
divisors(30) == 8  //  1, 2, 3, 5, 6, 10, 15, 30
```

## Solution

```golang
package kata

func Divisors(n int)int{
    var a int =0
    for i:=2; i<=n; i++ {
        if n%i==0 {
            a++
        }
    }
    return a+1
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
var _ = Describe("Should pass some basic tests", func() {
	It("Divisors(1)", func() {Expect(Divisors(1)).To(Equal(1))})
	It("Divisors(10)", func() {Expect(Divisors(10)).To(Equal(4))})
	It("Divisors(11)", func() {Expect(Divisors(11)).To(Equal(2))})
	It("Divisors(54)", func() {Expect(Divisors(54)).To(Equal(8))})
	It("Divisors(64)", func() {Expect(Divisors(64)).To(Equal(7))})
})
```

## Best Practices

```golang
```
