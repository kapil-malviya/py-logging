"""
	how to write python program exceptions to the log file :

=>> by using the following function we can write exceptions information to the log file,
	- logging.exception(message)

"""

# python program to write exception information to the log file =>> 

import logging

logging.basicConfig(filename='log03.txt', level=logging.INFO)
logging.info('A new request came')

try :
	x = int(input('enter first number : '))
	y = int(input('enter second number : '))
	print(x/y)
	
except ZeroDivisionError as msg :
	print('can not divide a number with zero.,')
	logging.exception(msg)

except ValueError as msg :
	print('enter only int value..')
	logging.exception(msg)

logging.info('request processing completed.')




'''
output =>> 

refer log03.txt

'''