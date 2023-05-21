
# if we set level as DEBUG then all messages will be written to log file..


import logging

logging.basicConfig(filename='log02.txt',level=logging.DEBUG)
print('python logging demo0')
logging.debug('starts from debugging message')
logging.info('info message')
logging.warning('warning message 88')
logging.error('error message')
logging.critical('till critical message')


'''
=>> output :
python logging demo0

log01.txt  =>> 

DEBUG:root:starts from debugging message
INFO:root:info message
WARNING:root:warning message 88
ERROR:root:error message
CRITICAL:root:till critical message



=>> we can format log messages to include date and time, ip address of the client etc at 
	advanced level.

'''