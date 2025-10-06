
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from Al_Qifl.encryptor import core

class EncryptorGUI(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Al-Qifl Encryptor - أداة تشفير تعليمية")
        self.geometry("500x300")

        self.directory_path = tk.StringVar()
        self.key_file_path = tk.StringVar()
        self.key_file_path.set(os.path.join(os.getcwd(), "key.key"))

        self.create_widgets()

    def create_widgets(self):
        # إطار اختيار المجلد
        dir_frame = tk.Frame(self)
        dir_frame.pack(pady=10, padx=10, fill="x")
        tk.Label(dir_frame, text="المجلد المستهدف:").pack(side="left")
        tk.Entry(dir_frame, textvariable=self.directory_path, width=50).pack(side="left", expand=True, fill="x")
        tk.Button(dir_frame, text="اختيار...", command=self.select_directory).pack(side="left")

        # إطار ملف المفتاح
        key_frame = tk.Frame(self)
        key_frame.pack(pady=5, padx=10, fill="x")
        tk.Label(key_frame, text="مسار حفظ المفتاح:").pack(side="left")
        tk.Entry(key_frame, textvariable=self.key_file_path, width=50).pack(side="left", expand=True, fill="x")

        # زر التشفير
        encrypt_button = tk.Button(self, text="بدء التشفير", command=self.start_encryption, bg="#ff4d4d", fg="white")
        encrypt_button.pack(pady=20)

        # منطقة عرض الحالة
        self.status_label = tk.Label(self, text="", fg="blue")
        self.status_label.pack(pady=10)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_path.set(directory)

    def start_encryption(self):
        directory = self.directory_path.get()
        key_file = self.key_file_path.get()

        if not directory or not os.path.isdir(directory):
            messagebox.showerror("خطأ", "يرجى اختيار مجلد صالح.")
            return

        confirm = messagebox.askyesno("تأكيد", f"تحذير: سيتم تشفير الملفات في المجلد \n{directory}\n. هل تريد المتابعة؟")

        if confirm:
            try:
                self.status_label.config(text="جاري التشفير...")
                self.update_idletasks()
                encrypted_count = core.encrypt_target_directory(directory, key_file, [".txt", ".jpg", ".pdf"])
                messagebox.showinfo("نجاح", f"اكتمل التشفير بنجاح.\nتم تشفير {encrypted_count} ملف.\nتم حفظ المفتاح في: {key_file}")
                self.status_label.config(text="")
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء التشفير: {e}")
                self.status_label.config(text="")

if __name__ == "__main__":
    app = EncryptorGUI()
    app.mainloop()

