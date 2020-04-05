# The Hashtag Generator

language: python3.4
`5 kyu`

## Instructions

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (`#`).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return `false`.
If the input or the result is an empty string it must return `false`.
Examples
```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```

## Solution

Ans1:

```python
def generate_hashtag(s):
    if s == "":
        return False
    if len(s) > 140:
        return False
    s = s.capitalize()
    ans = ""
    flag = 0
    for i in s:
        if i == " ":
            flag = 1
            continue
        if i.isalpha() and flag == 0:
            ans = ans+ i
        if i.isalpha() and flag == 1:
            ans = ans + i.upper()
            flag = 0
    ans = "#" + ans
    return ans
```

Ans2: 
```python
def generate_hashtag(s):
    if s == "" or len(s) > 140:
        return False
    ans = "#"
    for word in s.split():
        ans += word.capitalize()
    return ans
```

## Sample Tests

```
Test.describe("Basic tests")
Test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
Test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
Test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
Test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
Test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
Test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
Test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
Test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
Test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
Test.assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')
```

## Best Practices

```python
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
```
