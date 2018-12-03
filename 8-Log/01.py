import logging

LOG_FORMAT = '%(asctime)s     %(levelname)s     %(message)s'

logging.basicConfig(filename='marlon.log',level=logging.DEBUG,format=LOG_FORMAT)
print('-*-'*10)

# 写法一
logging.debug('This is e debug log')
logging.info('This is a info log')
logging.warn('This is a warn log')
logging.error('This is a error log')
logging.critical('This is a critial log')

print('-*-'*10)

# 写法二
logging.log(logging.DEBUG, 'debug')
logging.log(logging.INFO, 'info')
logging.log(logging.WARN, 'warn')
logging.log(logging.ERROR, 'error')
logging.log(logging.CRITICAL, 'critial')





