
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrpyt(text, shift):
    if direction == 'encode':
        encode_text = ""
        for i, j in enumerate(text):
            lshift = alphabet.index(j) + shift
            if lshift >= len(alphabet):
                lshift = len(alphabet) - lshift
            encode_text = encode_text+alphabet[lshift]
    elif direction == 'decode':
        encode_text = ""
        for i, j in enumerate(text):
            lshift = alphabet.index(j) - shift + 1
            if lshift >= len(alphabet):
                lshift = len(alphabet) - lshift


            encode_text = encode_text+alphabet[lshift]

    print(encode_text)

while direction in ('decode','encode'):

    encrpyt(text, shift)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##Bug alert: What happens if you try to encode the word 'civilization'?

##TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


# def prime_number(number):
#     is_prime = True
#     for i in range(2,number):
#         if number % i == 0:
#            is_prime = False
#     if is_prime:
#         print("is a prime number")
#     else:
#         print("is not a prime number")


# myNum = input("check for prime number: ")

# prime_number(int(myNum))