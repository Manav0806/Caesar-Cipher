print("WELCOME TO THE CEASAR CYPHER --_--")

# creating the list of alphabets
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# creating function for encoding and decoding
def ceasar(text,shift,direction):
    end_text = ""
    for i in text:
        if i in alphabets:
            position = alphabets.index(i)
            new_position = position + shift
            new_letter = alphabets[new_position]
            end_text += new_letter
        else:
            end_text += i
    print(f"The {direction}d text is:\n{end_text}")

should_continue = True
while should_continue:
    # creating variables for code
    direction = input("Type encode to encrypt or type decode to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # it is for shift if it is greater than the index in alphabet

    if direction=="decode":
        shift *= -1
    ceasar(text,shift,direction)
    
    result = input("Type Yes to continue and No for Exit:\n")
    if result=="no":
        should_continue = False