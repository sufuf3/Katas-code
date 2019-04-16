# Format a string of names like 'Bart, Lisa & Maggie'.

language: python3.4

## Instructions

Given: an array containing hashes of names
  
Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
  
Example:
  
```
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
```

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

## Solution

```python
def namelist(names):
    str = ""
    for i in names:
        if len(names)>1 and i['name'] == names[-2]['name']:
            str = str+i['name']+" & "
        elif i['name'] == names[-1]['name']:
            str = str+i['name']
        else:
            str = str+i['name']+", "
    return str
```

## Sample Tests

```
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
"Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
"Must work with two names")
Test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
Test.assert_equals(namelist([]), '', "Must work with no names")
```


## Best Practices

```python
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
```
