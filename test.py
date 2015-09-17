__author__ = 'titorx'

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d]%(funcName)s %(levelname)s %(message)s',
)


socket_server_log = logging.getLogger('socket')

http_server_log = logging.getLogger('http')

class h:
    def p(self):
        http_server_log.info('123')


p = h()
p.p()
