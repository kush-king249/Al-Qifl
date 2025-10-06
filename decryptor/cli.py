import argparse
import os
from Al_Qifl.decryptor import core

def main():
    parser = argparse.ArgumentParser(description="Al-Qifl Decryptor - أداة فك تشفير تعليمية")
    parser.add_argument("directory", help="المجلد المستهدف لفك التشفير")
    parser.add_argument("--key-file", required=True, help="مسار ملف المفتاح المستخدم لفك التشفير")

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"خطأ: المجلد '{args.directory}' غير موجود.")
        return

    if not os.path.isfile(args.key_file):
        print(f"خطأ: ملف المفتاح '{args.key_file}' غير موجود.")
        return

    print(f"سيتم محاولة فك تشفير الملفات في المجلد '{args.directory}' باستخدام المفتاح من '{args.key_file}'.")
    confirm = input("هل أنت متأكد أنك تريد المتابعة؟ (نعم/لا): ")

    if confirm.lower() == 'نعم':
        try:
            decrypted_count = core.decrypt_target_directory(args.directory, args.key_file)
            print(f"\nاكتمل فك التشفير بنجاح.")
            print(f"تم فك تشفير {decrypted_count} ملف.")
        except Exception as e:
            print(f"حدث خطأ أثناء عملية فك التشفير: {e}")
            print("يرجى التأكد من استخدام المفتاح الصحيح وأن الملفات لم يتم تعديلها.")
    else:
        print("تم إلغاء العملية.")

if __name__ == "__main__":
    main()
