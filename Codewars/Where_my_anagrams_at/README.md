# Where my anagrams at?

language: golang

`5 kyu`

## Instructions

What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

```sh
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
```

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

```
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```

Note for Go
- For Go: Empty string slice is expected when there are no anagrams found.


## Solution

```go
package kata
import(
  "strings"
)

func Anagrams(word string, words []string) []string {  
  w := ""
  for _,l := range strings.Split(word,""){
    if w == "" {
      w = l
    }
    if !strings.Contains(w,l) {
      w += l
    }
  }
  result := []string{}
  for _, lword := range words {
    inalist := true
    for _, a := range w {
      if !strings.ContainsRune(lword,a) {
        inalist = false
      }
    }
    inblist := true
    for _, b := range lword {
      if !strings.ContainsRune(w,b) {
        inblist = false
      }
    }
    if inalist && inblist && len(lword)==len(word){
      result = append(result, lword)
    }
  }
  if len(result) == 0 {
    return nil
  }
  return result
}
```

## Sample Tests

```go
package kata_test

import (
    "github.com/onsi/ginkgo"
    "github.com/onsi/gomega"
    "codewarrior/kata"
)

func dotest(word string, words, exp []string) {
    var ans = kata.Anagrams(word, words)
    gomega.Expect(ans).To(gomega.Equal(exp))
}

var _ = ginkgo.Describe("Test Example", func() {
ginkgo.It("should handle basic cases", func() {
     dotest("abba", []string{"aabb", "abcd", "bbaa", "dada"}, []string{"aabb", "bbaa"})
     dotest("laser", []string{"lazing", "lazy",  "lacer"}, nil)
   })
})
```

## Best Practices
- janpi
```go
package kata

func check(ana []int, w string) bool {
  for _, c := range w {
    if ana[c-97] == 0 {
      return false
    }
    ana[c-97]--
  }
  return true
}

func Anagrams(word string, words []string) (res []string) {
  m := make([]int, 26)
  tmp := make([]int, 26)
  for _, c := range word {
    m[c-97]++
  }
  for _, w := range words {
    if len(w) == len(word) {
      copy(tmp, m)
      if check(tmp, w) {
        res = append(res, w)
      }
    }
  }
  return res
}
```

- samuelgneff
```go
package kata
import (
  "reflect"
)
func Anagrams(word string, words []string) []string {
  
    // get count of individual characters in word
    letterCount := make(map[string]int)
    var returnWords []string
    for i :=0; i < len(word); i++ {
      if _, ok := letterCount[string(word[i])]; ok {
        letterCount[string(word[i])] = letterCount[string(word[i])] + 1
      } else {
        letterCount[string(word[i])] = 1
      }
    }
    // get count of letters for each word in array
    for j := 0; j < len(words); j++ {
      countTemp := make(map[string]int)
      for i :=0; i < len(words[j]); i++ {
          if _, ok := countTemp[string(words[j][i])]; ok {
            countTemp[string(words[j][i])] = countTemp[string(words[j][i])] + 1
          } else {
            countTemp[string(words[j][i])] = 1
          }
      }
      // deep compare maps to see if equal
      if reflect.DeepEqual(countTemp, letterCount) {
        returnWords = append(returnWords, words[j])
      }
    }
  return returnWords
}
```
