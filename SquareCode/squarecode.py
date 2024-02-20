'''
One classic method for composing secret messages is called a square code.  The spaces are
removed from the text and the characters are written into a square (or rectangle).  For example,
the sentence "If man was meant to stay on the ground god would have given us roots" is 54
characters long, so it is written into a rectangle with 7 rows and 8 columns.

                ifmanwas
                meanttos
                tayonthe
                groundgo
                dwouldha
                vegivenu
                sroots

The coded words are obtained by reading down the columns and going left to right.
For example, the message above is coded as following words:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

In your program, have the user enter a message or a predefined message as an input.
Have the maximum message length be 81 characters.
'''

# ADD IMPORT IF NEEDED

def squarecode(message = "If man was meant to stay on the ground god would have given us roots"):
    '''
    Encodes the given message and returns the encoded string
    :param message: plain text message
    :return: encoded string
    '''
    # YOUR CODE GOES HERE
    return

def main():
    message = input("Give a message to be encoded? ")
    message = message.strip()
    if len(message) == 0:
        print(squarecode())
    else:
        print(squarecode(message))

if __name__ == "__main__":
    main()