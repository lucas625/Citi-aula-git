from .base import *
Debug = False

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#seta https o redirecionamento, mas não deixa exatamente https