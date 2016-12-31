'''
Main function instantiates the Receiver class
Calls encrypt and decrypt on user-inputted message
'''
from receiver import Receiver

def main():
    message = raw_input("Enter a message you would like to encrypt/decrypt: ")
    receiver = Receiver()

    encrypted_message = receiver.encrypt(message)
    decrypted_message = receiver.decrypt(encrypted_message)
    
    print "Your original message was: " + message
    print "Your encrypted message is: " + ''.join([str(num) for num in encrypted_message])
    print "Your decrpyted message is: " + decrypted_message
    return

if __name__ == "__main__":
    main()
