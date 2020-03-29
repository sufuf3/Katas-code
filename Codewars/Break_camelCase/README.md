# Break camelCase

language: python3.4

`6 kyu`

## Instructions

Complete the solution so that the function will break up camel casing, using a space between words.

Example

```
solution("camelCasing")  ==  "camel Casing"
```

## Solution

```python
def solution(s):
    ans = ""
    for a in s:
        if a == a.upper():
            ans = ans + " " + a
        else:
            ans = ans+a
    return ans
```

## Sample Tests

```
Test.assert_equals(solution("helloWorld"), "hello World")
Test.assert_equals(solution("camelCase"), "camel Case")
Test.assert_equals(solution("breakCamelCase"), "break Camel Case")
```

## Best Practices

```python
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
```
