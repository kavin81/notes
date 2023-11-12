### Program questions on Input, Output, and Operators:


1) Write a Python program that checks if a given non-negative integer from the user, is a
palindrome. A palindrome is a number that remains the same when its digits are reversed. For
example, `121` is a palindrome because it reads the same forward and backward, whereas `1231`
is not a palindrome.

Answer:

```py
a = int(input("give int as input:"))
b = int(str(a)[::-1])
print(a == b)
```


2) Write a program that takes number of rows ‘n’ as input and prints the following pattern. For
`n=4`, it is,

```
1
121
12321
1234321
```

Answer:

```py
n = int(input("Enter the number of rows (n): "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
```

3) Write a program that takes number of rows ‘n’ as input and prints the following pattern, for
`n=4`, it is,
```
###1
##21
#321
4321
```

Answer:

```py
n = 4
rng = list(range(1, n + 1))[::-1]
while n > 0:
    x1 = "#" * (n - 1)
    x2 = -"".join([str(x) for x in rng[n - 1 :]])
    print(x1 + x2)
    n -= 1
```

4) Write a program that takes number of rows ‘n’ as input and prints the following pattern, for
`n=4`, it is,
```
1
10
101
1010
```

Answer:

```py
n = int(input("enter `n` rows:"))
if n % 2 == 0:
    print("10" * (n // 2))
else:
    print("10" * (n // 2) + "1")
```

### Lists and tuples and their Combinations:


5) Write a program that takes an integer 'n' as the number of elements to be inserted inside a list.
Accept the integer elements for list from the user and an integer 'k' as the desired occurrence
frequency from the user. The program should remove all elements that do not occur exactly
'k' times within the list and print the resulting modified list.
Eg: `n=7`, `input_lst=[10,20,20,30,40,10,50]`, `k=2` `Output=[20,20,10,10]`

Answer:

```py
n = [1, 2, 3, 4, 1, 2]  # input
k = 2  # fixed freq
a = {x: n.count(x) for x in set(n)}
a = [ele for ele, freq in a.items() if freq == k]
print(a)
```

6) Write a program that takes integer 'n' as the number of elements to be inserted inside a list.
Accept the integer elements for list, and position 'k' from the user. The program's objective is
to find and display the k-th smallest number from the list. It is important to note that the
numbers in the list may be repeated, and a simple sorting approach may not yield the correct
result. The program should handle this case by considering the frequency of each number.
Eg1: `n=6`, `lst1=[20,7,15,16,7,8]`, `k=3` `output=15`
Eg 2: `n=5`,`lst1=[5,4,19,9,18]`, `k=8` `output=None`

Answer:

```py
n = [1, 1, 3, 2] # input
k = 2 # input

print(list(set(sorted(n)))[k - 1])
```

7) Write a program that takes integer 'n' as the number of elements to be inserted inside a list,
and the integer elements for list from the user. Modify each element of a list by replacing it
with the sum of the next two elements. Assume the list is circular, so the last element will be
the sum of the elements at `index[0]` and `index[1]`.
Eg1: `n=4`,`lst1=[1,2,3,4]` `output=[5,7,5,3]`
Eg2: `n=2`, `lst1=[100,200]`, `output=[300,300]`

Answer:

```py
n_og = [1, 2, 3]  # input
n = []

for k, v in enumerate(n_og):
    try:
        v = n_og[k + 1] + n_og[k + 2]
        n.append(v)
    except IndexError:
        v = n_og[-(len(n_og) - k) + 1] + n_og[-(len(n_og) - k) + 2]
        n.append(v)
```

8) Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
integers from the user and prints the average of the elements along the main diagonal of the
2D list(nested list).
Eg 1: `row_ col= 3`, `input_lst1=[[1,2,3],[4,5,6],[7,8,9]]`, `output= 5.0` (i.e. (1 + 5 + 9) / 3 =5.0)

