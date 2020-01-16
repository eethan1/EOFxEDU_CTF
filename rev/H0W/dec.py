import struct
def rotl(int_value, k, bit=32):
    bit_string = '{:0%db}' % bit
    bin_value = bit_string.format(int_value)
    bin_value = bin_value[k:] + bin_value[:k]
    int_value = int(bin_value,2)
    return int_value


def rotr(int_value, k, bit=32):
    bit_string = '{:0%db}' % bit
    bin_value = bit_string.format(int_value)
    bin_value = bin_value[-k:] + bin_value[:-k]
    int_value = int(bin_value,2)
    return int_value

orig = open('output_orig.txt', 'rb').read()
print(len(orig))
decf = open('plain.png','wb')

def f0(a):
    return a ^ 0xFACEB00C;

def f1(a):
    return a - 74628;

def f2(a1):
    return rotr(a1 & 0xAAAAAAAA, 2) | rotl(a1 & 0x55555555, 4);

def f3(a):
    return f0(f1(f2(a)))
print(orig[0:4])
for i in range(0, 937422, 4):
    a = 0
    rand = int(input())
    #int.from_bytes(orig[i:i + 4],'little')
    if rand%4 == 0:
        a = f0(struct.unpack('<I', orig[i:i + 4])[0])
    elif rand%4 == 1:
        a = f1(struct.unpack('<I', orig[i:i + 4])[0])
    elif rand%4 == 2:
        a = f2(struct.unpack('<I', orig[i:i + 4])[0])
    elif rand%4 == 3:
        a = f3(struct.unpack('<I', orig[i:i + 4])[0])
    if a < 0:
        a = a &  0xffffffff
    try:
        decf.write(struct.pack('<I',a))
    except:
        print(a)