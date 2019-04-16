# Build Tower

language: python3.4

## Instructions

Build Tower by the following given argument:  
number of floors (integer and always greater than 0).  
  
Tower block is represented as *  
  
Python: return a list;  
JavaScript: returns an Array;  
C#: returns a string[];  
PHP: returns an array;  
C++: returns a vector<string>;  
Haskell: returns a [String];  
Ruby: returns an Array;  
Have fun!  
  
for example, a tower of 3 floors looks like below  
```
[
  '  *  ', 
  ' *** ', 
  '*****'
]
```
and a tower of 6 floors looks like below  
```
[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
```
Go challenge Build Tower Advanced once you have finished this :)  


## Solution

```python
def tower_builder(n_floors):
    array = []
    for i in range(0,n_floors):
        array.append(' '*(n_floors-i-1))
        array[i] = array[i]+'*'*(2*i)+'*'
        array[i] = array[i]+' '*(n_floors-i-1)
    return array
```

## Sample Tests

```
test.describe("Tests")
test.it("Basic Tests")
test.assert_equals(tower_builder(1), ['*', ])
test.assert_equals(tower_builder(2), [' * ', '***'])
test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])
```

## Best Practices

```python
def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
       tower.append(' '*(n_floors-i-1) + '*'*(2*i+1) + ' '*(n_floors-i-1))
    return tower
```
