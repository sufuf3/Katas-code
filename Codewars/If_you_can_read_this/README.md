# If you can read this...

language: go
`6 kyu`

## Instructions

The idea for this Kata came from 9gag today.here

You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet) wiki.

Like this:

** Input: ** If you can read

** Output: ** India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta

** Some notes **

Keep the punctuation, and remove the spaces.
Use Xray without dash or space.

## Solution

```go
package kata
 
import (
  "strings"
  )
 
func ToNato(words string) string {
  nato := []string{"Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot","Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"}
  ans := []string{}
  words = strings.ToUpper(words)
  for i:=0; i<len(words); i++{
    flag := 0
    for j:=0; j<26; j++{
      if nato[j][0] == words[i] {
        ans = append(ans, string(nato[j]))
        flag = 1
        break
      }
    }
    if flag == 0 && string(words[i]) != " "{
      ans = append(ans, string(words[i]))
    }
  }
    return strings.Join(ans, " ")
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
 
var _ = Describe("Tests using hard-coded strings", func() {
  It("Should return a correctly translated string", func() {
     Expect(ToNato("If you can read")).To(Equal("India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta"))
     Expect(ToNato("Did not see that coming")).To(Equal("Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf"))
     Expect(ToNato("go for it!")).To(Equal("Golf Oscar Foxtrot Oscar Romeo India Tango !"))
  })
})
```

## Best Practices

```go
package kata
 
import "unicode"
import "strings"
 
func ToNato(words string) string {
  nato := []string{
    "Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
    "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November",
    "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
    "Whiskey", "Xray", "Yankee", "Zulu",
  }
  charToCharlie := map[rune]string{}
  for _, value := range nato {
    charToCharlie[rune(value[0])] = value
  }

  result := ""
  for _, letter := range words {
    if unicode.IsLetter(letter) {
      result += charToCharlie[unicode.ToUpper(letter)] + " "
    } else if unicode.IsPunct(letter) {
      result += string(letter)
    }
  }
  return strings.TrimSpace(result)
}
```
