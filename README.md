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
