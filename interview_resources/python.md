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

# join / split / replace
' '.join(['these', 'are', 'words']) = 'these are words'
'these are words'.split() = ['these', 'are', 'words'] # split on whitespace
'banana'.split('a') = ['b', 'n', 'n', ''] # split on 'a'
'banana'.replace('a', '@') = 'b@n@n@' # replace 'a's with '@'s
```

# Integers

# Floats

# Lists
```
my_list[i:j:z] # i -> starting index, j -> ending index, z -> stride

[0, 1, 'a'][0] = 0 # get first element
[0, 1, 'a'][-1] = 'a' # get last element
[0, 1, 'a', 5.0, 'f'][2:4] = ['a', 5.0] # elements between position 2 (inclusive) and 4(exclusive)
[0, 1, 2, 3, 4][3:] = [3, 4] # elements from position 3 to the end
[0, 1, 2, 3, 4][::2] = [0, 2, 4] # every other element
[0, 1, 2, 3, 4][0:4:2] = [0, 2] # elements from position 0 to 4, taking every other element
[0, 1, 2, 3, 4][::-1] = [4, 3, 2, 1, 0] # reverse list
[1,2] * 2 = [1, 2, 1, 2] # multiply list

my_list = [1, 2, 3, 4]
my_list.pop() = 4 # pop removes last item in list my_list now equals [1, 2, 3]
[1, 2, 3, 4].pop(2) = 3 # removes element at specified index

# can also use delete
my_list = [1, 2, 3, 4]
del my_list[1:3] # my_list = [1,4]

# appending
my_list = [1, 2]
my_list.append(3) = [1, 2, 3]
```

# Booleans

# Tuples

# Dictionaries
```
my_dict = {'a':1, 'b': 2, 'c': 3}

# iterating through dict
for key, value in my_dict.items():
    print(key, value)

# removing item w/ pop (pop will return removed value unlike del)
my_dict.pop('b') # supplying a key is required

# removing item w/ del
del my_dict['b']
```


