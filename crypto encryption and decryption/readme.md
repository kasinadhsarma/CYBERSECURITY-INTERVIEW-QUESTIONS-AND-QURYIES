write here the topics or create new folder

1.CAESAR CIPHER:

*Caesar cipher technique is one of the earliest and simplest methods of encryption technique.
*It's simply a type of substitution cipher, i.e each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet.
*Thus to cipher a given text we need an integer value, known as a shift which indicates the number of positions each letter of the text has been moved down. 
*We can represent the numbers according to the scheme, A=0,B=1,C=2,D=3,E=4.............Z=25 and so on.

*FOR ENCRYPTION:
We can describe mathematically as ----> E=(P+K)mod26 
Here K --> represents the shift value and P --> represents the plain text.

*FOR DECRYPTION:
We can describe mathematically as -----> D=(C-K)mod26
Here k --> represents the shift value and C --> represents the cipher text.

*TIME COMPLEXITY OF CAESAR CIPHER IS : O(N)
*AUXILIARY SPACE OF CAESAR CIPHER IS : 0(N)

EXAMPLE:
PLAIN TEXT : THE QUICK BROWN FOX
by using encryption method
CIPHER TEXT : WKH TXLFN EURZQ IRA

BRUTE FORCE ATTACK ON CAESAR CIPHER:
*The encryption and decryption algorithm are know.
*There are only 25 keys to try.
*The language of the plantext is know and easily recognizable.

ADVANTAGES OF CAESAR CIPHER:
1.It is very easy to implement.
2.This method is the simplest method of cryptography.
3.Only one short key is used in its entire process.
4.If a system does not use complex coding techniques, it is the best method for it.
5.It requires only a few computing resources.

DISADVANTAGES OF CAESAR CIPHER:
1.It can be easily hacked. It means the message encrypted by this method can be easily decrypted.
2.It provides very little security.
3.By looking at the pattern of letters in it, the entire message can be decrypted.

