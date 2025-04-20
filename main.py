# BASE 64 encrypter and decrypter
# WITHOUT USING base64 LIBRARY

# BASE 64 CHR TABLE
ALPHABETS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


# MAIN LOGICS
def encode_to_base64(input_text) :
    
    """
    encodes a string into base64 format without using the base64 library
    """
    binary_data=""

    # converts each chr to its 8-bit binary representation
    for character in input_text :
        binary_data+=f"{ord(character):08b}"  # getting ascii (8 bits format)


    # caculate padding to make the binary string length multiple of 6
    padding_bits=(6-len(binary_data)%6)%6
    binary_data+='0'*padding_bits  # adding necessary zero bits for allignment

    # convert each 6-bit binary chunck  to a corresponding  BASE64 chr
    encoded_result=""

    for a in range(0,len(binary_data),6) :
        six_bit_chunk=binary_data[a:a+6]
        index=int(six_bit_chunk,2)
        encoded_result+=ALPHABETS[index]

    # adding '=' padding chrs to make output length a multiple of four
    padding_chars=(4 - len(encoded_result) % 4) % 4
    encoded_result+="=" * padding_chars

    return encoded_result


def decode_from_base64(encoded_text) :

    """
    decodes a BASE64-encoded string back to its original form without using library
    """

    # counting '=' padding  chrs and remove them 
    padding_count=encoded_text.count('=')
    encoded_text=encoded_text.rstrip('=')

    binary_data=""

    # converst each BASE64 chrs to 6-bit binary string

    for char in encoded_text :
        if char not in ALPHABETS : 
            return " Error : Invalid Base64 input. "
        index=ALPHABETS.index(char)
        binary_data+=f"{index:06b}"

    # removing padding bits (2 bits per '=' padding chr)

    if padding_count :
        binary_data=binary_data[:-(padding_count*2)]

    # convert binary string into original chrs (8-bit per chrs)

    decoded_text=""
    for a in range(0,len(binary_data),8):
        byte_chunk=binary_data[a:a+8]
        if len(byte_chunk)==8:
            decoded_text+=chr(int(byte_chunk, 2))

    return decoded_text



# MAIN INTERFACE
def base64_tool() :
    
   
    print("/----------- Base64 Encoder / Decoder -----------/ ")
    print("1. Encode Text")
    print("2. Decode Text")

    user_choice=input("Select an option (1 or 2) : ").strip()

    if user_choice not in ['1','2'] :
        print(" Invalid selection. Please choose either 1 or 2. ")
        return

    user_input=input("Enter your text : ")

    if user_choice=='1':
        result=encode_to_base64(user_input)
        print(f"\nEncoded Output : {result}")
    else:
        result=decode_from_base64(user_input)
        print(f"\nDecoded Output : {result}")


base64_tool()

# END
