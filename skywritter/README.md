# Skywriting v2
```
Written by: NotDeGhost

Fortnite Battle Royale contains a variety of weapons and this page lists every weapon in Fortnite along with their weapon stats like damage, DPS, fire rate, magazine size, and reload speed.

Note: This was a throwback to the original skywriting which included many big leaps of intuition.

This problem has now been modified to make it more doable.

Hint 1: I like xoring together the names of "Rifle"s together. Hint 2: Try googling the first sentence of this problem.

Flag: LjUlMiA9LxI1GTUTNiodECAtUSx5YxY4
```
Disappointed with this challenge...

I saw the hint it gave us:
```
From each name derives a key, equal to chr * len(name) where chr is some char and name is the name. XOR all the keys w/ the cipher to get the flag.
```
So I used python to brute force the key:
```python
from pwn import xor
import string
text = 'LjUlMiA9LxI1GTUTNiodECAtUSx5YxY4'.decode('base64')
for i in string.ascii_letters:
	print xor(text,i),i
```
Result:
```
...
hsctf{iTs_sUpl[Vfkj?%P~ F
...
```
Found part of the flag with `F` as key

`iTs_sUp` is correct I guess, next two letter should be `er`

Modify the script to brute force next part of flag:
```python
for i in string.ascii_letters:
	print xor(text[13:],i),i
```

Result:
```
...
eR_obc6,Yw O 
...
```
Combine both together become : `hsctf{iTs_sUpeR_ob`

The whole flag should be something like : `hsctf{iTs_sUpeR_obViOus}`

Couldn't find next part of key, I just brute force it at the CTF website

And the whole key is pretty weird : `FFFFFFFFFFFFFOOOOO\x07E\x16\x16EE`

## Flag
> hsctf{iTs_sUpeR_obViouS}