# Vowel Count

language: golang
`7 kyu`

## Instructions

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

## Solution

```go
package kata

func GetCount(str string) (count int) {
  count = 0
  for i:=0; i<len(str); i++{
    if string(str[i])=="a" || string(str[i])=="e" || string(str[i])=="i" || string(str[i])=="o" || string(str[i])=="u"{
      count++
    }
  }
  return count
}
```
Solve 2
```go
package kata

func GetCount(str string) (count int) {
  for _, c:= range str{
    switch c{
      case 'a', 'e', 'i', 'o', 'u':
        count ++
    }
  }
  return count
}
```

## Sample Tests

```go
// Ginkgo BDD Testing Framework <http://onsi.github.io/ginkgo></http:>
// Gomega Matcher Library <http://onsi.github.io/gomega></http:>

package kata_test

import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Test Example", func() {
  It("should test that the solution returns the correct value", func() {
    Expect(GetCount("abracadabra")).To(Equal(5))
  })
})
```

