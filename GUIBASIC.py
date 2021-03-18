Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Sawasdee(name):
	print('hello'+name)
	print('สบายดีไหม'+name)

	
>>> Sawasdee(Lonng)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Sawasdee(Lonng)
NameError: name 'Lonng' is not defined
>>> Sawasdee('Lonng')
helloLonng
สบายดีไหมLonng
>>> Sawasdee('mos')
hellomos
สบายดีไหมmos
>>> 
= RESTART: C:/Users/kodch/OneDrive/Desktop/Uncle Engineer/Python Bootcamp/helloworld.py
Hello World
Hello World
Hello World
>>> 
= RESTART: C:/Users/kodch/OneDrive/Desktop/Uncle Engineer/Python Bootcamp/helloworld.py
Hello John
Hello Robert
Hello Smith
>>> 
= RESTART: C:/Users/kodch/OneDrive/Desktop/Uncle Engineer/Python Bootcamp/helloworld.py
Hello John
Hello Robert
Hello Smith
>>> print(name)
David
>>> print(lastname)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(lastname)
NameError: name 'lastname' is not defined
>>> 
= RESTART: C:/Users/kodch/OneDrive/Desktop/Uncle Engineer/Python Bootcamp/helloworld.py
Hello John
Hello Robert
Hello Smith
>>> print(lastname)
Takeshi
>>> import math
>>> print(math.pi)
3.141592653589793
>>> print(math.square)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(math.square)
AttributeError: module 'math' has no attribute 'square'
>>> math.pow(2,3)
8.0
>>> from math import pow
>>> pow(2,3)
8.0
>>> 
