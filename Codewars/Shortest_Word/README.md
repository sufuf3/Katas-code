# Shortest Word

language: Golang 1.12

## Instructions

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.


## Solution

```golang
package kata
import (
  "strings"
)

func FindShort(s string) int {
  a := strings.Split(s, " ");
  var k int;
  ans := 9999;
  for i := range a {
   k = strings.Count(a[i], "")-1; // take away 1 for before & after each rune
   if k<ans {
     ans = k;
   }
  }
  return ans;
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
var _ = Describe("Test Example", func() {
  It("should test that the solution returns the correct value", func() {
    Expect(FindShort("bitcoin take over the world maybe who knows perhaps")).To(Equal(3))
    Expect(FindShort("turns out random test cases are easier than writing out basic ones")).To(Equal(3))
  })
})
```

## Best Practices

```golang
package kata

import "strings"

func FindShort(s string) int {
  shortest := len(s)
  for _, word := range strings.Split(s, " ") {
    if len(word) < shortest {
      shortest = len(word)
    }
  }
  return shortest
}
```
