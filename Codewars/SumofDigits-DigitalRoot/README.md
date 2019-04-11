# Sum of Digits / Digital Root

language: python3.4

## Instructions
In this kata, you must create a digital root function.
  
A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
  
Here's how it works:
  
```
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
```

## Solution

```python
def digital_root(n):
    if n<10:
        return n
    total = 0
    while n>9:
        tmp = n%10
        n = int(n/10)
        total = total + tmp
    total = total+n
    if total <10:
        return total
    else:
        return digital_root(total)
```

## Sample Tests

```
test.assert_equals( digital_root(16), 7 )
test.assert_equals( digital_root(456), 6 )
test.assert_equals( digital_root(942), 6 )
test.assert_equals( digital_root(132189), 6 )
test.assert_equals( digital_root(493193), 2 )
```

## Best Practices

```python
def digital_root(n):
    while n>9:
        n=sum(map(int,str(n)))
    return n
```
