# Ransomware Simulation

## Overview

This project simulates a ransomware attack for educational and testing purposes. Ransomware is a type of malware that encrypts files on a victim's computer and demands payment (usually in cryptocurrency) for the decryption key. This simulation provides insights into how ransomware operates and its potential impact.

## How It Works

The ransomware simulation consists of several components:

1. **Encryption**: The ransomware encrypts files in a specified directory using a symmetric encryption algorithm (Fernet). It targets files with specific extensions (e.g., .txt) to encrypt.

2. **Ransom Note**: After encrypting the files, the ransomware generates a ransom note with instructions for the victim to follow. The note typically includes information on how to pay the ransom and receive the decryption key.

3. **Desktop Background Change**: The ransomware changes the victim's desktop background to display the ransom note, ensuring that the message is prominently visible to the victim.

4. **Decryption**: The victim is instructed to email the attacker and pay a ransom to receive the decryption key. Once the ransom is paid, the attacker provides the decryption key, allowing the victim to decrypt their files.

## Features

- Encrypt files in a target directory
- Generate ransom notes with payment instructions
- Change the desktop background to display the ransom note
- Simulate decryption process using a provided decryption key

## Usage

To simulate the ransomware attack:

1. Modify the `ransomware.py` file to specify the target directory and other parameters.
2. Run the ransomware script to encrypt files and generate the ransom note.
3. Follow the instructions in the ransom note to simulate the decryption process.

## Additional Tools

### RSA Key Generation

The project also includes a script (`rsa_key_generator.py`) to generate RSA encryption and decryption keys. These keys are used for encrypting and decrypting the session key during the ransomware attack.

### Session Key Decryption

Another script (`decrypt_session_key.py`) is provided to decrypt the session key file (`EMAIL_ME.txt`) using the private RSA key (`private.pem`). This script simulates the step where the attacker decrypts the session key provided by the victim.

## Disclaimer

This project is intended for educational and testing purposes only. Do not use it for illegal activities. The developers assume no liability for any misuse or damage caused by this simulation.

## Contributions

Contributions to this project are welcome. If you have any suggestions or improvements, feel free to submit a pull request.
