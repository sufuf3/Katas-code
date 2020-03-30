# Count characters in your string

language: python3.4
`6 kyu`

## Instructions

The main idea is to count all the occurring characters(UTF-8) in string. If you have string like this `aba` then the result should be `{ 'a': 2, 'b': 1 }`

What if the string is empty ? Then the result should be empty object literal `{ }`

For C#: Use a `Dictionary<char, int>` for this kata!


## Solution

```python
def count(string):
    if string == None:
        return {}
    ans = {}
    for i in string:
        if i not in ans.keys():
            ans[i] = 1
        else:
            ans[i] = ans[i]+1
    return ans
```

## Sample Tests

```
test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})
```

## Best Practices

```python
from collections import Counter

def count(string):
    return Counter(string)
```

https://docs.python.org/2/library/collections.html#collections.Counter 
