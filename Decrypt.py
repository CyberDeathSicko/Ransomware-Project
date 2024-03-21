from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

class Decryptor:
    def __init__(self, encrypted_session_key_file, private_key_file, output_file):
        self.encrypted_session_key_file = encrypted_session_key_file
        self.private_key_file = private_key_file
        self.output_file = output_file

    def decrypt_session_key(self):
        try:
            # Check if the encrypted session key file exists
            if not os.path.exists(self.encrypted_session_key_file):
                raise FileNotFoundError(f"The file '{self.encrypted_session_key_file}' does not exist.")

            # Read the encrypted session key from the file
            with open(self.encrypted_session_key_file, 'rb') as f:
                encrypted_session_key = f.read()

            # Check if the private key file exists
            if not os.path.exists(self.private_key_file):
                raise FileNotFoundError(f"The file '{self.private_key_file}' does not exist.")

            # Read the private RSA key
            private_key = RSA.import_key(open(self.private_key_file).read())

            # Create a decrypter object using the private key
            decrypter = PKCS1_OAEP.new(private_key)

            # Decrypt the session key
            decrypted_session_key = decrypter.decrypt(encrypted_session_key)

            # Write the decrypted session key to the output file
            with open(self.output_file, 'wb') as f:
                f.write(decrypted_session_key)

            print("Session key decrypted successfully.")
            return decrypted_session_key
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Error during session key decryption: {e}")
            return None

def main():
    try:
        # Paths to input and output files
        encrypted_session_key_file = 'EMAIL_ME.txt'
        private_key_file = 'private.pem'
        output_file = 'PUT_ME_ON_DESKTOP.txt'

        # Create a Decryptor object and decrypt the session key
        decryptor = Decryptor(encrypted_session_key_file, private_key_file, output_file)
        decrypted_session_key = decryptor.decrypt_session_key()
        if decrypted_session_key is not None:
            print(f"Decrypted session key: {decrypted_session_key}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
