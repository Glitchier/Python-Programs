alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text,no_shift):
    cipher_text=""
    for letter in plain_text:
        pos=alphabet.index(letter)
        new_pos=pos+no_shift
        new_letter=alphabet[new_pos]
        cipher_text+=new_letter
    print(f"The Encoded text is : {cipher_text}")

print('''             
╔═══╗                         ╔═══╗      ╔╗         
║╔═╗║                         ║╔═╗║      ║║         
║║ ╚╝╔══╗ ╔══╗╔══╗╔══╗ ╔═╗    ║║ ╚╝╔╗╔══╗║╚═╗╔══╗╔═╗
║║ ╔╗╚ ╗║ ║╔╗║║══╣╚ ╗║ ║╔╝    ║║ ╔╗╠╣║╔╗║║╔╗║║╔╗║║╔╝
║╚═╝║║╚╝╚╗║║═╣╠══║║╚╝╚╗║║     ║╚═╝║║║║╚╝║║║║║║║═╣║║ 
╚═══╝╚═══╝╚══╝╚══╝╚═══╝╚╝     ╚═══╝╚╝║╔═╝╚╝╚╝╚══╝╚╝ 
                                     ║║             
                                     ╚╝             
''')
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if(direction=='encode'):
    encrypt(text,shift)
else:
    print("Invalid command.")