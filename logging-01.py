"""

logging the exceptions : (to store flow of the operation)

=>> it is highly recommended to store complete application flow and exceptions information
	to a file, this process is called logging.

=>> the main advantages of logging are :
	- we can use log files while performing debugging
	- we can provide statistics like number of requests per day etc

=>> to implement logging, python provides one inbuilt module logging :

logging levels =>> 
		depending on type of information, logging data is divided according to the following 6
		levels in python :

1. CRITICAL : 50 : represents a very serious problem that needs high attention
				=> (represented by number : 50)

2. ERROR : 40 : represents a serious error

3. WARNING : 30 : represents a warning message, some caution needed (it is alert to the programmer)

4. INFO : 20 : represents a message with some important information

5. DEBUG : 10 : represents a message with debugging information

6. NOTSET : 0 : represents that the level is not set


## How to implement logging : 

- to perform logging, first we required to create a file to store messages and we have to
	specify which level messages we have to store.

- we can do this by using basicConfig() function of logging module..

=>> logging.basicConfig(filename='log.txt',level=logging.WARNING)

	- the above line will create a file log.txt and we can store either WARNING level or higher
		level messages to that file.

=>> After creating log file, we can write messages to that file by using the following methods :

logging.debug(message)
logging.info(message)
logging.warning(message)
logging.error(message)
logging.critical(message)

"""

'''

import logging

logging.basicConfig(filename='log01.txt', level=logging.WARNING)
print('python logging demo')
logging.debug('debugging message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')



in the above program only WARNING and higher level messages will be written to log file,
if we set level as DEBUG then all messages will be written to log file...

=>> output :
python logging demo

log01.txt  =>> 

WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message




import logging

logging.basicConfig(filename='log01.txt')
print('python logging demo')
logging.debug('debugging message')
logging.info('info message')
logging.warning('warning message 88')
logging.error('error message')
logging.critical('critical message')


=>> output :
python logging demo

log01.txt  =>> 

WARNING:root:warning message 88
ERROR:root:error message
CRITICAL:root:critical message

'''