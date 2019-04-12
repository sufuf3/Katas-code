# Find the odd int

language: python3.4

## Instructions

Given an array, find the int that appears an odd number of times.
  
There will always be only one integer that appears an odd number of times.
  


## Solution

```python
def find_it(seq):
    dict = {}
    for i in seq:
        if i in dict:
            dict[i]= dict[i]+1
        else:
            dict[i]=1
    for key, value in dict.items():
        if value%2==1:
            return key
            break
    return None
```

## Sample Tests

```
test.describe("Example")
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
```

## Best Practices

```python
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
```
