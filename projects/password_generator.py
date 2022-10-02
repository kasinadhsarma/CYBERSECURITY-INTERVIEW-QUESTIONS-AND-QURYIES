from argparse import ArgumentParser
import secrets
import random
import string

# Setting up the Argument Parser
parser = ArgumentParser(
    prog='Password Generator.',
    description='Generate any number of passwords with this tool.'
)

# Adding the arguments to the parser
parser.add_argument("-n", "--numbers", default=0,
                    help="Number of digits in the PW", type=int)
parser.add_argument("-l", "--lowercase", default=0,
                    help="Number of lowercase chars in the PW", type=int)
parser.add_argument("-u", "--uppercase", default=0,
                    help="Number of uppercase chars in the PW", type=int)
parser.add_argument("-s", "--special-chars", default=0,
                    help="Number of special chars in the PW", type=int)

# add total pw length argument
parser.add_argument("-t", "--total-length", type=int,
                    help="The total password length. If passed, it will ignore -n, -l, -u and -s, "
                    "and generate completely random passwords with the specified length")

# The amount is a number so we check it to be of type int.
parser.add_argument("-a", "--amount", default=1, type=int)
parser.add_argument("-o", "--output-file")

# Parsing the command line arguments.
args = parser.parse_args()

# list of passwords
passwords = []
# Looping through the amount of passwords.
for _ in range(args.amount):
    if args.total_length:
        # generate random password with the length
        # of total_length based on all available characters
        passwords.append("".join(
            [secrets.choice(string.digits + string.ascii_letters + string.punctuation)
             for _ in range(args.total_length)]))
    else:
        password = []
        # If / how many numbers the password should contain
        for _ in range(args.numbers):
            password.append(secrets.choice(string.digits))

        # If / how many uppercase characters the password should contain
        for _ in range(args.uppercase):
            password.append(secrets.choice(string.ascii_uppercase))

        # If / how many lowercase characters the password should contain
        for _ in range(args.lowercase):
            password.append(secrets.choice(string.ascii_lowercase))

        # If / how many special characters the password should contain
        for _ in range(args.special_chars):
            password.append(secrets.choice(string.punctuation))
        # Shuffle the list with all the possible letters, numbers and symbols.
        random.shuffle(password)
        # Get the letters of the string up to the length argument and then join them.
        password = ''.join(password)
        # append this password to the overall list of password.
        passwords.append(password)
# Store the password to a .txt file.
if args.output_file:
    with open(args.output_file, 'w') as f:
        f.write('\n'.join(passwords))
print('\n'.join(passwords))

'''  python password_generator.py --help
usage: Password Generator. [-h] [-n NUMBERS] [-l LOWERCASE] [-u UPPERCASE] [-s SPECIAL_CHARS] [-t TOTAL_LENGTH]
                           [-a AMOUNT] [-o OUTPUT_FILE]

Generate any number of passwords with this tool.

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBERS, --numbers NUMBERS
                        Number of digits in the PW
  -l LOWERCASE, --lowercase LOWERCASE
                        Number of lowercase chars in the PW
  -u UPPERCASE, --uppercase UPPERCASE
                        Number of uppercase chars in the PW
  -s SPECIAL_CHARS, --special-chars SPECIAL_CHARS
                        Number of special chars in the PW
  -t TOTAL_LENGTH, --total-length TOTAL_LENGTH
                        The total password length. If passed, it will ignore -n, -l, -u and -s, and generate completely   
                        random passwords with the specified length
  -a AMOUNT, --amount AMOUNT
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
 '''

# example 1
''' python password_generator.py --total-length 12
    uQPxL'bkBV># '''

#example 2
''' python password_generator.py --total-length 12 --amount 10
    &8I-%5r>2&W&
    k&DW<kC/obbr
    =/'e-I?M&,Q!
    YZF:Lt{*?m#.
    VTJO%dKrb9w6
    E7}D|IU}^{E~
    b:|F%#iTxLsp
    &Yswgw&|W*xp
    $M`ui`&v92cA
    G3e9fXb3u'lc '''

#you can also specify the number of upper case and lower case charecters and numbers by using -u -l & -n respectively.