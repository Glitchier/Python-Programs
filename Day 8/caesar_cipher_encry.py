alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text,no_shift,ch):
    cipher_text=""
    for letter in plain_text:
        if letter in alphabet:
            pos=alphabet.index(letter)
            if(ch=='encode'):
                new_pos=pos+no_shift
                new_letter=alphabet[new_pos]
                cipher_text+=new_letter
            elif(ch=='decode'):
                new_pos=pos-no_shift
                new_letter=alphabet[new_pos]
                cipher_text+=new_letter
            else:
                print("Invalid choice!!!")
        else:
            cipher_text+=letter
    print(f"The {ch} text is : {cipher_text}")

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

again=True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%25
    caesar(text,shift,direction)
    res=input("Do you want to run again? Type Yes or No : ").lower()
    if(res=="no"):
        again=False