
import argparse
import sys
import os

# Add the current directory to sys.path to allow importing the 'Al_Qifl' package
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Now, import modules from the Al_Qifl package
from Al_Qifl.encryptor import cli as encryptor_cli
from Al_Qifl.decryptor import cli as decryptor_cli
from Al_Qifl.encryptor import gui as encryptor_gui
from Al_Qifl.decryptor import gui as decryptor_gui

def run_encryptor_cli(args_list):
    sys.argv = [sys.argv[0]] + args_list
    encryptor_cli.main()

def run_decryptor_cli(args_list):
    sys.argv = [sys.argv[0]] + args_list
    decryptor_cli.main()

def run_encryptor_gui():
    # The GUI part needs a display, which is not available in this environment.
    # We will print a message instead.
    print("To run the GUI, please execute this command in a graphical environment: python main.py encrypt-gui")
    # app = encryptor_gui.EncryptorGUI()
    # app.mainloop()

def run_decryptor_gui():
    # The GUI part needs a display, which is not available in this environment.
    # We will print a message instead.
    print("To run the GUI, please execute this command in a graphical environment: python main.py decrypt-gui")
    # app = decryptor_gui.DecryptorGUI()
    # app.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Al-Qifl - A Ransomware Simulation Tool for Education")
    parser.add_argument("mode", choices=["encrypt-cli", "decrypt-cli", "encrypt-gui", "decrypt-gui"], 
                        help="Execution mode: encrypt-cli, decrypt-cli, encrypt-gui, decrypt-gui")

    args, remaining_args = parser.parse_known_args()

    if args.mode == "encrypt-cli":
        run_encryptor_cli(remaining_args)
    elif args.mode == "decrypt-cli":
        run_decryptor_cli(remaining_args)
    elif args.mode == "encrypt-gui":
        run_encryptor_gui()
    elif args.mode == "decrypt-gui":
        run_decryptor_gui()

