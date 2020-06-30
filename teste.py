import logging

logging.basicConfig(filename='logfile.log',level=logging.INFO,
format='%(asctime)s:%(levelname)s:%(message)s')





# Logs
logger.debug('A debug messssage')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')