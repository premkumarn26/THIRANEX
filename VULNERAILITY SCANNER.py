VULNERAILITY SCANNER :

import socket
from datetime import datetime

known_vulnerabilities = {
    "Apache/2.4.49": "Critical - Path Traversal (CVE-2021-41773)",
    "OpenSSH_7.2": "Medium - Outdated OpenSSH version",
    "vsFTPd 2.3.4": "Critical - Backdoor Vulnerability",
}

def scan_ports(target, start_port=1, end_port=1024):
    open_ports = []

    print("=" * 50)
    print(" Vulnerability Scanner ")
    print("=" * 50)
    print(f"Scanning Target : {target}\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    return open_ports

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))

        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        except:
            pass

        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()

        return banner

    except:
        return "Unknown"

def check_vulnerability(banner):
    for software, issue in known_vulnerabilities.items():
        if software.lower() in banner.lower():
            return issue
    return "No known vulnerabilities found"

def weak_configuration(port):
    warnings = {
        21: "FTP detected - Credentials may be sent in plain text.",
        23: "Telnet detected - Insecure remote login.",
        80: "HTTP service detected - Consider HTTPS.",
        445: "SMB exposed - Verify access restrictions.",
        3389: "RDP exposed - Ensure strong authentication."
    }

    return warnings.get(port, "No common weak configuration.")

def generate_report(target, findings):
    filename = "Vulnerability_Report.txt"

    with open(filename, "w") as file:
        file.write("=" * 60 + "\n")
        file.write("        VULNERABILITY SCAN REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Target : {target}\n")
        file.write(f"Date   : {datetime.now()}\n\n")

        for item in findings:
            file.write(item + "\n")

    print(f"\nReport saved as '{filename}'")


def main():

    target = input("Enter Target IP or Hostname: ")

    findings = []

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid Hostname/IP")
        return

    open_ports = scan_ports(ip)

    if not open_ports:
        print("\nNo open ports found.")
        return

    print("\nDetailed Analysis")
    print("-" * 50)

    for port in open_ports:

        banner = grab_banner(ip, port)
        vulnerability = check_vulnerability(banner)
        warning = weak_configuration(port)

        print(f"\nPort : {port}")
        print(f"Banner         : {banner}")
        print(f"Vulnerability  : {vulnerability}")
        print(f"Configuration  : {warning}")

        findings.append(f"Port {port}")
        findings.append(f"Banner        : {banner}")
        findings.append(f"Vulnerability : {vulnerability}")
        findings.append(f"Configuration : {warning}")
        findings.append("-" * 50)

    generate_report(target, findings)

if __name__ == "__main__":
    main()

OUTPUT :


Enter Target IP or Hostname: scanme.nmap.org

==================================================
 Vulnerability Scanner
==================================================
Scanning Target : 45.33.xx.xx

[OPEN] Port 22
[OPEN] Port 80

Detailed Analysis
--------------------------------------------------

Port : 22
Banner         : SSH-2.0-OpenSSH_8.2
Vulnerability  : No known vulnerabilities found
Configuration  : No common weak configuration.

Port : 80
Banner         : HTTP/1.1 200 OK
Vulnerability  : No known vulnerabilities found
Configuration  : HTTP service detected - Consider HTTPS.

Report saved as 'Vulnerability_Report.txt'
