
# Al-Qifl: A Safe Ransomware Simulation for Educational Purposes

![Al-Qifl Logo](https://via.placeholder.com/400x200?text=Al-Qifl+Logo) <!-- Placeholder for a future logo -->

## Important Disclaimer

**THIS PROJECT IS FOR EDUCATIONAL PURPOSES ONLY. DO NOT RUN IT ON ANY REAL OR IMPORTANT DATA. The author and contributors are not responsible for any damage that may result from the misuse of this tool.**

Al-Qifl aims to provide a safe and controlled environment to understand the internal mechanism of ransomware and how it operates, as well as to explore decryption methods. It is designed for cybersecurity students, researchers, and anyone interested in practically understanding this type of cyber threat.

## Educational Objectives

Through this project, you will be able to:

*   **Deep understanding of Ransomware threats:** Gain an attacker's perspective and how files are targeted and encrypted.
*   **Practical application of encryption:** Use strong encryption algorithms (AES via Python's `cryptography` library) in a realistic context.
*   **Incident Response skills:** Understand the decryption process and how to restore files using the correct key.
*   **Security tool development:** Build tools with Command Line Interfaces (CLI) and Graphical User Interfaces (GUI) to handle security tasks.

## How Al-Qifl Works?

Al-Qifl consists of two main parts: the **Encryptor** and the **Decryptor**.

### 1. The Encryptor (Al-Qifl Encryptor)

This part simulates the encryption process performed by ransomware. The encryptor works as follows:

1.  **Target Identification:** You are asked to specify a safe test folder. It searches for files with common extensions (e.g., `.txt`, `.jpg`, `.pdf`, `.docx`) within this folder.
2.  **Key Generation:** It generates a random and secure encryption key using the AES algorithm. This key is saved in a separate file (usually `key.key`) outside the test folder. This represents the "key" held by the attacker.
3.  **Encryption:** It encrypts the content of each target file using the generated key. After encryption, the file extension is changed (for example, from `my_doc.txt` to `my_doc.txt.rnsm`) and the original file is deleted.
4.  **Ransom Note:** It creates a text file (usually `README_FOR_DECRYPTION.txt`) in the test folder containing a fake message stating that the files are encrypted and demanding a "fake ransom" (in this case, referring to using the decryption tool).

### 2. The Decryptor (Al-Qifl Decryptor)

This part simulates the decryption process using the correct key to restore files.

1.  **Key Loading:** You are asked to provide the path to the key file (`key.key`) that was saved during the encryption process.
2.  **Encrypted File Identification:** It searches for files with the new extension (e.g., `.rnsm`) within the test folder.
3.  **Decryption:** It decrypts the content of each encrypted file using the provided key. After decryption, the original file extension is restored, and the encrypted file is deleted.

## Project Structure

```
Al-Qifl/
├── README_ar.md          # README file in Arabic
├── README_en.md          # README file in English
├── report.md             # Comprehensive project report in Arabic
├── encryptor/
│   ├── __init__.py
│   ├── cli.py            # Command Line Interface for Encryptor
│   ├── gui.py            # Graphical User Interface for Encryptor
│   └── core.py           # Core encryption logic
├── decryptor/
│   ├── __init__.py
│   ├── cli.py            # Command Line Interface for Decryptor
│   ├── gui.py            # Graphical User Interface for Decryptor
│   └── core.py           # Core decryption logic
├── utils/
│   ├── __init__.py
│   └── file_operations.py # Helper functions for file operations
├── requirements.txt      # List of required libraries
└── main.py               # Main entry point for running both interfaces
```

## Requirements

*   Python 3.x
*   Libraries listed in `requirements.txt`

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kush-king249/Al-Qifl.git
    cd Al-Qifl
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    # venv\Scripts\activate   # For Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run Al-Qifl using either the Command Line Interface (CLI) or the Graphical User Interface (GUI).

### 1. Command Line Interface (CLI)

#### Encryptor CLI

To encrypt files in a specific directory:

```bash
python main.py encrypt-cli <target_directory_path> [--key-file <key_file_path>] [--ext <extension1> <extension2> ...]
```

**Example:**

```bash
python main.py encrypt-cli /home/user/test_files --key-file my_secret_key.key --ext .txt .jpg .pdf
```

*   `<target_directory_path>`: The directory containing the files to be encrypted.
*   `--key-file`: (Optional) Path to save the encryption key. Default is `key.key` in the current working directory.
*   `--ext`: (Optional) List of target extensions. Default is `.txt`, `.jpg`, `.jpeg`, `.png`, `.pdf`, `.docx`, `.xlsx`.

#### Decryptor CLI

To decrypt files in a specific directory:

```bash
python main.py decrypt-cli <target_directory_path> --key-file <key_file_path>
```

**Example:**

```bash
python main.py decrypt-cli /home/user/test_files --key-file my_secret_key.key
```

*   `<target_directory_path>`: The directory containing the encrypted files.
*   `--key-file`: **Required** The path to the key file used for encryption.

### 2. Graphical User Interface (GUI)

#### Encryptor GUI

To run the Encryptor GUI:

```bash
python main.py encrypt-gui
```

A window will appear allowing you to select the target directory and start the encryption process.

#### Decryptor GUI

To run the Decryptor GUI:

```bash
python main.py decrypt-gui
```

A window will appear allowing you to select the target directory and the key file, then start the decryption process.

## Screenshots

<!-- Screenshots will be added here after testing -->

## Author

*   **Hassan Mohamed Hassan Ahmed**

## Contribution

Contributions are welcome to improve this educational project. Please read the contribution guidelines (if available) before submitting pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details. <!-- If a license file exists -->

