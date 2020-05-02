# Roman Numerals Decoder

language: golang

`6 kyu`

## Instructions

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:
```
solution('XXI'); // should return 21
```
Help:
```
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
```

## Solution
```go
package kata

func Decode(roman string) int {
  m := map[string]int{
       "I" : 1,
       "V" : 5,
       "X" : 10,
       "L" : 50,
       "C" : 100,
       "D" : 500,
       "M" : 1000,
    }
  num := 0
  if len(roman) == 1 {
    return m[roman]
  }

  for i,v := range roman {
    if i>0 && m[string(v)] > m[string(roman[i-1])]{
      num = num - m[string(roman[i-1])]*2 + m[string(v)]
    } else {
      num = num + m[string(v)]
    }
  }
  return num
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

var _ = Describe("test roman to decimal converter", func() {
   It("should give decimal number from roman", func() {
     Expect(Decode("XXI")).To(Equal(21))
    
   })
   It("should give decimal number from roman", func() {
     Expect(Decode("I")).To(Equal(1))
   })
   It("should give decimal number from roman", func() {
     Expect(Decode("IV")).To(Equal(4))
   })
   It("should give decimal number from roman", func() {
     Expect(Decode("MMVIII")).To(Equal(2008))
   })
   It("should give decimal number from roman", func() {
     Expect(Decode("MDCLXVI")).To(Equal(1666))
   })
})
```

## Best Practices

```go
package kata

var decoder = map[rune]int {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

func Decode(roman string) int {
    if len(roman) == 0 { return 0 }
    first := decoder[rune(roman[0])]
    if len(roman) == 1 { return first }
    next := decoder[rune(roman[1])]
    if next > first { return (next - first) + Decode(roman[2:]) }
    return first + Decode(roman[1:])
}
```
