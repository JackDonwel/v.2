FrostLocker Simulation

Version: 1.0
Author: Jack Donwel
License: Educational / Simulation Use Only

Overview

frostlocker_sim.py is a ransomware simulation designed for safe, educational purposes. It demonstrates common ransomware behaviors, such as file “encryption”, persistence, and ransom note generation, without causing real harm to files or systems.

This project is intended for cybersecurity training, awareness, and lab exercises only.

Features

Simulates file encryption by renaming files with a .frostlocked extension.

Creates a dummy ransom note in the target directory.

Demonstrates persistence techniques by adding itself to the Windows startup registry.

Simulates exfiltration of basic system information to a mock C2 server.

Can be run safely in a controlled lab environment.

Configuration
Target Directory

By default, the simulation targets:

    TARGET_DIR = "C:\\simulation_target\\"

  ⚠️ Important: Only use a safe folder in a lab environment. Do not point this to real system or personal files.

Target File Types

The simulation only “encrypts” files with the following extensions:

      TARGET_EXTENSIONS = ['.txt', '.docx', '.xlsx', '.jpg', '.png', '.sim']

Requirements

    Python 3.8+

    Windows operating system (simulation uses Windows-specific APIs)

    Python libraries:

pip install pycryptodome requests

Usage

    Open a command prompt or PowerShell as administrator.

    Navigate to the directory containing frostlocker_sim.py.

    Run the simulation:

python frostlocker_sim.py

    The script will create the target folder if it does not exist.

    It will generate sample files for “encryption”.

    A simulated ransom note will appear after files are processed.

Safety Notice

    This script is completely safe when used in a controlled lab environment.

    No real files outside the configured target directory will be affected.

    Do not use this on production systems, personal documents, or network shares.

    This project is for educational and research purposes only.

Converting to an Executable

You can convert the script into a standalone Windows executable using PyInstaller:

    pip install pyinstaller
    pyinstaller --onefile frostlocker_sim.py

The executable will be located in the dist folder. Always test in a safe lab environment.
License

This project is for educational use only. Redistribution or use for malicious purposes is strictly prohibited.

License

This project is for educational use only. Redistribution or use for malicious purposes is strictly prohibited.
