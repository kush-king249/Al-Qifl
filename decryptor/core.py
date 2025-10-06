
import os
from cryptography.fernet import Fernet
from ..utils import file_operations

ENCRYPTED_EXTENSION = ".rnsm"

def load_key(filepath):
    """
    Loads the encryption key from a file.
    :param filepath: The full path to the key file.
    :return: The encryption key (bytes).
    """
    return file_operations.read_file(filepath)

def decrypt_file(filepath, key):
    """
    Decrypts a single file and restores its original extension.
    :param filepath: The full path to the file to be decrypted.
    :param key: The encryption key (bytes).
    """
    f = Fernet(key)
    encrypted_content = file_operations.read_file(filepath)
    decrypted_content = f.decrypt(encrypted_content)
    
    # Extract original extension from the filename
    original_filepath = file_operations.get_original_extension_from_encrypted(filepath, ENCRYPTED_EXTENSION)
    file_operations.write_file(original_filepath, decrypted_content)
    os.remove(filepath) # Remove the encrypted file after decryption

def decrypt_target_directory(directory, key_filepath):
    """
    Decrypts all encrypted files in a specific directory.
    :param directory: The path to the target directory.
    :param key_filepath: The path to the encryption key file.
    :return: The number of files that were successfully decrypted.
    """
    key = load_key(key_filepath)
    
    files_to_decrypt = file_operations.find_files(directory, [ENCRYPTED_EXTENSION])
    decrypted_files_count = 0
    for filepath in files_to_decrypt:
        try:
            decrypt_file(filepath, key)
            decrypted_files_count += 1
        except Exception as e:
            print(f"Error decrypting file {filepath}: {e}")
    return decrypted_files_count

