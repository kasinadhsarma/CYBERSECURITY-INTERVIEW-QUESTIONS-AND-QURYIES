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





2.PLAY FAIR CIPHER
ENCRYPTION:

*The playfair algorithm is based on a 5x5 matrix of letters.
*The matrix is constructed by filling in the letter of the keyword from left to right and from top to bottom, and then filling the remainder of the matrix with the remaining letters in alphabetic order.
*The letters I and J are in one place.
*Make pairs of letters add filler letter "X" if the same letter appears in a pair.
PLAIN TEXT :  INSTRUCTIONS
PLAIN TEXT : IN ST RU ME NT SZ
KEY TEXT :  MONARCHY

![image](https://user-images.githubusercontent.com/88045527/196042883-38b89cc9-8599-4ee4-a28b-d545662320a8.png)

CIPHER TEXT IS : GATLMZCLRQTX
*If the letters appear on the same row, replace them with the letters to their immediate right respectively, wrapping around to the left side of the row if necessary. 
*If the letters are on different rows and columns, replace them with the letters on other corner of the same row. 
*The order is important - the first letter of the pair should be replaced first. 

DECRYPTION:

*The key square is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext. Each of the 25 alphabets must be unique and one letter of the alphabet (usually J) is omitted from the table (as the table can hold only 25 alphabets). If the plaintext contains J, then it is replaced by I. 
 
*The initial alphabets in the key square are the unique alphabets of the key in the order in which they appear followed by the remaining letters of the alphabet in order. 

CIPHER TEXT :  GATLMZCLRQTX
CIPHER TEXT : GA TL MZ CL RQ TX
DECRYPTED TEXT FROM CIPHER TEXT IS : INSTRUMENTSZ

![image](https://user-images.githubusercontent.com/88045527/196043192-17513aba-39cb-4c94-b266-e7b6f70c6146.png)


ADVANTAGES:
*It is significantly harder to break since the frequency analysis technique used to break simple substitution ciphers is difficult but still can be used on (25*25) = 625 digraphs rather than 25 monographs which is difficult. 
*Frequency analysis thus requires more cipher text to crack the encryption. 

DISADVANTAGES:
*An interesting weakness is the fact that a digraph in the ciphertext (AB) and it’s reverse (BA) will have corresponding plaintexts like UR and RU (and also ciphertext UR and RU will correspond to plaintext AB and BA, i.e. the substitution is self-inverse). That can easily be exploited with the aid of frequency analysis, if the language of the plaintext is known. 
 
*Another disadvantage is that playfair cipher is a symmetric cipher thus same key is used for both encryption and decryption. 
