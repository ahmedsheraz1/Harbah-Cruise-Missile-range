Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import ssl
timestamp = ssl.cert_time_to_seconds("Jan  5 09:34:43 2018 GMT")
timestamp
1515144883
from datetime import datetime
print(datetime.utcfromtimestamp(timestamp))
2018-01-05 09:34:43
ssl.OPENSSL_VERSION_NUMBER
269488351
hex(ssl.OPENSSL_VERSION_NUMBER)
'0x101010df'
