import logging

user_1 = 'John'
user_2 = 'Boris'

#only works on Python 3.9
logging.basicConfig(filename='/home/fraz/my_repos/github/Python/logging/example.log', 
                    encoding='utf-8', 
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

#root_logger = logging.getLogger()
#root_logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler('/home/fraz/my_repos/github/Python/logging/example.log', 'w', 'utf-8')
#root_logger.addHandler(handler)

logging.warning('Watch out!')  # will print a message to the console
logging.error('another error')   # will print a message to the console
logging.critical('Its critical')   # will print a message to the console

logging.info('I told you so')  # will not print anything
logging.debug('Watch out beadles about!')  # will not print anything

##using variables
logging.error('user %s does not have admin rights', user_1)
logging.error(f'{user_2} is a muppet!')