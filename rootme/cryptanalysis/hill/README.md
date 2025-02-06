![image](https://github.com/user-attachments/assets/e6b813d7-bd09-412e-8ee6-95d36f8c0d38)

i'm proud of myself.

sooo to what is going on....
we recieve 2 things: ciphertext and alphabet used. we know it's a hill cipher. hill cipher is linear algebra. linear algebra is *fun*.

cipher:
>EgiMbrC7AbHOTyCiRJTU4eWlQwfgK4?fGQvzcjXBBw?NpxK6rv3OsObp?N9vjIqzHC?O9WwOT1VVtu32my2CzNNkHTozl5W,nE7Lm4rBJucP8XezREIuzgl0C7ANnn.561s9jBIYgECq!8XezREBDQ6sOG2i44iQIligvf9.Auk5hgNMuzREcjXzvPWrieWlQwfgK4km0xS?o0tuPB7VJo0t,nOwCUZAyxYyf0LvcfrIFmbPJDoAs9xaJA!cQF8?ffkln7SKO.h CVdc?JqPiAK9c8jt5Ck9ZAyrVP.y13pyC6OdvrN1dkHTseEgnDHQGEfKjBIf90KjAyFNBBwtXMaTZpbycC3HiqFp07SK44inxH5YAvEEml?CKjNQoCJwzNNbHOTyCnE7Lm4uZFCir

alphabet used:
>{'!': 8, ' ': 42, ',': 58, '.': 6, '1': 7, '0': 1, '3': 34, '2': 37, '5': 3, '4': 47, '7': 43, '6': 63, '9': 54, '8': 13, '?': 60, 'A': 35, 'C': 57, 'B': 16, 'E': 31, 'D': 64, 'G': 9, 'F': 23, 'I': 29, 'H': 32, 'K': 55, 'J': 53, 'M': 21, 'L': 5, 'O': 52, 'N': 41, 'Q': 40, 'P': 26, 'S': 22, 'R': 18, 'U': 51, 'T': 15, 'W': 17, 'V': 62, 'Y': 45, 'X': 66, 'Z': 50, 'a': 25, 'c': 38, 'b': 0, 'e': 30, 'd': 33, 'g': 14, 'f': 2, 'i': 10, 'h': 4, 'k': 59, 'j': 39, 'm': 11, 'l': 28, 'o': 12, 'n': 19, 'q': 24, 'p': 49, 's': 46, 'r': 61, 'u': 20, 't': 27, 'w': 36, 'v': 44, 'y': 56, 'x': 48, 'z': 65}

> The encryption key is 3x3 in size; The message, written in English, seems to talk about the method used.

3 things. ok.
firstly, this alphabet contains 67 symbols. 67 is a prime number. nice!
secondly, spase symbol is encrypted aswell, which makes it impossible to just guess where exactly words are. 
well, if the message seems to talk about cipher used, it probably contains string 'Hill cipher' somewhere. what we need to analyse this cipher is at least 9 chars of plaintext, 'Hill ciph'. because there is 3x3 key, you know. 9 chars.
using our new alphabet, we  can encode this as 
``32 10 28 
28 42 38 
10 49 4``
it was multiplied by some other matrix and now is hidden somwhere inside the ciphertext. my first guess was that it was at the wery beginning, turned out to be wrong though. but for this short explanation, let's say that EgiMbrC7A == Hill ciph
from now on we'll be talking about matrices, where **P** is plaintext matrix mentioned above, **C** is cipher matrix, **K** is key matrix.
**C** is vety easy to see: repeating same steps as with **P**, we get:
``31 14 10
21 0 61
57 43 35``
here goes some mathematics:
(**P**x**K**)mod67=**C**
**K**=(**P**^(-1)x**C**)mod67
order matters. be careful. 
so, having plaintext and cipher we can now find the key. i wrote matrix invertion function in two steps: first create minor matrix, then... magic. 
``x^(-1) mod m = x^(m-2) mod m``
for our problem: every element of inverted matrix mod 67 can be counted as (minor*(determinant**65))%67. now, multiply this inverted matrix by ciphertext matrix and BUM! we have the key. to decipher, multiply every 3-lettered vector of ciphertext by inverted key matrix. repeat for all possible strings that encode 'Hill ciph'
my code is kinda sloppy and probably could've been done better, BUT well it worked for me. at the end i've found 2 strings that looked kinda readable (a lot of spaces between words, suspisios). spent a few more minutes looking at them aand....... [REDACTED]
