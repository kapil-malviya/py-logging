"""
Debugging :

	(DEBUGGING BY USING ASSERTIONS)


  - the process of identifying and fixing the bug is called debugging..

=>> the very comman way of debugging is to use print() statement, but the problem
	 with the print() statement is after fixing the bug, compulsory we have to 
	 delete the extra added print() statements otherwise these will be executed 
	 at runtime which creates performance problems and disturbs console output..

  - to overcome this problem we should go for assert statement, the main advantage
  	of assert dtatement over print() statement is after fixing bug we are not 
  	required to delete assert statement, based on our requirement we can enable 
  	or disable assert statements..

  - hence the main purpose of assertion is to perform debugging, usually we can 
    perform debugging either in development or in test environments but not in 
    production environment, hence assertion concept is applicable only for 
    development and test environments but not in production environment...


# Types of assert statements =>> 
  - simple version
  - augmented version


1. Simple Version =>> 

	assert conditional_expression


2. Augmented Version =>>

	assert conditional_expression,message

=>> conditional_expression will be evaluated and if it is true then the program will be continued,
	if it is false then the program will be terminated by raising AssertionError..,

	by seeing AssertionError, programmer can analyze the code and can fix the problem...

"""


x=8


assert x>7


assert x>8, 'here x value should be >8 but it is not'


print(x)



'''
output =>> 

Traceback (most recent call last):
  File "D:\file_____________1.py", line 52, in <module>
    assert x>8, 'here x value should be >8 but it is not'
           ^^^
AssertionError: here x value should be >8 but it is not

'''