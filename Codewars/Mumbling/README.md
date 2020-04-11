# Mumbling

language: golang

`7 kyu`

## Instructions

This time no story, no theory. The examples below show you how to write function `accum`:

Examples:
```
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```
The parameter of accum is a string which includes only letters from `a..z` and `A..Z`.

## Solution

```go
package kata

import ("unicode"
        "strings")

func Accum(s string) string {
    var ans string
    for i, c := range s {
      if i == (len(s) -1) {
        ans = ans + string(unicode.ToUpper(c)) + strings.Repeat(string(unicode.ToLower(c)),i)
      } else {
        ans = ans + string(unicode.ToUpper(c)) + strings.Repeat(string(unicode.ToLower(c)),i) + "-"
      }
    }
    return ans
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

func dotest(s string, exp string) {
    var ans = Accum(s)
    Expect(ans).To(Equal(exp))
}

var _ = Describe("Test Example", func() {

    It("should handle basic cases", func() {
        dotest("ZpglnRxqenU", "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
        dotest("NyffsGeyylB", "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
        dotest("MjtkuBovqrU", "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
        dotest("EvidjUnokmM", "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
        dotest("HbideVbxncC", "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
    })
})


```

## Best Practices

```go
package kata

import "strings"

func Accum(s string) string {
    parts := make([]string, len(s))
    
    for i := 0; i < len(s); i++ {
      parts[i] = strings.ToUpper(string(s[i])) + strings.Repeat(strings.ToLower(string(s[i])), i)
    }
    
    return strings.Join(parts, "-")
}
```
