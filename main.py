import os
import sys
import time
import requests
import json
import random
import re

RESET="\033[0m"; BOLD="\033[1m"; GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; BLUE="\033[94m"; CYAN="\033[96m"; WHITE="\033[97m"; MAGENTA="\033[95m"

# ================== CONFIGURATION ==================
API_BASE = "https://wasifali.biz.id/public_apis/sim-info-api.php?search="
# ===================================================

def clear(): os.system("clear")

def show_banner():
    print(f"""{CYAN}{BOLD}
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
    ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {RED}⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⡀⠀
    {RED}⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
    {RED}⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
    {RED}⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
    {RED}⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
    {RED}⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
    {RED}⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
    {RED}⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛{RESET}
    {MAGENTA}{BOLD}       [ R O M A N   S I M   H A C K E R ]{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    {GREEN} DEV: {WHITE}ROMAN HACKER {GREEN}| TG: {WHITE}@romanempire078{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    """)

def hacker_loading(msg, duration=1.0):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{YELLOW}{BOLD}  [{frames[i % 4]}] {msg}...{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f"\r{GREEN}{BOLD}  [✓] {msg} DONE!{RESET}          \n")

def fake_sql_injection():
    queries = [
        "SELECT * FROM users WHERE mobile = '{}'",
        "UNION SELECT null, username, password FROM admins",
        "SELECT table_name FROM information_schema.tables",
        "UPDATE users SET access_level = 'ROOT' WHERE id = 1"
    ]
    print(f"\n{RED}{BOLD}  [!] INITIATING SQL INJECTION...{RESET}")
    for i in range(3):
        q = random.choice(queries)
        print(f"\033[91m  [SQL] {q}\033[0m")
        time.sleep(0.3)

