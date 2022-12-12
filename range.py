Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
26932
a[1:3]
array('H', [10, 700])
