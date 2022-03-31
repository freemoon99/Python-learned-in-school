Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
my_tuple = ("one", "two", "three", "four")
print(my_tuple[0])
one
print(my_tuple[1])
two
print(my_tuple[2])
three
print(my_tuple[3])
four

=========== RESTART: C:/Users/pkh/Desktop/객체지향 파이썬 코딩/myMagic8Ball.py ==========
Welcome to MyMagic8Ball.
Ask me for advice then press ENTER to shake me.
print(my_tuple[2])
shaking...
shaking...
shaking...
shaking...

Traceback (most recent call last):
  File "C:/Users/pkh/Desktop/객체지향 파이썬 코딩/myMagic8Ball.py", line 21, in <module>
    print(answers[choice])
TypeError: 'set' object is not subscriptable

=========== RESTART: C:/Users/pkh/Desktop/객체지향 파이썬 코딩/myMagic8Ball.py ==========
Welcome to MyMagic8Ball.
Ask me for advice then press ENTER to shake me.
et' object is no
shaking...
shaking...
shaking...
shaking...

No way, Jose!
Traceback (most recent call last):
  File "C:/Users/pkh/Desktop/객체지향 파이썬 코딩/myMagic8Ball.py", line 23, in <module>
    imput("\n\nPress the RETURN key to finish.")
NameError: name 'imput' is not defined. Did you mean: 'input'?


=========== RESTART: C:/Users/pkh/Desktop/객체지향 파이썬 코딩/myMagic8Ball.py ==========
Welcome to MyMagic8Ball.
Ask me for advice then press ENTER to shake me.
Ask me for advice then press ENTER to shake me.
shaking...
shaking...
shaking...
shaking...

Yes, I think on balance that is the right choice.


Press the RETURN key to finish.

s = "bar" # a string
t = ("b", "a", "r") # a tuple
1 = ["b", "a", "r"] # a list
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
I = ["b", "a", "r"] # a list
d = {1:"b", 2:"a", 3:"r"} # a dictionary

print(s)
bar
print(s[2])
r
a=s+"f"
a
'barf'
i.find("b")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    i.find("b")
NameError: name 'i' is not defined. Did you mean: 'I'?
i.find("b")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    i.find("b")
NameError: name 'i' is not defined. Did you mean: 'I'?
I.find("b")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    I.find("b")
AttributeError: 'list' object has no attribute 'find'
L.find("b")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    L.find("b")
NameError: name 'L' is not defined
L.find("b")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    L.find("b")
NameError: name 'L' is not defined
l.find("b")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l.find("b")
NameError: name 'l' is not defined
I.find("b")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    I.find("b")
AttributeError: 'list' object has no attribute 'find'
i = ["b", "a", "r"] # a list

i.find("b")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    i.find("b")
AttributeError: 'list' object has no attribute 'find'
s.find("b")
0
len(s)
3

print(t)
('b', 'a', 'r')
print(t[2])
r
a=t+("f",)
a
('b', 'a', 'r', 'f')
t.index("b")
0
len(t)
3
print(1)
1
print(i)
['b', 'a', 'r']
print(i[2])
r
a=i+["f"]
a
['b', 'a', 'r', 'f']
i.append("f")
i
['b', 'a', 'r', 'f']
i.sort()
i
['a', 'b', 'f', 'r']
i.sort()
i
['a', 'b', 'f', 'r']
del i[1]
1
1
del i[1]
io
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    io
NameError: name 'io' is not defined. Did you mean: 'i'?
del i[1]
i
['a']
i[0]="c"
i
['c']
i.index("b")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    i.index("b")
ValueError: 'b' is not in list
len(i)
1
print(d)
{1: 'b', 2: 'a', 3: 'r'}
print(d[2])
a
d[4]="f"
d[4]
'f'
sorted(d)
[1, 2, 3, 4]
sorted(d.values())
['a', 'b', 'f', 'r']
del d[1]
i
['c']
d[1]="c"
print(d)
{2: 'a', 3: 'r', 4: 'f', 1: 'c'}
len(d)
4
