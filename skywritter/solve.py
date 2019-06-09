from pwn import xor
import string
text = 'LjUlMiA9LxI1GTUTNiodECAtUSx5YxY4'.decode('base64')
known = 'hsctf{iTs_sUpeR_obViouS}'
key = 	'FFFFFFFFFFFFFOOOOO\x07E\x16\x16EE'
for i in string.ascii_letters:
	print xor(text[13:],i),i
# print xor(text,key)