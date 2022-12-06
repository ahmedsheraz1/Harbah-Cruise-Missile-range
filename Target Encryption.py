Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import os
from hashlib import blake2b
msg = b'some message'
salt1 = os.urandom(blake2b.SALT_SIZE)
h1 = blake2b(salt=salt1)
h1.update(msg)
salt2 = os.urandom(blake2b.SALT_SIZE)
h2 = blake2b(salt=salt2)
h2.update(msg)
h1.digest() != h2.digest()
True
