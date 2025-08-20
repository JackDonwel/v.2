FrostLocker Ransomware Simulator

Author: (donwell) Red Team
Version: 1.0
Classification: FOR AUTHORIZED LAB USE ONLY
Overview

FrostLocker is a simulated ransomware payload designed for red team engagements and cybersecurity awareness training. It mimics the behaviors of real-world ransomware—including file encryption, persistence, and extortion—in a safe, reversible, and controlled manner within an isolated lab environment.

This tool is intended to demonstrate the impact of a successful phishing attack and to train blue teams on detection, response, and recovery procedures.
⚠️ Critical Disclaimer

THIS SOFTWARE IS DESIGNED STRICTLY FOR AUTHORIZED EDUCATIONAL AND PENETRATION TESTING PURPOSES.

    Do not run this on any system without explicit, written authorization.

    Do not run this on any system that is not a fully isolated virtual machine (VM).

    Do not use this tool for any malicious, illegal, or unethical activities.

    The authors assume no liability for any damage caused by misuse of this software.

By proceeding, you acknowledge that you are solely responsible for its use and any consequences.
Features Simulated

    Social Engineering: Masquerades as a legitimate PDF invoice.

    Privilege Escalation: Requests UAC admin privileges to execute its payload.

    Persistence: Adds itself to the Windows Registry Run key to survive reboots.

    Data Exfiltration Beacon: Attempts to call out to a simulated Command & Control (C2) server.

    File "Encryption": Safely simulates file encryption by appending a .frostlocked extension to target files within a designated directory.

    Ransom Note: Drops and displays a realistic ransom note (!!!_READ_ME_!!!.txt).

    Inhibits Recovery: Attempts to delete Volume Shadow Copies to prevent easy restoration.

Prerequisites & Lab Setup

    Isolated Lab Environment: A virtualized Windows 11 machine (e.g., in VirtualBox or VMware) with no network connection to your host or primary network.

    Target Directory: Create a dedicated folder for the simulation to act upon:
    text

C:\simulation_target\

Python (for Building): On your build machine (e.g., Kali Linux), ensure Python 3.x is installed along with required libraries:
bash

    pip install pycryptodome pyinstaller requests

Installation & Deployment

    Build the Payload:

        Save the provided Python script as frostlocker_sim.py.

        Compile it into a standalone executable:
        bash

        pyinstaller --onefile --noconsole frostlocker_sim.py

        The resulting executable will be in the ./dist/ folder.

    Prepare the Decoy:

        Rename the compiled .exe file to something convincing (e.g., Invoice_INV-7842.pdf.exe).

    Deliver the Payload:

        Transfer the executable to the isolated Windows 11 VM (e.g., via a shared folder or virtual CD-ROM).

Execution & Simulation

    On the target Windows VM, double-click the Invoice_INV-7842.pdf.exe file.

    When the User Account Control (UAC) prompt appears, click "Yes". This is a critical step that simulates a user granting the attack elevated privileges.

    Observe the simulation:

        Files in C:\simulation_target\ will be renamed with a .frostlocked extension.

        A ransom note will pop up on the screen.

        The payload will be added to the startup registry.

Recovery & Cleanup

Since this is a simulation, recovery is straightforward.

Method 1: Revert VM Snapshot (Recommended)

    The fastest and cleanest method is to revert the virtual machine to a snapshot taken before the simulation.

Method 2: Manual Cleanup

    Boot into Safe Mode.

    Remove Persistence:

        Press Win + R, type regedit, and navigate to:
        HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run

        Delete the value named WindowsSecurityUpdate.

    Restore Files:

        Navigate to C:\simulation_target\.

        Manually rename all files, removing the .frostlocked extension.

Detection Points (For Blue Teams)

This simulation is designed to trigger common security controls. Look for:

    Network: Outbound HTTP POST requests to unknown domains.

    Endpoint: Process execution from unusual locations (e.g., Downloads, Temp).

    Registry: Modification of the HKCU\...\Run key.

    File System: Mass renaming of files with a new extension.

    System: The vssadmin delete shadows command being executed.

License

This project is licensed for educational use only. Redistribution is prohibited without explicit permission.

Remember: Ethical hacking is a powerful skill. Always use it responsibly, legally, and with permission.
