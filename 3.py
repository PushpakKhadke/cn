def xor_encrypt(input_string,key):
    encrypted = ""
    for char in input_string:
        encrypted += chr(ord(char) ^ key)
    return encrypted

def xor_decrypt(input_string,key):
    decrypted = ""
    for char in input_string:
        decrypted += chr(ord(char) ^ key)
    return decrypted

input_string = input("Enter String = ")
key = 42
encrypted_string = xor_encrypt(input_string, key)
print("Encrypted String = ", encrypted_string)

decrypted_string = xor_decrypt(encrypted_string,key)
print("Decrypted String = ",decrypted_string)