def fake_proxy_routing():
    print(f"\n{CYAN}{BOLD}  [!] ROUTING VIA SECURE PROXIES...{RESET}")
    for _ in range(3):
        ip = f"{random.randint(11, 250)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        print(f"\033[93m  [PROXY] Connecting to Node {ip} -> OK\033[0m")
        time.sleep(0.2)

def fetch_and_display(query, search_type):
    clear()
    show_banner()
    
    fake_proxy_routing()
    hacker_loading(f"Bypassing NADRA Firewall for {search_type}", 1.2)
    fake_sql_injection()
    hacker_loading("Extracting Encrypted Data", 1.5)
    
    print(f"\n{YELLOW}  [~] Fetching Raw Payload from Server...{RESET}")
    time.sleep(1)
    
    url = API_BASE + query
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(f"{RED}  [!] Server Rejected Connection: {response.status_code}{RESET}")
            input(f"\n{CYAN}  Press ENTER to return...{RESET}")
            return
            
        try:
            data = response.json()
        except:
            print(f"{RED}  [!] Failed to Decrypt Payload.{RESET}")
            input(f"\n{CYAN}  Press ENTER to return...{RESET}")
            return

        hacker_loading("Decrypting AES-256 Payload", 1.2)
        
        records = []
        if isinstance(data, list): records = data
        elif isinstance(data, dict):
            if 'records' in data and isinstance(data['records'], list): records = data['records']
            elif 'data' in data and isinstance(data['data'], list): records = data['data']
            elif 'status' in data and data['status'] == 'error':
                print(f"\n{RED}  [X] TARGET NOT FOUND IN DATABASE.{RESET}")
                input(f"\n{CYAN}  Press ENTER to return...{RESET}")
                return
            else: records = [data]
                
        valid_records = [r for r in records if isinstance(r, dict) and any(r.values())]
                
        if not valid_records:
            print(f"\n{RED}  [X] NO RECORDS FOUND FOR {query}.{RESET}")
            input(f"\n{CYAN}  Press ENTER to return...{RESET}")
            return

        # Success Display
        clear()
        show_banner()
        print(f"\n{GREEN}{BOLD}  [✓] DATA BREACH SUCCESSFUL!{RESET}")
        print(f"{RED}  [!] TARGET: {WHITE}{query} ({search_type}){RESET}\n")
        
        for idx, rec in enumerate(valid_records, 1):
            name = rec.get('name', rec.get('fullname', 'Unknown'))
            mobile = rec.get('mobile', rec.get('number', 'N/A'))
            cnic = rec.get('cnic', rec.get('nic', 'N/A'))
            address = rec.get('address', rec.get('city', 'N/A'))
            network = rec.get('network', rec.get('carrier', 'N/A'))
            
            print(f"{CYAN}{BOLD}  ╔══════════════════════════════════════════════════╗")
            print(f"  ║               🔓 RECORD #{idx} DECRYPTED 🔓              ║")
            print(f"  ╠══════════════════════════════════════════════════╣")
            print(f"  ║  {YELLOW}NAME    : {WHITE}{str(name)[:35]:<35} {CYAN}║")
            print(f"  ║  {YELLOW}MOBILE  : {WHITE}{str(mobile)[:35]:<35} {CYAN}║")
            print(f"  ║  {YELLOW}CNIC    : {WHITE}{str(cnic)[:35]:<35} {CYAN}║")
            print(f"  ║  {YELLOW}ADDRESS : {WHITE}{str(address)[:35]:<35} {CYAN}║")
            print(f"  ║  {YELLOW}NETWORK : {WHITE}{str(network)[:35]:<35} {CYAN}║")
            print(f"  ╚══════════════════════════════════════════════════╝{RESET}\n")
            
        print(f"{MAGENTA}  ── HACKED BY ROMAN HACKER ──{RESET}\n")
            
    except requests.exceptions.Timeout:
        print(f"\n{RED}  [!] Error: Connection Timed Out.{RESET}")
    except requests.exceptions.ConnectionError:
        print(f"\n{RED}  [!] Error: No Internet Connection.{RESET}")
    except Exception as e:
        print(f"\n{RED}  [!] System Error: {e}{RESET}")

    input(f"{CYAN}  Press ENTER to return to main menu...{RESET}")

def search_by_number():
    clear()
    show_banner()
    print(f"{GREEN}{BOLD}  ► SEARCH BY MOBILE NUMBER{RESET}\n")
    number = input(f"{WHITE}  [?] Enter Mobile Number (e.g., 03001234567): {RESET}").strip()
    
    clean_num = ''.join(c for c in number if c.isdigit() or c == '+')
    if len(clean_num) < 10:
        print(f"{RED}  [!] Invalid Number! Please enter a valid mobile number.{RESET}")
        time.sleep(2)
        return
        
    fetch_and_display(clean_num, "Mobile")

def search_by_cnic():
    clear()
    show_banner()
    print(f"{GREEN}{BOLD}  ► SEARCH BY CNIC{RESET}\n")
    cnic = input(f"{WHITE}  [?] Enter CNIC without dashes (e.g., 3520112345671): {RESET}").strip()
    
    clean_cnic = ''.join(c for c in cnic if c.isdigit())
    if len(clean_cnic) != 13:
        print(f"{RED}  [!] Invalid CNIC! CNIC must be exactly 13 digits.{RESET}")
        time.sleep(2)
        return
        
    fetch_and_display(clean_cnic, "CNIC")

def main():
    while True:
        try:
            clear()
            show_banner()
            print(f"""{BLUE}{BOLD}
    ┌──────────────────────────────────────────────────┐
    │             ROMAN SIM DATABASE HACKER            │
    ├──────────────────────────────────────────────────┤
    │  {WHITE}[1]{GREEN} Search Ownership (By Number)              │
    │  {WHITE}[2]{GREEN} Search All Numbers (By CNIC)              │
    │  {WHITE}[3]{RED} Exit System                               │
    └──────────────────────────────────────────────────┘
{RESET}""")
            
            choice = input(f"{GREEN}{BOLD}  └──► Select Option [1-3]: {RESET}").strip()
            
            if choice == "1":
                search_by_number()
            elif choice == "2":
                search_by_cnic()
            elif choice == "3":
                print(f"\n{RED} Exiting System...{RESET}")
                time.sleep(1)
                break
            else:
                time.sleep(0.5)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
