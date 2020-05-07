# Strings

```
my_str = '123456789'

my_str[i:j:z] # i -> starting index, j -> ending index, z -> stride

my_str[0] = '1' # get first element
my_str[-1] = '9' # get last element
my_str[2:5] = '345' # elements between position 2 (inclusive) and 4(exclusive)
my_str[5:] = '6789' # elements from position 5 to the end
my_str[::2] = '13579' # every other element
my_str[0:6:2] = '135' # elements from position 0 to 6, taking every other element
my_str[::-1] = '987654321' # reverse string

len(my_str) = 9 # length of string

my_str.count('1') = 1 # count number of '1's in string

my_str.find('5') = 4 # find index where '5' occurs in string

my_str = 'tHiS iS a StRIng'

my_str.upper() = 'THIS IS A STRING' # all uppercase
my_str.lower() = 'this is a string' # all lowercase
my_str.isalnum() = False # check if string is all alphanumeric characters
my_str.isalpha() = False # check if string is all alphabetic characters (false due to spaces)
my_str.islower() = False # checks if all characters are lowercase
my_str.isupper() = False # checks if all characters are uppercase
my_str.isnumeric() = False # checks if all characters are numeric

' '.join(['these', 'are', 'words']) = 'these are words'
'these are words'.split() = ['these', 'are', 'words'] # split on whitespace
'banana'.split('a') = ['b', 'n', 'n', ''] # split on 'a'
'banana'.replace('a', '@') = 'b@n@n@' # replace 'a's with '@'s
```

# Integers

# Floats

# Lists

# Booleans

# Tuples

# Dictionaries

