
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from Al_Qifl.decryptor import core

class DecryptorGUI(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Al-Qifl Decryptor - أداة فك تشفير تعليمية")
        self.geometry("500x300")

        self.directory_path = tk.StringVar()
        self.key_file_path = tk.StringVar()

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
        tk.Label(key_frame, text="مسار ملف المفتاح:").pack(side="left")
        tk.Entry(key_frame, textvariable=self.key_file_path, width=50).pack(side="left", expand=True, fill="x")
        tk.Button(key_frame, text="اختيار...", command=self.select_key_file).pack(side="left")

        # زر فك التشفير
        decrypt_button = tk.Button(self, text="بدء فك التشفير", command=self.start_decryption, bg="#4CAF50", fg="white")
        decrypt_button.pack(pady=20)

        # منطقة عرض الحالة
        self.status_label = tk.Label(self, text="", fg="blue")
        self.status_label.pack(pady=10)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_path.set(directory)

    def select_key_file(self):
        key_file = filedialog.askopenfilename(filetypes=[("Key files", "*.key")])
        if key_file:
            self.key_file_path.set(key_file)

    def start_decryption(self):
        directory = self.directory_path.get()
        key_file = self.key_file_path.get()

        if not directory or not os.path.isdir(directory):
            messagebox.showerror("خطأ", "يرجى اختيار مجلد صالح.")
            return

        if not key_file or not os.path.isfile(key_file):
            messagebox.showerror("خطأ", "يرجى اختيار ملف مفتاح صالح.")
            return

        confirm = messagebox.askyesno("تأكيد", f"""سيتم محاولة فك تشفير الملفات في المجلد \n{directory}\n باستخدام المفتاح المحدد. هل تريد المتابعة؟""")

        if confirm:
            try:
                self.status_label.config(text="جاري فك التشفير...")
                self.update_idletasks()
                decrypted_count = core.decrypt_target_directory(directory, key_file)
                messagebox.showinfo("نجاح", f"اكتمل فك التشفير بنجاح.\nتم فك تشفير {decrypted_count} ملف.")
                self.status_label.config(text="")
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء فك التشفير: {e}\nيرجى التأكد من استخدام المفتاح الصحيح.")
                self.status_label.config(text="")

if __name__ == "__main__":
    app = DecryptorGUI()
    app.mainloop()

