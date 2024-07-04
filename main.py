import argparse
import os
import base64
from getpass import getpass
from Encryption_and_Dycryption.Create_Encryption_dycryption import EncryptionManager

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import shutil
from Logger_Writer.Logger import Log_Writer

class Calling_Complete_Function:
    def __init__(self):
        pass







    def Log_Folder_create_delete(self,Log_File_folder,Log_Text_file):

        if os.path.exists(Log_File_folder):
            shutil.rmtree(Log_File_folder)
            self.Log_Folder_create_delete()
        else:
            os.makedirs('Log_Text_file', exist_ok=True)




if __name__=="__main__":
    handle_directory = EncryptionManager().handle_directory()
    Log_File_folder = "./Log_File_text"
    Log_Text_file = "./Log_File_text"
    main_class = Calling_Complete_Function()
    main_class.Log_Folder_create_delete(Log_File_folder,Log_Text_file)

    file_obj= open(Log_Text_file,'r+')
    Log_Writer().LogWriter(file_obj, "Starting complete process")

    Log_Writer().LogWriter(file_obj,"Log folder created successfully")
    file_obj.close()

    parser = argparse.ArgumentParser(description="Encrypt or decrypt files and directories.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode of operation: encrypt or decrypt.")
    parser.add_argument("path", help="Path to the file or directory.")
    args = parser.parse_args()

    passphrase = getpass.getpass("Enter your passphrase: ")
    encryption_manager = EncryptionManager(passphrase)

    if os.path.isdir(args.path):
        handle_directory(args.path, encryption_manager, encrypt=(args.mode == "encrypt"))
    else:
        if args.mode == "encrypt":
            encryption_manager.encrypt_file(args.path)
        elif args.mode == "decrypt":
            encryption_manager.decrypt_file(args.path)











