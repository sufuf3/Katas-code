# You're a square!


language: python3.4

## Instructions
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!
  
However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.
  
Task  
Given an integral number, determine if it's a square number:
  
> In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
  
The tests will always use some integral number, so don't worry about that in dynamic typed languages.
  
Examples
  
```
is_square (-1) # => false
is_square   0 # => true
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false
```
```
isSquare(-1) returns  false
isSquare(0) returns   true
isSquare(3) returns   false
isSquare(4) returns   true
isSquare(25) returns  true  
isSquare(26) returns  false
```

## Solution

```python
def is_square(n):
    if n ==0:
        return True
    elif n<0:
        return False
    else:
        for i in range(0,2147483647):
            if i*i>n:
                break
            elif i*i==n:
                return True
        return False
```

## Sample Tests

```
test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
test.assert_equals(is_square( 0), True, "0 is a square number (0 * 0)")
test.assert_equals(is_square( 3), False, "3 is not a square number")
test.assert_equals(is_square( 4), True, "4 is a square number (4 * 4)")
test.assert_equals(is_square(25), True, "25 is a square number (5 * 5)")
test.assert_equals(is_square(26), False, "26 is not a square number")
```

## Best Practices

```python
import math
def is_square(n):
    if n < 0:
        return False
    sqrt = math.sqrt(n)
    return sqrt.is_integer()
```

> sqrt(): 返回数字x的平方根
