# uncompyle6 version 3.6.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Jul  3 2019, 15:36:16) 
# [GCC 5.4.0 20160609]
# Embedded file name: H0W.py
# Size of source mod 2**32: 387 bytes
import sys, struct
from terrynini import *
if len(sys.argv) != 2:
    print('Usage: python3 H0W.py filename')
    exit(0)
nini3() # jetbrain = open(outpu.txt,w)
f = open(sys.argv[1], 'rb').read()
if len(f) % 4 != 0:
    f += (4 - len(f) % 4) * '\x00'
nini1() # github=time()
nini4() # srand(github)
for i in range(0, len(f), 4):
    nini6(nini5(struct.unpack('<i', f[i:i + 4])[0]))
print(nini2())
for i in list(map(ord, nini2())):
    print(i)
    nini6(i)
20190803052514
print('Complete')
# okay decompiling H0W.pyc