Answer:
```py
lst_2d = <2d list> # TODO: input of list
res = sum([val[idx] for idx, val in enumerate(lst_2d)]) / len(lst_2d)
```

9) Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
integers from the user and print the transpose of the 2D list(nested list/like matrix).
Eg 1:- `row_col=3` `input_lst1= [[1, 5],[2, 7]]` `Output= [[1, 2],[5, 7]]`

Answer:

```py
lst_2d = <2d list> # TODO: input of list
res = [[] for x in lst_2d]

for idx,val in enumerate(lst_2d):
    i = 0
    for x in val:
        res[i].append(x)
        i += 1

print(res)
```

### Program questions on Combination of Sets, Dictionaries and Strings using functions:

10) Write a program that takes a sentence as input and converts each alphabet in a given sentence
to the next letter in the alphabet, while preserving the case of the letters. For example, a is
converted to b, b to c, so on and z to a. (ignore punctuations in the input sentence) Eg:
`inp_str=”Welcome to python”` `output=”Xfmdpnf up qzuipm”`

Answer:

```py
# TODO: if time permits make it shorter
a,b = "Welcome to python",str()

for x in a:
    if x.isalpha():
        if x == "x":
            b += "A"
        elif x == "X":
            b += "A"
        else:
            b += chr(ord(x) + 1)
    else:
        b += x
print(b)
```

11) Write a program to take inputs of different data type as key input and then the value as its
data_types name (i.e,. “string”, “integer” or “float”). Store the values in a dictionary with key
as input and value as data type. Make a sentence with all the inputs which are of string data
type and display the same. For example, for the dictionary `{"hello":"string", 5:"integer",
“world”: “string”}` the sentence is "hello world".

Answer:

```py
n = int(input("enter no.of inputs in dict"))
a = dict()
while n > 0:
    k = input("enter key")
    v = input("enter data-type")
    a[eval(v)(k)] = v
    n -= 1

a = " ".join([k for k, v in a.items() if v == "str"])
print(a)

```

12) Write a python program that accepts two inputs as word from the user and checks if two
words are anagrams of each other. An anagram is a word or phrase formed by rearranging the
letters of another.
Eg 1: `inp_string 1: anagram` `inp_string 2: nagaram` , `Output: True`
Eg 2: `inp_string 1: baseball`, `inp_string 2: basketball` , `Output: False`

Answer:

```py

w1 = input("enter word1:").replace(" ","").lower()
w2 = input("enter word2:").replace(" ","").lower()

print(sorted(w1)==sorted(w2))
```

13) Write a program that accepts word as input from the user and translates that word into Pig
Latin. In Pig Latin, words are transformed by moving the first letter to the end and adding
"ay." For example, "hello" becomes "ellohay."

Answer:

```py
a = "hello" # input of string
a = list(a)
a += a.pop(0)
print("".join(a) + "ay")

```

14) A cipher is a method of transforming a message to conceal its meaning. The simplest
technique involves shifting the letters in the message by a certain number of positions, known
as the “shift” or “key”. Given a message and an integer shift value, print the encrypted
message. For instance, Encryption - If shift value is 2, A becomes C, B becomes D etc. Z
cycles back and becomes B.
Eg1: `inp_str=”Hello world”` , `shift_value=3`, `Output= Khoor zruog`
Eg2: `inp_str=” Zero to hero!”` , `shift_value=1`, `Output= Afsp up ifsp!`

Answer:

```py
a, b = "Hello world", str() # input , str()
n = 3 # shift_value
for x in a:
    if x.isalpha():
        if x == "x":
            b += "A"
        elif x == "X":
            b += "A"
        else:
            b += chr(ord(x) + n)
    else:
        b += x
print(b)

```

15) Write a Python program that takes a string as input, finds and prints all the unique substrings
of the given string in a list in lexicographical order.

Answer:

```py
st = "hello world"
from itertools import permutations

perms = ["".join(p) for p in permutations(st)]
print(list(set(sorted(perms))))
```