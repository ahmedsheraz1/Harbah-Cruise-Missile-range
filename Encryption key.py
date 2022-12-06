Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the sea skimming repetition")
m.digest()
b'\xc6b\xc3s\xf1\xe1\x97\x03\xa6\xcb \x89\xea\xe0@\x99\x99\xeb\x92\xa4e\x11\xa5\xf0\x89\x87\xf8l5\x90\t}'
m.hexdigest()
'c662c373f1e19703a6cb2089eae0409999eb92a46511a5f08987f86c3590097d'

