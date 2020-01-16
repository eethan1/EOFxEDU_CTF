import struct
a = open('aaa','wb')


a.write(struct.pack('<i',0x71222222))