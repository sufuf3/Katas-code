# Decode the Morse code

language: golang

`6 kyu`

## Instructions

In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

```
DecodeMorse(".... . -.--   .--- ..- -.. .")
// should return "HEY JUDE"
```

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

- Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
- C#: MorseCode.Get(".--") (returns string)
- Elixir: @morse_codes variable (from use MorseCode.Constants). Ignore the unused variable warning for morse_codes because it's no longer used and kept only for old solutions.
- Elm: MorseCodes.get : Dict String String
- Haskell: morseCodes ! ".--" (Codes are in a Map String String)
- Java: MorseCode.get(".--")
- Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
- Rust: self.morse_code
- Scala: morseCodes(".--")
- Swift: MorseCode[".--"] ?? "" or MorseCode[".--", default: ""]
- C: provides parallel arrays, i.e. morse[2] == "-.-" for ascii[2] == "C"

All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.

Good luck!

After you complete this kata, you may try yourself at Decode the Morse code, advanced.

## Solution

```golang
package kata

import (
	"strings"
)

func DecodeMorse(morseCode string) string {
	words := strings.Split(morseCode, "   ")
	ans := ""
	for i,v := range words {
		if v != "" {
			l := strings.Split(v, " ")
			for _,v := range l {
				ans = ans + string(MORSE_CODE[v])  
			}
			if i < (len(words)-1) {
				ans = ans + string(" ")
			}
		}
	}
	return ans
}
```

## Sample Tests

```golang
package kata_test

import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Test Example", func() {
  It("Example from description", func(){
    Expect(DecodeMorse(".... . -.--   .--- ..- -.. .")).To(Equal("HEY JUDE"))
  })
})
```

## Best Practices

```golang
package kata

import (
  "strings"
)

func DecodeMorse(morseCode string) (decoded string) {
  for _, word := range strings.Split(strings.TrimSpace(morseCode), "   ") {
    for _, char := range strings.Split(word, " "){
      decoded += MORSE_CODE[char]
    }
    decoded += " "
  }
  return strings.TrimSpace(decoded)
}
```
https://www.codewars.com/kata/reviews/59568ea5ed008103cd00012d/groups/595c94a9891563c3240005ee

```golang
package kata

import "strings"

func DecodeMorse(morseCode string) (result string) {
  
  for _, word := range strings.Split(morseCode, "   "){
    result += " "
    for _, letter := range strings.Split(word," ") {
      result += MORSE_CODE[letter]
    }
  }
  
  return strings.TrimSpace(result)
}
```
https://www.codewars.com/kata/reviews/59568ea5ed008103cd00012d/groups/599ee13344bdcfcf7200022e 
