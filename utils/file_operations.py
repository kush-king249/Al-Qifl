
import os

def find_files(directory, extensions):
    """
    يبحث عن الملفات ذات الامتدادات المحددة داخل مجلد معين.
    :param directory: المسار إلى المجلد المراد البحث فيه.
    :param extensions: قائمة بالامتدادات المستهدفة (مثال: [".txt", ".jpg"]).
    :return: قائمة بالمسارات الكاملة للملفات المطابقة.
    """
    target_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext.lower()) for ext in extensions):
                target_files.append(os.path.join(root, file))
    return target_files

def read_file(filepath):
    """
    يقرأ محتوى ملف ثنائي.
    :param filepath: المسار الكامل للملف.
    :return: محتوى الملف كـ bytes.
    """
    with open(filepath, 'rb') as f:
        return f.read()

def write_file(filepath, content):
    """
    يكتب محتوى ثنائي إلى ملف.
    :param filepath: المسار الكامل للملف.
    :param content: المحتوى المراد كتابته كـ bytes.
    """
    with open(filepath, 'wb') as f:
        f.write(content)

def change_extension(filepath, new_extension):
    """
    يغير امتداد ملف.
    :param filepath: المسار الكامل للملف.
    :param new_extension: الامتداد الجديد (مثال: ".rnsm").
    :return: المسار الجديد للملف بعد تغيير الامتداد.
    """
    base, _ = os.path.splitext(filepath)
    return base + new_extension

def get_original_extension_from_encrypted(filepath, encrypted_extension):
    """
    يستعيد الامتداد الأصلي لملف مشفر من اسمه.
    :param filepath: المسار الكامل للملف المشفر.
    :param encrypted_extension: الامتداد الذي تم إضافته أثناء التشفير (مثال: ".rnsm").
    :return: المسار الجديد للملف بالامتداد الأصلي.
    """
    if filepath.endswith(encrypted_extension):
        # Remove the encrypted extension
        temp_path = filepath[:-len(encrypted_extension)]
        # The original extension is now at the end of temp_path
        # e.g., 'document.txt' becomes 'document.txt.rnsm', so temp_path is 'document.txt'
        return temp_path
    return filepath
    return filepath

