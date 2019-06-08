from pwn import xor,remote
p = remote('crypto.hsctf.com',8111)
p.recvuntil("Here is my super secret message: ")
enc_flag = p.recvuntil("\n")[:-1].decode('hex')
p.sendlineafter("Enter the message you want to encrypt: ",'f'*53)
p.recvuntil("Encrypted: ")
encrypted = p.recvuntil("\n")[:-1].decode('hex')
key = xor(encrypted,'f'*53)
flag = xor(enc_flag,key)
print flag