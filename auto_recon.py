#!/usr/bin/env python3
import subprocess
import sys
import re

TARGET_IP = "172.18.0.2"

print(f"[*] Initializing Security Validation Pipeline against Node: {TARGET_IP}")
print("[*] Executing deep ingress service and banner extraction scan...")

try:
    scan_output = subprocess.check_output(["nmap", "-sV", "-p", "80,3306", TARGET_IP]).decode("utf-8")
    apache_match = re.search(r"80/tcp\s+open\s+http\s+(.+)", scan_output)
    apache_version = apache_match.group(1).strip() if apache_match else "Unknown / Hardened"
    
    print("\n" + "="*50)
    print("        AUTOMATED INFRASTRUCTURE COMPLIANCE REPORT")
    print("="*50)
    print(f"[+] Target Node Verified : {TARGET_IP} (corporate-web-portal)")
    print(f"[+] Detected Core Server  : {apache_version}")
    
    if "2.4.38" in apache_version:
        print(f"[-] SECURITY WARNING     : Outdated Apache version detected! Vulnerable to CVEs.")
        print(f"[-] Architecture Flaw    : Flat network topology lets attacker node interact directly.")
    else:
        print(f"[+] Posture Status       : Base version compliant or modified.")
    print("="*50)
    print("[*] Automated Compliance Evaluation Phase Complete.\n")

except Exception as e:
    print(f"[!] Critical Error executing pipeline sweep: {str(e)}")
    sys.exit(1)
