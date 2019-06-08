# Super Secure System
Description
```
Written by: Tux

Keith made a SUPER SECURE SYSTEM!!! He claims it is so secure as long as he doesn't reuse his key...

nc crypto.hsctf.com 8111
```
Netcat to it:
```
* * * SUPER SECURE SYSTEM * * *
My encryption system is impossible to crack if used once!
You can use this system to encrypt any of your messages with my super special key!!!
Here is my super secret message: 19365a28254c3b6f32244b5d2a125f55561d0c0e19685740787e0136504679277d4012730f1354464d60592f52676f4015642f5a32

Enter the message you want to encrypt:
```
Testing with the encryption method:
```
Enter the message you want to encrypt: a

Encrypted: 10

aEnter the message you want to encrypt: a

Encrypted: 1024

Enter the message you want to encrypt: aaa

Encrypted: 102458

Enter the message you want to encrypt: aaaa

Encrypted: 1024583d
```
After a few testing, the encrypted text length is same as the plaintext (original text)

I guess the encryption algorithm is using XOR (Exclusive OR):
```
Example (In binary):
1 xor 1 = 0
1 xor 0 = 1
0 xor 1 = 1
0 xor 0 = 0
``` 
What special about XOR is the encryption method is same as decryption method:
```
Example:
Assume 6 is the key
(Encryption)
19 xor 6 = 21	10011	19
				  110	 6
				-----
				10101	21
(Decryption)
21 xor 6 = 19	10101	21
				  110	 6
				-----
				10011	19
```
In this case, we don't know the key.

But we can encrypt text with the same key, then finding the key is easy!
```
Example:
Assume 19 is flag, 6 is key
19 xor 6 = 21	10011	19
				  110	 6
				-----
				10101	21 (Encrypted flag)

I type 24, then it show me encrypted text
24 xor 6 = 30	11000	24
				  110	 6
				-----
				11110	30 (Encrypted text)

I use 30 xor 24 to find the key
30 xor 24 = 30	11110	30
				11000	24
				-----
				00110	 6 (Key found)

I use the key to get flag
21 xor 6 = 19	10101	21
				  110	 6
				-----
				10011	19 (Flag)
```
Easy right?

Now we need to count the encrypted message length:
```
>>> len("19365a28254c3b6f32244b5d2a125f55561d0c0e19685740787e0136504679277d4012730f1354464d60592f52676f4015642f5a32")/2
53
```
Then we need to input 53 characters to find the key, because key and message must be same length

I wrote a [python script](solve.py) to solve it!
```python
from pwn import xor,remote
p = remote('crypto.hsctf.com',8111)
p.recvuntil("Here is my super secret message: ")
enc_flag = p.recvuntil("\n")[:-1].decode('hex')
p.sendlineafter("Enter the message you want to encrypt: ",'f'*53)
p.recvuntil("Encrypted: ")
encrypted = p.recv()[:-2].decode('hex')
key = xor(encrypted,'f'*53)
flag = xor(enc_flag,key)
print flag
```
## Result
```
[x] Opening connection to crypto.hsctf.com on port 8111
[x] Opening connection to crypto.hsctf.com on port 8111: Trying 134.209.219.179
[+] Opening connection to crypto.hsctf.com on port 8111: Done
hsctf{h0w_d3d_y3u_de3cryP4_th3_s1p3R_s3cuR3_m355a9e?}
[*] Closed connection to crypto.hsctf.com port 8111
```
# Flag
> hsctf{h0w_d3d_y3u_de3cryP4_th3_s1p3R_s3cuR3_m355a9e?}