# Buddy Pairs

language: golang

`5 kyu`

## Instructions
You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. In the following description, divisors will mean proper divisors. For example for 100 they are `1, 2, 4, 5, 10, 20, 25, and 50`.

Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

For example 48 & 75 is such a pair:

- Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
- Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
Task
Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n

If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil or (for Dart) null; (for Pascal) [-1, -1].

Examples
(depending on the languages)

```
buddy(10, 50) returns [48, 75] 
buddy(48, 50) returns [48, 75]
or
buddy(10, 50) returns "(48 75)"
buddy(48, 50) returns "(48 75)"
```
Note
- for C: The returned string will be free'd.
- See more examples in "Sample Tests:" of your language.

## Solution

```golang
package kata
import "math"

// the return is `nil` if there is no buddy pair
func Buddy(start, limit int) []int {
  for i := start; i <= limit; i++ {
    sum:=0
    mystart := i
    for j := 2; j<=(int(math.Sqrt(float64(i)))); j++ {
      if i%j == 0 {
        sum = sum + j
        if j != i/j {
          sum = sum + i/j
        }
      }
    }
    sum2:=0
    for k := 2; k<=(int(math.Sqrt(float64(sum)))); k++ {
      if sum%k == 0{
        sum2 = sum2 + k
        if k != sum/k {
          sum2 = sum2 + sum/k
        }
      }
    }
    if sum2==mystart && mystart<sum{
      return []int{mystart, sum}
    }
  }
  return nil
}
```

## Sample Tests

```golang
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
  "fmt"
  "strings"
)
func arrayToString(a []int, delim string) string {
    return strings.Join(strings.Split(fmt.Sprint(a), " "), delim)
}
func dotest(start, limit int, exp string) {
    ans := arrayToString(Buddy(start, limit), " ")
    fmt.Printf("Expected %s\nGot %s\n", exp, ans)
    Expect(ans).To(Equal(exp))
}

var _ = Describe("Test Example", func() {
    It("should handle basic cases buddy", func() {
        dotest(1071625, 1103735, "[1081184 1331967]")
        dotest(57345, 90061, "[62744 75495]")
        dotest(2693, 7098, "[5775 6128]")
        dotest(6379, 8275, "[]");
    })
    
})
```

## Best Practices

```golang
package kata

func Buddy(start, limit int) []int {
  for n := start; n <= limit; n++ {
    m := sumPropDiv(n)
    if m > n {
      if sumPropDiv(m) == n {
        return []int{n, m}
      }
    }
  }
  return nil
}

func sumPropDiv(num int) (sum int) {
  for i := 2; i < num/i; i++ {
    if num%i == 0 {
      sum += i + num/i
    }
  }
  return
}
```
