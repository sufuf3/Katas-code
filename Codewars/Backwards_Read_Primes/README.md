# Backwards Read Primes

language: golang

`6 kyu`

## Instructions

Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a different prime. (This rules out primes which are palindromes.)
```
Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.
```
Task
Find all Backwards Read Primes between two positive given numbers (both inclusive), the second one always being greater than or equal to the first one. The resulting array or the resulting string will be ordered following the natural order of the prime numbers.

Examples (in general form):
backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967] backwardsPrime(501, 599) => []

See "Sample Tests" for your language.

Notes
- Forth Return only the first backwards-read prime between start and end or 0 if you don't find any
- Ruby Don't use Ruby Prime class, it's disabled.

## Solution

```go
package kata

import (
  "math"
  "strconv"
  "fmt"
)

func ReverseNumber(number int) int {  
  strNumber := strconv.Itoa(number)  
  reverseStrNumber := ""  
  for length := len(strNumber); length > 0; length-- {  
    reverseStrNumber += string(strNumber[length-1])  
  }  
  reverseNum, error := strconv.Atoi(reverseStrNumber)  
  if error != nil {  
    fmt.Println("Failure to cast String to int")  
  }  
  return reverseNum  
}

func IsPrime(num int) bool{
    for d := 2; d <= int(math.Sqrt(float64(num))); d++ {
    if num%d==0{
      return false
    }
  }
  return true
}

func BackwardsPrime(start int, stop int) []int {
  var primes []int  
  for ; start <= stop; start++ {
    num := ReverseNumber(start)
    if start>10 && IsPrime(start) && IsPrime(num) && num != start {
      primes = append(primes, start)
    }
  }
  return primes
}
```

## Sample Tests

```go
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
  
)

func dotest(start int, stop int, exp []int) {
    var ans = BackwardsPrime(start, stop)
    Expect(ans).To(Equal(exp))
}

var _ = Describe("Tests BackwardsPrime", func() {

    It("should handle basic cases", func() {
        var a = []int{13, 17, 31, 37, 71, 73, 79, 97}
        dotest(1, 100, a)
        a = []int{13, 17, 31}
        dotest(1, 31, a)
        dotest(501, 599, nil)
        
    })
})

```

## Best Practices

```go
package kata

func BackwardsPrime(start int, stop int) []int {
  if start%2==0 {start++}
  var res []int
  for n:= start; n<=stop; n+=2{
    if isPrimeDiv(n){
      r:= reverseInt(n)
      if r!=n && isPrimeDiv(r){
        res = append(res, n)
      }
    }    
  }
  return res
}

func isPrimeDiv(n int) bool {
  for d:= 2; d*d<=n; d++{
    if n%d==0 {
      return false
    }
  }    
  return true
}

func reverseInt(n int) int{
  var res int
  for ;n>0;n/=10{
    res= res*10+n%10
  }
  return res
}
```
