# Broken GPS
```
Written by: Disha and Shray

Ella is following a broken GPS. The GPS tells her to move in the opposite direction than the one she should be travelling in to get to her destination, and she follows her GPS exactly. For instance, every time she is supposed to move west, the GPS tells her to move east and she does so. Eventually she ends up in a totally different place than her intended location. What is the shortest distance between these two points? Assume that she moves one unit every time a direction is specified. For instance, if the GPS tells her to move "north," she moves one unit north. If the GPS tells her to move "northwest," then she moves one unit north and one unit west.

Input Format:
You will receive a text file with N directions provided to her by the GPS (the ones that she will be following) (1<=N<=1000). The first line in the file will be N, and each consequent line will contain a single direction: “north,” “south,” “east,” “west,” “northwest,” “northeast,” “southwest,” or “southeast.”

Output Format:
Round your answer to the nearest whole number and then divide by 26. Discard the quotient (mod 26). Each possible remainder corresponds to a letter in the alphabet. (0=a, 1=b… 25=z).

Find the letter for each test case and string them together. The result is the flag. (For instance, a, b, c becomes “abc”). Remember to use the flag format and keep all letters lowercase!
```
[input.zip](input.zip)

After reading these **bunch of text**, it will give us input (direction)

We can convert them into `x` and `y` coordinates
```
If is north, y + 1
south, y - 1
east x + 1
west x - 1
northeast y + 1, x + 1
southwest y - 1, x - 1
etc...
```
Then calculate the distance, calculate the letter:
```
distance = sqrt((2x)^2 + (2y)^2) (2x and 2y because both x and y are same)
flag = distance % 26
```
[Full python script](solve.py)

**Result:** `garminesuckz`

# Flag
> hsctf{garminesuckz}