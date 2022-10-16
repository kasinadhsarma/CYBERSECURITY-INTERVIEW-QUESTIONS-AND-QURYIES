def generateKeyMatrix (key): 
    # Create 5X5 matrix with all values as 0
    # [
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0]
    # ]
    matrix_5x5 = [[0 for i in range (5)] for j in range(5)]
    simpleKeyArr = []
    """
     Generate SimpleKeyArray with key from user Input 
     with following below condition:
     1. Character Should not be repeated again
     2. Replacing J as I (as per rule of playfair cypher)
    """
    for c in key:
        if c not in simpleKeyArr:
            if c == 'J':
                simpleKeyArr.append('I')
            else:
                simpleKeyArr.append(c)
    """
    Fill the remaining SimpleKeyArray with rest of unused letters from english alphabets 
    """
    is_I_exist = "I" in simpleKeyArr
    # A-Z's ASCII Value lies between 65 to 90 but as range's second parameter excludes that value we will use 65 to 91
    for i in range(65,91):
        if chr(i) not in simpleKeyArr:
            # I = 73
            # J = 74
            # We want I in simpleKeyArr not J
            if i==73 and not is_I_exist:
                simpleKeyArr.append("I")
                is_I_exist = True
            elif i==73 or i==74 and is_I_exist:
                pass
            else:
                simpleKeyArr.append(chr(i))
    """
    Now map simpleKeyArr to matrix_5x5 
    """
    index = 0
    for i in range(0,5):
        for j in range(0,5):
            matrix_5x5[i][j] = simpleKeyArr[index]
            index+=1
    return matrix_5x5
def indexLocator (char,cipherKeyMatrix):
    indexOfChar = []

    # convert the character value from J to I
    if char=="J":
        char = "I"
    for i,j in enumerate(cipherKeyMatrix):
        # [
        #   (0, ['K', 'A', 'R', 'E', 'N']),
        #   (1, ['D', 'B', 'C', 'F', 'G']), 
        #   (2, ['H', 'I', 'L', 'M', 'O']), 
        #   (3, ['P', 'Q', 'S', 'T', 'U']), 
        #   (4, ['V', 'W', 'X', 'Y', 'Z'])
        # ]
        # j refers to inside matrix =>  ['K', 'A', 'R', 'E', 'N'],
        for k,l in enumerate(j):
            # [(0,'K'),(1,'A'),(2,'R'),(3,'E'),(4,'N')]
            if char == l:
                indexOfChar.append(i)
                indexOfChar.append(k)
                return indexOfChar
def encryption (plainText,key):
    cipherText = []
    # 1. Generate Key Matrix
    keyMatrix = generateKeyMatrix(key)
    # 2. Encrypt According to Rules of playfair cipher
    i = 0
    while i < len(plainText):
        # 2.1 calculate two grouped characters indexes from keyMatrix
        n1 = indexLocator(plainText[i],keyMatrix)
        n2 = indexLocator(plainText[i+1],keyMatrix)
        # 2.2  if same column then look in below row so
        # format is [row,col]
        # now to see below row => increase the row in both item
        # (n1[0]+1,n1[1]) => (3+1,1) => (4,1)
        # (n2[0]+1,n2[1]) => (4+1,1) => (5,1)
        # but in our matrix we have 0 to 4 indexes only
        # so to make value bound under 0 to 4 we will do %5
        # i.e.,
        #   (n1[0]+1 % 5,n1[1])
        #   (n2[0]+1 % 5,n2[1])
        if n1[1] == n2[1]:
            i1 = (n1[0] + 1) % 5
            j1 = n1[1]

            i2 = (n2[0] + 1) % 5
            j2 = n2[1]
            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
            cipherText.append(", ")
        # same row
        elif n1[0]==n2[0]:
            i1= n1[0]
            j1= (n1[1] + 1) % 5

            i2= n2[0]
            j2= (n2[1] + 1) % 5
            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
            cipherText.append(", ")
        # if making rectangle then
        # [4,3] [1,2] => [4,2] [3,1]
        # exchange columns of both value
        else:
            i1 = n1[0]
            j1 = n1[1]
            i2 = n2[0]
            j2 = n2[1]
            cipherText.append(keyMatrix[i1][j2])
            cipherText.append(keyMatrix[i2][j1])
            cipherText.append(", ")
        i += 2  
    return cipherText
def convertPlainTextToDiagraphs (plainText):
    # add X if Two letters are being repeated
    for s in range(0,len(plainText)+1,2):
        if s<len(plainText)-1:
            if plainText[s]==plainText[s+1]:
                plainText=plainText[:s+1]+'X'+plainText[s+1:]
    # append X if the total letters are odd, to make plaintext even
    if len(plainText)%2 != 0:
        plainText = plainText[:]+'X'
    return plainText
def main():
    #Getting user inputs Key (to make the 5x5 char matrix) and Plain Text (Message that is to be encripted)
    key = input("Enter key: ").replace(" ","").upper()
    plainText =input("Plain Text: ").replace(" ","").upper()
    convertedPlainText = convertPlainTextToDiagraphs(plainText)
    print(convertedPlainText)
    keyMatrix = generateKeyMatrix(key)
    cipherText = " ".join(encryption(convertedPlainText,key))
    print(cipherText)
    # print(len(keyMatrix)) => 5
    print(keyMatrix)
    print('keytext')
    print('plainText')
    print('cipherText')
if __name__ == "__main__":
    main()
