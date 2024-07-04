import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend

class EncryptionManager:
    def encrypt_file(self, file_path):
        with open(file_path, "rb") as f:
            file_data = f.read()
        fek = self.generate_random_key()
        encrypted_data = self.aes_encrypt(fek, file_data)
        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted_data)
        self.store_encrypted_fek(fek)
        print(f"File '{file_path}' encrypted and key stored.")

    def decrypt_file(self, file_path):
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
        fek = self.retrieve_encrypted_fek()
        file_data = self.aes_decrypt(fek, encrypted_data)
        with open(file_path.replace(".enc", ".dec"), "wb") as f:
            f.write(file_data)
        print(f"File '{file_path}' decrypted.")

    def handle_directory(directory, encryption_manager, encrypt=True):
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if encrypt:
                    encryption_manager.encrypt_file(file_path)
                else:
                    encryption_manager.decrypt_file(file_path)

