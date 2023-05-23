"""
Debugging by using assertions :

"""

'''

def squareIt(x) :
	return x**x

print(squareIt(2))
print(squareIt(3))
print(squareIt(4))


=>>
4
27
256

'''

'''

def squareIt(x) :
	return x**x


assert squareIt(2)==4, 'the square of 2 must be 4'

assert squareIt(3)==9, 'the square of 3 must be 9'

assert squareIt(4)==16, 'the square of 4 must be 16'

print(squareIt(2))
print(squareIt(3))
print(squareIt(4))



=>> 
Traceback (most recent call last):
  File "D:__________02.py", line 31, in <module>
    assert squareIt(3)==9, 'the square of 3 must be 9'
           ^^^^^^^^^^^^^^
AssertionError: the square of 3 must be 9

'''




def squareIt(x) :
	return x**2


assert squareIt(2)==4, 'the square of 2 must be 4'

assert squareIt(3)==9, 'the square of 3 must be 9'

assert squareIt(4)==16, 'the square of 4 must be 16'

print(squareIt(2))
print(squareIt(3))
print(squareIt(4))


'''
=>>
4
9
16

'''


"""
Exception Handling vs Assertions =>>

- Assertions concept can be used to alert programmer to resolve development time errors.
- Exception Handling can be used to handle runtime errors

"""