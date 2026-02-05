#  Python Multi-Threaded Port Scanner

A fast and efficient network scanner built with Python. This tool uses **Socket** programming and **Multi-threading** to scan open ports on a target IP or domain, identifying potential web servers and generating detailed reports.

## Key Features
* **Multi-threading:** Scans hundreds of ports simultaneously for high speed.
* **Service Detection:** Automatically identifies potential HTTP (80) and HTTPS (443) web servers.
* **Report Generation:** Saves the results automatically into a `.txt` file with timestamps.
* **User Friendly:** Interactive console menu with input validation.

## Prerequisites
* Python 3.x
* No external libraries required (uses native `socket` and `threading`).

## How to Run
1. Clone the repository:
   git clone https://github.com/Keverx/Port-Scanner-Python.git

2. Navigate to the folder:
    cd Port-Scanner-Python

3. Run the script:
     python PortScanner.py
