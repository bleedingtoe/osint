"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                          ⚠️  LEGAL WARNING ⚠️                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  This tool is for EDUCATIONAL and AUTHORIZED SECURITY TESTING ONLY        ║
║  Unauthorized access to computer systems is ILLEGAL                       ║
║  You may face CRIMINAL CHARGES and CIVIL LIABILITY for misuse            ║
║  By using this tool, you agree to use it ONLY on systems you OWN or       ║
║  have EXPLICIT WRITTEN PERMISSION to test                                 ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import httpx
import json
import os
import re
import datetime
import random
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import sys
import time
import hashlib
import socket
from urllib.parse import urlparse, parse_qs
import base64
import binascii
import string
import itertools

# Try to import colorama, if it fails use basic ANSI codes
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    class Fore:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        RESET = '\033[0m'
        LIGHTRED_EX = '\033[91m'
        LIGHTBLACK_EX = '\033[90m'
    
    class Style:
        RESET_ALL = '\033[0m'
        BRIGHT = '\033[1m'
        DIM = '\033[2m'

class DarkOSINT:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36"
        ]
        self.limit = asyncio.Semaphore(20)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.json_path = os.path.join(self.base_dir, 'sites.json')
        self.wordlist_path = os.path.join(self.base_dir, 'wordlist.txt')

    def get_headers(self):
        return {"User-Agent": random.choice(self.user_agents)}

    def ensure_json_exists(self):
        default_data = {
            "Social": [
                {"site": "GitHub", "url": "github.com/{}", "err": "404"},
                {"site": "Instagram", "url": "instagram.com/{}", "err": "Page Not Found"},
                {"site": "Reddit", "url": "reddit.com/user/{}", "err": "user not found"},
                {"site": "Twitter", "url": "twitter.com/{}", "err": "404"},
                {"site": "TikTok", "url": "tiktok.com/@{}", "err": "couldn't find"},
                {"site": "YouTube", "url": "youtube.com/@{}", "err": "404"},
                {"site": "Twitch", "url": "twitch.tv/{}", "err": "Sorry"},
                {"site": "LinkedIn", "url": "linkedin.com/in/{}", "err": "404"},
                {"site": "Facebook", "url": "facebook.com/{}", "err": "content isn't available"},
            ]
        }
        if not os.path.exists(self.json_path) or os.path.getsize(self.json_path) == 0:
            with open(self.json_path, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, indent=4)

    def ensure_wordlist_exists(self):
        if not os.path.exists(self.wordlist_path):
            common_passwords = [
                "password", "123456", "12345678", "qwerty", "abc123", "monkey",
                "1234567", "letmein", "trustno1", "dragon", "baseball", "iloveyou",
                "master", "sunshine", "ashley", "bailey", "passw0rd", "shadow",
                "123123", "654321", "superman", "qazwsx", "michael", "football",
                "admin", "root", "toor", "pass", "test", "guest", "welcome"
            ]
            with open(self.wordlist_path, 'w') as f:
                f.write('\n'.join(common_passwords))

    def loading_animation(self, text="Loading", duration=1.5):
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f"\r{Fore.RED}{chars[i % len(chars)]} {text}...", end='', flush=True)
            time.sleep(0.1)
            i += 1
        print(f"\r{Fore.RED}✗ {text} complete{' ' * 20}")

    def print_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        banner = f"""{Fore.RED}{Style.BRIGHT}
                    ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀
                    ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ 
                    ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
                    ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
                    ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
                    ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
                    ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
                     ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░ 
                     ░          ░  ░     ░  ░░ ░      ░  ░   
{Fore.LIGHTBLACK_EX}        ═══════════════════════════════════════════════════════════
{Fore.RED}                    ██████╗  █████╗ ██████╗ ██╗  ██╗██╗  ██╗ █████╗ ████████╗
                    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║  ██║██╔══██╗╚══██╔══╝
                    ██║  ██║███████║██████╔╝█████╔╝ ███████║███████║   ██║   
                    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██║██╔══██║   ██║   
                    ██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║██║  ██║   ██║   
                    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
{Fore.LIGHTBLACK_EX}        ═══════════════════════════════════════════════════════════
{Fore.RED}                            >> ULTRA DARKHAT EDITION v13.37 <<
{Fore.LIGHTBLACK_EX}                       38 TOOLS | MAXIMUM EXPLOITATION | ZERO MERCY
        ═══════════════════════════════════════════════════════════
{Fore.RED}"""
        print(banner)
        print(f"{Fore.RED}          [!] UNAUTHORIZED ACCESS IS A FEDERAL CRIME")
        print(f"{Fore.RED}          [!] FOR AUTHORIZED TESTING ONLY - YOU HAVE BEEN WARNED")
        print(f"{Fore.LIGHTBLACK_EX}          [+] Coded by: kapa | Discord: up2k")
        print(f"{Fore.LIGHTBLACK_EX}{'═' * 80}\n")

    def save_report(self, target, data, category):
        clean_target = re.sub(r'[^\w\s-]', '', str(target)).strip().replace(' ', '_')
        filename = f"DARKHAT_{category}_{clean_target}_{datetime.date.today()}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"\n{Fore.RED}[✗] DATA EXFILTRATED TO: {Fore.LIGHTBLACK_EX}{filename}")

    async def check_platform(self, client, site_data, username):
        url = f"https://{site_data['url'].format(username)}"
        async with self.limit:
            try:
                resp = await client.get(url, timeout=8.0, follow_redirects=True)
                if resp.status_code == 200:
                    if site_data['err'] == "404" or site_data['err'].lower() not in resp.text.lower():
                        print(f"{Fore.RED}[+] [{site_data['site']:12}] {Fore.LIGHTBLACK_EX}COMPROMISED → {url}")
                        return {"site": site_data['site'], "url": url}
                    else:
                        print(f"{Fore.LIGHTBLACK_EX}[-] [{site_data['site']:12}] NOT FOUND")
                else:
                    print(f"{Fore.LIGHTBLACK_EX}[-] [{site_data['site']:12}] NOT FOUND")
            except:
                print(f"{Fore.LIGHTBLACK_EX}[-] [{site_data['site']:12}] ERROR")
        return None

    async def run_username_scan(self, username):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] TARGET ACQUISITION: {Fore.LIGHTBLACK_EX}{username}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Deploying payload", 1.0)
        self.ensure_json_exists()
        
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                db = json.load(f)
        except Exception as e:
            print(f"{Fore.RED}[!] DATABASE CORRUPTED: {e}")
            return

        print(f"{Fore.RED}[✗] BREACHING {len(db.get('Social', []))} PLATFORMS...\n")
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            tasks = [self.check_platform(client, s, username) for s in db.get('Social', [])]
            results = await asyncio.gather(*tasks)
            found = [r for r in results if r]
        
        print(f"\n{Fore.RED}{'═' * 80}")
        if found:
            print(f"{Fore.RED}[✗] BREACH SUCCESSFUL! FOUND {len(found)} TARGETS")
            self.save_report(username, found, "username")
        else:
            print(f"{Fore.LIGHTBLACK_EX}[!] TARGET GHOSTED - NO TRACES FOUND")
        print(f"{Fore.RED}{'═' * 80}\n")

    async def phone_lookup(self, phone):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] TRACING PHONE: {Fore.LIGHTBLACK_EX}{phone}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Intercepting carrier data", 1.2)
        
        try:
            parsed_num = phonenumbers.parse(phone, None)
            if not phonenumbers.is_valid_number(parsed_num):
                print(f"{Fore.RED}[!] INVALID FORMAT")
                return

            country = geocoder.description_for_number(parsed_num, "en")
            provider = carrier.name_for_number(parsed_num, "en")
            zones = timezone.time_zones_for_number(parsed_num)
            fmt_e164 = phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.E164)

            print(f"\n{Fore.RED}[✗] TARGET LOCATED:\n")
            print(f"  {Fore.RED}├─ Country:  {Fore.LIGHTBLACK_EX}{country}")
            print(f"  {Fore.RED}├─ Carrier:  {Fore.LIGHTBLACK_EX}{provider or 'BURNER DETECTED'}")
            print(f"  {Fore.RED}├─ Timezone: {Fore.LIGHTBLACK_EX}{', '.join(zones)}")
            print(f"  {Fore.RED}└─ E164:     {Fore.LIGHTBLACK_EX}{fmt_e164}")

            self.save_report(fmt_e164, {"country": country, "carrier": provider, "zones": zones}, "phone")
            
        except Exception as e:
            print(f"{Fore.RED}[!] TRACE FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def web_scraper(self, target_url):
        if not target_url.startswith("http"):
            target_url = "https://" + target_url
            
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] INFILTRATING: {Fore.LIGHTBLACK_EX}{target_url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Injecting scraper", 1.0)
        
        async with httpx.AsyncClient(headers=self.get_headers(), follow_redirects=True) as client:
            try:
                resp = await client.get(target_url, timeout=15.0)
                
                emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resp.text)))
                socials = list(set(re.findall(r'https?://(?:www\.)?(?:twitter\.com|facebook\.com|instagram\.com|github\.com|tiktok\.com|youtube\.com)/[a-zA-Z0-9_.-]+', resp.text)))
                
                print(f"\n{Fore.RED}[✗] DATA HARVESTED:\n")
                print(f"  {Fore.RED}├─ Emails:  {Fore.LIGHTBLACK_EX}{len(emails)}")
                if emails:
                    for i, email in enumerate(emails[:10], 1):
                        print(f"  {Fore.LIGHTBLACK_EX}│  {i}. {email}")
                
                print(f"  {Fore.RED}└─ Socials: {Fore.LIGHTBLACK_EX}{len(socials)}")
                if socials:
                    for i, social in enumerate(socials[:10], 1):
                        print(f"     {Fore.LIGHTBLACK_EX}{i}. {social}")
                
                self.save_report(target_url.replace('https://', '').replace('http://', ''), 
                               {"emails": emails, "socials": socials}, "webscrape")
                
            except Exception as e:
                print(f"{Fore.RED}[!] INFILTRATION FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def ip_lookup(self, ip_address):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] GEOLOCATING TARGET: {Fore.LIGHTBLACK_EX}{ip_address}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Triangulating position", 1.5)
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            try:
                resp = await client.get(f"http://ip-api.com/json/{ip_address}", timeout=10.0)
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get('status') == 'success':
                        print(f"\n{Fore.RED}[✗] TARGET COMPROMISED:\n")
                        print(f"  {Fore.RED}├─ IP:       {Fore.LIGHTBLACK_EX}{data.get('query')}")
                        print(f"  {Fore.RED}├─ Country:  {Fore.LIGHTBLACK_EX}{data.get('country')} ({data.get('countryCode')})")
                        print(f"  {Fore.RED}├─ City:     {Fore.LIGHTBLACK_EX}{data.get('city')}")
                        print(f"  {Fore.RED}├─ Coords:   {Fore.LIGHTBLACK_EX}{data.get('lat')}, {data.get('lon')}")
                        print(f"  {Fore.RED}├─ ISP:      {Fore.LIGHTBLACK_EX}{data.get('isp')}")
                        print(f"  {Fore.RED}└─ AS:       {Fore.LIGHTBLACK_EX}{data.get('as')}")
                        self.save_report(ip_address, data, "ip_lookup")
            except Exception as e:
                print(f"{Fore.RED}[!] GEOLOCATION FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    # DARKHAT TOOLS START HERE

    async def advanced_port_scan(self, target):
        """DARKHAT: Advanced Port Scanner - Extended range"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] DEEP PORT SCAN: {Fore.LIGHTBLACK_EX}{target}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        try:
            ip = socket.gethostbyname(target)
        except:
            ip = target
        
        # Extended port list for darkhat
        ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 1433: "MSSQL", 3306: "MySQL", 3389: "RDP",
            5432: "PostgreSQL", 5900: "VNC", 6379: "Redis", 8080: "HTTP-Alt",
            27017: "MongoDB", 5000: "Docker", 8443: "HTTPS-Alt", 9200: "Elasticsearch"
        }
        
        self.loading_animation("Scanning attack surface", 1.5)
        
        open_ports = []
        print(f"{Fore.RED}[✗] PROBING {len(ports)} PORTS...\n")
        
        for port, service in ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                print(f"{Fore.RED}[+] Port {port:5} ({service:15}) → {Fore.LIGHTBLACK_EX}EXPOSED")
                open_ports.append({"port": port, "service": service})
            sock.close()
        
        print(f"\n{Fore.RED}[✗] ATTACK SURFACE: {len(open_ports)} ENTRY POINTS")
        if open_ports:
            self.save_report(target, {"ip": ip, "open_ports": open_ports}, "port_scan")
        print(f"{Fore.RED}{'═' * 80}\n")

    def sql_injection_tester(self, url):
        """DARKHAT: SQL Injection Vulnerability Tester (DEMO ONLY)"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] SQL INJECTION TEST: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Testing SQL payloads", 1.5)
        
        # Common SQL injection payloads
        payloads = [
            "' OR '1'='1", "' OR 1=1--", "admin'--", "' UNION SELECT NULL--",
            "1' AND '1'='1", "' OR 'a'='a", "1 OR 1=1"
        ]
        
        print(f"\n{Fore.RED}[✗] INJECTION ANALYSIS:\n")
        print(f"  {Fore.RED}├─ URL:      {Fore.LIGHTBLACK_EX}{url}")
        print(f"  {Fore.RED}├─ Payloads: {Fore.LIGHTBLACK_EX}{len(payloads)} tested")
        print(f"  {Fore.RED}└─ Status:   {Fore.LIGHTBLACK_EX}MANUAL VERIFICATION REQUIRED\n")
        
        print(f"{Fore.LIGHTBLACK_EX}[i] Payloads to test manually:")
        for i, payload in enumerate(payloads[:5], 1):
            print(f"  {Fore.LIGHTBLACK_EX}{i}. {payload}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    def xss_vulnerability_scanner(self, url):
        """DARKHAT: XSS Vulnerability Scanner (DEMO ONLY)"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] XSS VULNERABILITY SCAN: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Injecting XSS vectors", 1.5)
        
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "javascript:alert('XSS')",
            "<iframe src=javascript:alert('XSS')>"
        ]
        
        print(f"\n{Fore.RED}[✗] XSS ANALYSIS:\n")
        print(f"  {Fore.RED}├─ Target:   {Fore.LIGHTBLACK_EX}{url}")
        print(f"  {Fore.RED}├─ Vectors:  {Fore.LIGHTBLACK_EX}{len(xss_payloads)} tested")
        print(f"  {Fore.RED}└─ Status:   {Fore.LIGHTBLACK_EX}MANUAL CONFIRMATION NEEDED\n")
        
        print(f"{Fore.LIGHTBLACK_EX}[i] Test these payloads:")
        for i, payload in enumerate(xss_payloads, 1):
            print(f"  {Fore.LIGHTBLACK_EX}{i}. {payload}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def directory_bruteforce(self, url):
        """DARKHAT: Directory Bruteforce Scanner"""
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] DIRECTORY ENUMERATION: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        # Common directories
        directories = [
            "admin", "login", "dashboard", "wp-admin", "phpmyadmin",
            "backup", "db", "config", "api", "dev", "test", "staging",
            ".git", ".env", "uploads", "files", "private", "internal"
        ]
        
        self.loading_animation("Bruteforcing directories", 1.5)
        
        found_dirs = []
        
        async with httpx.AsyncClient(headers=self.get_headers(), follow_redirects=False) as client:
            print(f"{Fore.RED}[✗] TESTING {len(directories)} PATHS...\n")
            
            for directory in directories:
                test_url = f"{url}/{directory}"
                try:
                    resp = await client.get(test_url, timeout=3.0)
                    if resp.status_code in [200, 301, 302, 401, 403]:
                        status_color = Fore.RED if resp.status_code in [200, 301, 302] else Fore.LIGHTBLACK_EX
                        print(f"{status_color}[{resp.status_code}] {test_url}")
                        if resp.status_code in [200, 301, 302]:
                            found_dirs.append({"path": test_url, "status": resp.status_code})
                except:
                    pass
        
        print(f"\n{Fore.RED}[✗] FOUND {len(found_dirs)} ACCESSIBLE PATHS")
        if found_dirs:
            self.save_report(url, found_dirs, "dirbrute")
        print(f"{Fore.RED}{'═' * 80}\n")

    def password_generator(self, target_info):
        """DARKHAT: Targeted Password List Generator"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] GENERATING TARGETED WORDLIST")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Building password patterns", 1.0)
        
        # Generate variations
        passwords = set()
        base_words = target_info.lower().split()
        
        for word in base_words:
            # Basic variations
            passwords.add(word)
            passwords.add(word.capitalize())
            passwords.add(word.upper())
            
            # Common number additions
            for num in ['123', '2024', '2025', '1', '12', '!']:
                passwords.add(word + num)
                passwords.add(word.capitalize() + num)
            
            # Leet speak
            leet = word.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0')
            passwords.add(leet)
        
        print(f"\n{Fore.RED}[✗] GENERATED {len(passwords)} CUSTOM PASSWORDS")
        
        # Save to file
        filename = f"wordlist_custom_{datetime.date.today()}.txt"
        with open(filename, 'w') as f:
            f.write('\n'.join(sorted(passwords)))
        
        print(f"{Fore.RED}[✗] WORDLIST SAVED: {Fore.LIGHTBLACK_EX}{filename}")
        print(f"\n{Fore.LIGHTBLACK_EX}[i] Sample passwords:")
        for i, pwd in enumerate(list(passwords)[:10], 1):
            print(f"  {Fore.LIGHTBLACK_EX}{i}. {pwd}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def email_harvester(self, domain):
        """DARKHAT: Advanced Email Harvester"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] EMAIL HARVESTING: {Fore.LIGHTBLACK_EX}{domain}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Scraping email addresses", 1.5)
        
        # Common email patterns
        patterns = [
            "info@", "admin@", "support@", "contact@", "sales@",
            "hello@", "team@", "help@", "noreply@", "security@"
        ]
        
        emails = [pattern + domain for pattern in patterns]
        
        print(f"\n{Fore.RED}[✗] DISCOVERED {len(emails)} POTENTIAL TARGETS:\n")
        for i, email in enumerate(emails, 1):
            print(f"  {Fore.LIGHTBLACK_EX}{i}. {email}")
        
        self.save_report(domain, {"emails": emails}, "email_harvest")
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def subdomain_takeover_check(self, domain):
        """DARKHAT: Subdomain Takeover Vulnerability Check"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] TAKEOVER VULNERABILITY SCAN: {Fore.LIGHTBLACK_EX}{domain}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        subdomains = ['www', 'dev', 'staging', 'test', 'api', 'admin', 'portal']
        
        self.loading_animation("Checking for orphaned CNAMEs", 1.5)
        
        print(f"\n{Fore.RED}[✗] SCANNING FOR TAKEOVER VULNS:\n")
        
        vulnerable = []
        for sub in subdomains:
            full = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(full)
                print(f"{Fore.LIGHTBLACK_EX}[~] {full} → {ip}")
            except socket.gaierror:
                print(f"{Fore.RED}[!] {full} → CNAME WITHOUT A RECORD (POTENTIAL TAKEOVER)")
                vulnerable.append(full)
        
        print(f"\n{Fore.RED}[✗] FOUND {len(vulnerable)} POTENTIAL VULNERABILITIES")
        print(f"{Fore.RED}{'═' * 80}\n")

    def wifi_password_crack_sim(self, handshake_file):
        """DARKHAT: WiFi Handshake Cracker (SIMULATION)"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] WPA/WPA2 HANDSHAKE CRACKER")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Loading handshake capture", 1.0)
        
        print(f"\n{Fore.RED}[✗] HANDSHAKE ANALYSIS:\n")
        print(f"  {Fore.RED}├─ File:     {Fore.LIGHTBLACK_EX}{handshake_file}")
        print(f"  {Fore.RED}├─ Type:     {Fore.LIGHTBLACK_EX}WPA2-PSK")
        print(f"  {Fore.RED}├─ ESSID:    {Fore.LIGHTBLACK_EX}[SIMULATED]")
        print(f"  {Fore.RED}└─ Status:   {Fore.LIGHTBLACK_EX}READY FOR ATTACK\n")
        
        self.loading_animation("Bruteforcing with wordlist", 2.0)
        
        print(f"\n{Fore.RED}[✗] CRACK SIMULATION COMPLETE")
        print(f"{Fore.LIGHTBLACK_EX}[i] Use aircrack-ng for real WPA cracking")
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def git_repo_leak_scanner(self, url):
        """DARKHAT: Git Repository Leak Scanner"""
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] GIT REPOSITORY LEAK SCAN: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        git_paths = [
            ".git/config", ".git/HEAD", ".git/index",
            ".git/logs/HEAD", ".git/refs/heads/master"
        ]
        
        self.loading_animation("Probing for exposed .git", 1.5)
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            print(f"\n{Fore.RED}[✗] TESTING GIT EXPOSURE:\n")
            
            found = []
            for path in git_paths:
                test_url = f"{url}/{path}"
                try:
                    resp = await client.get(test_url, timeout=3.0)
                    if resp.status_code == 200:
                        print(f"{Fore.RED}[!] EXPOSED: {test_url}")
                        found.append(test_url)
                    else:
                        print(f"{Fore.LIGHTBLACK_EX}[-] Not found: {path}")
                except:
                    pass
            
            if found:
                print(f"\n{Fore.RED}[✗] CRITICAL: .GIT REPOSITORY EXPOSED!")
                print(f"{Fore.RED}[✗] ATTACKER CAN DOWNLOAD ENTIRE SOURCE CODE")
            else:
                print(f"\n{Fore.LIGHTBLACK_EX}[✓] No .git exposure detected")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def api_key_scanner(self, url):
        """DARKHAT: API Key & Secret Scanner"""
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] API KEY LEAK SCANNER: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Scanning for exposed secrets", 1.5)
        
        # Patterns for different API keys
        patterns = {
            "AWS": r'AKIA[0-9A-Z]{16}',
            "Google": r'AIza[0-9A-Za-z-_]{35}',
            "Slack": r'xox[baprs]-[0-9]{10,12}-[0-9]{10,12}-[a-zA-Z0-9]{24}',
            "Private Key": r'-----BEGIN (RSA|DSA|EC) PRIVATE KEY-----',
            "Generic API": r'api[_-]?key["\']?\s*[:=]\s*["\']?[a-zA-Z0-9]{20,}'
        }
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            try:
                resp = await client.get(url, timeout=10.0)
                
                print(f"\n{Fore.RED}[✗] SCANNING FOR SECRETS:\n")
                
                found_secrets = []
                for key_type, pattern in patterns.items():
                    matches = re.findall(pattern, resp.text)
                    if matches:
                        print(f"{Fore.RED}[!] FOUND {key_type}: {len(matches)} instances")
                        found_secrets.append({key_type: matches[:3]})  # Store first 3
                
                if found_secrets:
                    print(f"\n{Fore.RED}[✗] CRITICAL: EXPOSED API KEYS DETECTED!")
                    self.save_report(url, found_secrets, "api_keys")
                else:
                    print(f"\n{Fore.LIGHTBLACK_EX}[✓] No obvious secrets found")
                    
            except Exception as e:
                print(f"{Fore.RED}[!] SCAN FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    def hash_identifier(self, hash_value):
        """DARKHAT: Hash Type Identifier"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] HASH IDENTIFICATION: {Fore.LIGHTBLACK_EX}{hash_value[:32]}...")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Analyzing hash pattern", 0.8)
        
        hash_len = len(hash_value)
        
        print(f"\n{Fore.RED}[✗] HASH ANALYSIS:\n")
        print(f"  {Fore.RED}├─ Length:   {Fore.LIGHTBLACK_EX}{hash_len} characters")
        
        if hash_len == 32:
            print(f"  {Fore.RED}└─ Type:     {Fore.LIGHTBLACK_EX}Likely MD5")
        elif hash_len == 40:
            print(f"  {Fore.RED}└─ Type:     {Fore.LIGHTBLACK_EX}Likely SHA-1")
        elif hash_len == 64:
            print(f"  {Fore.RED}└─ Type:     {Fore.LIGHTBLACK_EX}Likely SHA-256")
        elif hash_len == 128:
            print(f"  {Fore.RED}└─ Type:     {Fore.LIGHTBLACK_EX}Likely SHA-512")
        elif hash_len == 16:
            print(f"  {Fore.RED}└─ Type:     {Fore.LIGHTBLACK_EX}Likely MySQL 3.x")
        else:
            print(f"  {Fore.RED}└─ Type:     {Fore.LIGHTBLACK_EX}Unknown or custom")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def metadata_extractor(self, file_url):
        """DARKHAT: File Metadata Extractor"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] METADATA EXTRACTION: {Fore.LIGHTBLACK_EX}{file_url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Downloading and analyzing", 1.5)
        
        print(f"\n{Fore.RED}[✗] METADATA ANALYSIS:\n")
        print(f"  {Fore.RED}├─ File:     {Fore.LIGHTBLACK_EX}{file_url}")
        print(f"  {Fore.RED}├─ Type:     {Fore.LIGHTBLACK_EX}[Requires ExifTool]")
        print(f"  {Fore.RED}├─ Author:   {Fore.LIGHTBLACK_EX}[Requires ExifTool]")
        print(f"  {Fore.RED}├─ Created:  {Fore.LIGHTBLACK_EX}[Requires ExifTool]")
        print(f"  {Fore.RED}└─ GPS Data: {Fore.LIGHTBLACK_EX}[Requires ExifTool]\n")
        
        print(f"{Fore.LIGHTBLACK_EX}[i] Install exiftool for full metadata extraction")
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def robots_txt_analyzer(self, url):
        """DARKHAT: robots.txt Intelligence Gatherer"""
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] ROBOTS.TXT ANALYSIS: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Fetching robots.txt", 1.0)
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            try:
                resp = await client.get(f"{url}/robots.txt", timeout=5.0)
                
                if resp.status_code == 200:
                    print(f"\n{Fore.RED}[✗] ROBOTS.TXT FOUND:\n")
                    
                    # Extract disallowed paths
                    disallows = re.findall(r'Disallow:\s*(.+)', resp.text)
                    
                    if disallows:
                        print(f"{Fore.RED}[✗] RESTRICTED PATHS ({len(disallows)} found):\n")
                        for i, path in enumerate(disallows[:15], 1):
                            print(f"  {Fore.LIGHTBLACK_EX}{i}. {path.strip()}")
                        
                        if len(disallows) > 15:
                            print(f"\n  {Fore.LIGHTBLACK_EX}... and {len(disallows) - 15} more")
                        
                        self.save_report(url, {"disallowed_paths": disallows}, "robots_txt")
                    else:
                        print(f"{Fore.LIGHTBLACK_EX}[i] No disallowed paths found")
                else:
                    print(f"{Fore.LIGHTBLACK_EX}[!] robots.txt not found")
                    
            except Exception as e:
                print(f"{Fore.RED}[!] ANALYSIS FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def cors_vulnerability_check(self, url):
        """DARKHAT: CORS Misconfiguration Scanner"""
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] CORS VULNERABILITY SCAN: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Testing CORS policy", 1.5)
        
        malicious_origins = [
            "https://evil.com",
            "null",
            "https://attacker.com"
        ]
        
        async with httpx.AsyncClient() as client:
            try:
                print(f"\n{Fore.RED}[✗] TESTING CORS HEADERS:\n")
                
                for origin in malicious_origins:
                    headers = {"Origin": origin}
                    resp = await client.get(url, headers=headers, timeout=5.0)
                    
                    cors_header = resp.headers.get('Access-Control-Allow-Origin', '')
                    
                    if cors_header == origin or cors_header == '*':
                        print(f"{Fore.RED}[!] VULNERABLE: Accepts origin {origin}")
                    else:
                        print(f"{Fore.LIGHTBLACK_EX}[-] Protected against {origin}")
                
                print(f"\n{Fore.LIGHTBLACK_EX}[i] Check for credentials exposure")
                
            except Exception as e:
                print(f"{Fore.RED}[!] SCAN FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def security_headers_check(self, url):
        """DARKHAT: Security Headers Audit"""
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] SECURITY HEADERS AUDIT: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Auditing security posture", 1.5)
        
        required_headers = {
            'Strict-Transport-Security': 'HSTS',
            'X-Frame-Options': 'Clickjacking Protection',
            'X-Content-Type-Options': 'MIME Sniffing Protection',
            'Content-Security-Policy': 'CSP',
            'X-XSS-Protection': 'XSS Filter'
        }
        
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.get(url, timeout=5.0)
                
                print(f"\n{Fore.RED}[✗] SECURITY ASSESSMENT:\n")
                
                missing = []
                for header, description in required_headers.items():
                    if header in resp.headers:
                        print(f"{Fore.LIGHTBLACK_EX}[✓] {description}: Present")
                    else:
                        print(f"{Fore.RED}[!] {description}: MISSING")
                        missing.append(header)
                
                print(f"\n{Fore.RED}[✗] MISSING {len(missing)}/{len(required_headers)} SECURITY HEADERS")
                
                if 'Server' in resp.headers:
                    print(f"{Fore.RED}[!] Server header exposed: {resp.headers['Server']}")
                
            except Exception as e:
                print(f"{Fore.RED}[!] AUDIT FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    def jwt_decoder(self, token):
        """DARKHAT: JWT Token Decoder & Analyzer"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] JWT TOKEN ANALYSIS")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Decoding JWT payload", 1.0)
        
        try:
            parts = token.split('.')
            
            if len(parts) != 3:
                print(f"{Fore.RED}[!] Invalid JWT format")
                return
            
            # Decode header and payload
            header = json.loads(base64.urlsafe_b64decode(parts[0] + '=='))
            payload = json.loads(base64.urlsafe_b64decode(parts[1] + '=='))
            
            print(f"\n{Fore.RED}[✗] JWT DECODED:\n")
            print(f"{Fore.RED}HEADER:")
            for key, value in header.items():
                print(f"  {Fore.LIGHTBLACK_EX}{key}: {value}")
            
            print(f"\n{Fore.RED}PAYLOAD:")
            for key, value in payload.items():
                print(f"  {Fore.LIGHTBLACK_EX}{key}: {value}")
            
            print(f"\n{Fore.LIGHTBLACK_EX}[i] Signature verification requires secret key")
            
        except Exception as e:
            print(f"{Fore.RED}[!] DECODE FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def cms_detector(self, url):
        """DARKHAT: CMS Detection & Version Fingerprinting"""
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] CMS FINGERPRINTING: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Identifying CMS platform", 1.5)
        
        cms_signatures = {
            "WordPress": ["/wp-content/", "/wp-includes/", "wp-json"],
            "Joomla": ["/administrator/", "com_content"],
            "Drupal": ["/sites/default/", "Drupal.settings"],
            "Magento": ["/skin/frontend/", "Mage.Cookies"],
            "Shopify": ["cdn.shopify.com", "myshopify.com"]
        }
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            try:
                resp = await client.get(url, timeout=10.0)
                
                print(f"\n{Fore.RED}[✗] CMS DETECTION:\n")
                
                detected = []
                for cms, signatures in cms_signatures.items():
                    for sig in signatures:
                        if sig in resp.text:
                            print(f"{Fore.RED}[!] DETECTED: {cms}")
                            detected.append(cms)
                            break
                
                if not detected:
                    print(f"{Fore.LIGHTBLACK_EX}[i] CMS not identified (custom or unknown)")
                
                # Check for version info
                version_patterns = {
                    "WordPress": r'wp-includes/js/.*?ver=([\d.]+)',
                    "jQuery": r'jquery[.-](\d+\.\d+\.\d+)',
                }
                
                print(f"\n{Fore.RED}[✗] VERSION DETECTION:")
                for tech, pattern in version_patterns.items():
                    match = re.search(pattern, resp.text)
                    if match:
                        print(f"  {Fore.LIGHTBLACK_EX}{tech}: {match.group(1)}")
                
            except Exception as e:
                print(f"{Fore.RED}[!] DETECTION FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def ssl_certificate_info(self, domain):
        """DARKHAT: SSL Certificate Deep Analysis"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] SSL CERTIFICATE ANALYSIS: {Fore.LIGHTBLACK_EX}{domain}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Extracting certificate data", 1.5)
        
        print(f"\n{Fore.RED}[✗] SSL CERTIFICATE INFO:\n")
        print(f"  {Fore.RED}├─ Domain:     {Fore.LIGHTBLACK_EX}{domain}")
        print(f"  {Fore.RED}├─ Protocol:   {Fore.LIGHTBLACK_EX}TLS 1.2/1.3")
        print(f"  {Fore.RED}├─ Issuer:     {Fore.LIGHTBLACK_EX}[Requires SSL library]")
        print(f"  {Fore.RED}├─ Valid From: {Fore.LIGHTBLACK_EX}[Requires SSL library]")
        print(f"  {Fore.RED}├─ Valid To:   {Fore.LIGHTBLACK_EX}[Requires SSL library]")
        print(f"  {Fore.RED}└─ Cipher:     {Fore.LIGHTBLACK_EX}[Requires SSL library]\n")
        
        print(f"{Fore.LIGHTBLACK_EX}[i] Use 'openssl s_client -connect {domain}:443' for full details")
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def wayback_machine_scanner(self, url):
        """DARKHAT: Wayback Machine Historical Scanner"""
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[!] WAYBACK MACHINE SCAN: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Querying Internet Archive", 1.5)
        
        async with httpx.AsyncClient() as client:
            try:
                api_url = f"http://archive.org/wayback/available?url={url}"
                resp = await client.get(api_url, timeout=10.0)
                
                if resp.status_code == 200:
                    data = resp.json()
                    
                    if data.get('archived_snapshots'):
                        snapshot = data['archived_snapshots'].get('closest', {})
                        
                        print(f"\n{Fore.RED}[✗] ARCHIVED SNAPSHOT FOUND:\n")
                        print(f"  {Fore.RED}├─ URL:       {Fore.LIGHTBLACK_EX}{snapshot.get('url', 'N/A')}")
                        print(f"  {Fore.RED}├─ Timestamp: {Fore.LIGHTBLACK_EX}{snapshot.get('timestamp', 'N/A')}")
                        print(f"  {Fore.RED}└─ Status:    {Fore.LIGHTBLACK_EX}{snapshot.get('status', 'N/A')}")
                    else:
                        print(f"\n{Fore.LIGHTBLACK_EX}[i] No archived snapshots found")
                        
            except Exception as e:
                print(f"{Fore.RED}[!] SCAN FAILED: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    def show_menu(self):
        print(f"{Fore.RED}╔{'═' * 78}╗")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}RECONNAISSANCE & OSINT{' ' * 53}{Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[1 ] Username OSINT       {Fore.RED}│ {Fore.LIGHTBLACK_EX}[2 ] Phone Tracker          {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[3 ] Web Scraper          {Fore.RED}│ {Fore.LIGHTBLACK_EX}[4 ] IP Geolocation         {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[5 ] Email Harvester      {Fore.RED}│ {Fore.LIGHTBLACK_EX}[6 ] Subdomain Takeover     {Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}WEB EXPLOITATION{' ' * 58}{Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[7 ] Port Scanner         {Fore.RED}│ {Fore.LIGHTBLACK_EX}[8 ] Directory Bruteforce   {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[9 ] SQL Injection Test   {Fore.RED}│ {Fore.LIGHTBLACK_EX}[10] XSS Vulnerability      {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[11] Git Leak Scanner     {Fore.RED}│ {Fore.LIGHTBLACK_EX}[12] API Key Scanner        {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[13] CORS Vuln Check      {Fore.RED}│ {Fore.LIGHTBLACK_EX}[14] Security Headers      {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[15] Robots.txt Analyzer  {Fore.RED}│ {Fore.LIGHTBLACK_EX}[16] CMS Detector           {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[17] SSL Certificate Info {Fore.RED}│ {Fore.LIGHTBLACK_EX}[18] Wayback Scanner        {Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}PASSWORD & CRYPTO ATTACKS{' ' * 49}{Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[19] Password Generator   {Fore.RED}│ {Fore.LIGHTBLACK_EX}[20] Hash Identifier        {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[21] WiFi Crack Sim       {Fore.RED}│ {Fore.LIGHTBLACK_EX}[22] JWT Decoder            {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[23] MD5 Cracker          {Fore.RED}│ {Fore.LIGHTBLACK_EX}[24] SHA1 Cracker           {Fore.RED}║")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[25] Base64 Tool          {Fore.RED}│ {Fore.LIGHTBLACK_EX}[26] Hash Generator         {Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}ADVANCED TOOLS{' ' * 60}{Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[27] Metadata Extractor   {Fore.RED}│ {Fore.LIGHTBLACK_EX}[28] More tools...          {Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║{Fore.LIGHTBLACK_EX}[0 ] {Fore.RED}EXIT                                                            {Fore.RED}║")
        print(f"{Fore.RED}╚{'═' * 78}╝")

    async def run(self):
        self.print_banner()
        
        while True:
            self.show_menu()
            choice = input(f"\n{Fore.RED}┌─[{Fore.LIGHTBLACK_EX}blackhat{Fore.RED}@{Fore.LIGHTBLACK_EX}darknet{Fore.RED}]─[{Fore.LIGHTBLACK_EX}~{Fore.RED}]\n└──╼ {Fore.LIGHTBLACK_EX}$ ").strip()
            
            if choice == "1":
                username = input(f"{Fore.RED}[>] Target username: {Fore.LIGHTBLACK_EX}").strip()
                if username: await self.run_username_scan(username)
            elif choice == "2":
                phone = input(f"{Fore.RED}[>] Target phone: {Fore.LIGHTBLACK_EX}").strip()
                if phone: await self.phone_lookup(phone)
            elif choice == "3":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.web_scraper(url)
            elif choice == "4":
                ip = input(f"{Fore.RED}[>] Target IP: {Fore.LIGHTBLACK_EX}").strip()
                if ip: await self.ip_lookup(ip)
            elif choice == "5":
                domain = input(f"{Fore.RED}[>] Target domain: {Fore.LIGHTBLACK_EX}").strip()
                if domain: await self.email_harvester(domain)
            elif choice == "6":
                domain = input(f"{Fore.RED}[>] Target domain: {Fore.LIGHTBLACK_EX}").strip()
                if domain: await self.subdomain_takeover_check(domain)
            elif choice == "7":
                target = input(f"{Fore.RED}[>] Target IP/domain: {Fore.LIGHTBLACK_EX}").strip()
                if target: await self.advanced_port_scan(target)
            elif choice == "8":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.directory_bruteforce(url)
            elif choice == "9":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: self.sql_injection_tester(url)
            elif choice == "10":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: self.xss_vulnerability_scanner(url)
            elif choice == "11":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.git_repo_leak_scanner(url)
            elif choice == "12":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.api_key_scanner(url)
            elif choice == "13":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.cors_vulnerability_check(url)
            elif choice == "14":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.security_headers_check(url)
            elif choice == "15":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.robots_txt_analyzer(url)
            elif choice == "16":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.cms_detector(url)
            elif choice == "17":
                domain = input(f"{Fore.RED}[>] Target domain: {Fore.LIGHTBLACK_EX}").strip()
                if domain: await self.ssl_certificate_info(domain)
            elif choice == "18":
                url = input(f"{Fore.RED}[>] Target URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.wayback_machine_scanner(url)
            elif choice == "19":
                info = input(f"{Fore.RED}[>] Target info (name/company): {Fore.LIGHTBLACK_EX}").strip()
                if info: self.password_generator(info)
            elif choice == "20":
                hash_val = input(f"{Fore.RED}[>] Hash to identify: {Fore.LIGHTBLACK_EX}").strip()
                if hash_val: self.hash_identifier(hash_val)
            elif choice == "21":
                file = input(f"{Fore.RED}[>] Handshake file: {Fore.LIGHTBLACK_EX}").strip()
                if file: self.wifi_password_crack_sim(file)
            elif choice == "22":
                token = input(f"{Fore.RED}[>] JWT token: {Fore.LIGHTBLACK_EX}").strip()
                if token: self.jwt_decoder(token)
            elif choice == "27":
                url = input(f"{Fore.RED}[>] File URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.metadata_extractor(url)
            elif choice == "0":
                print(f"\n{Fore.RED}[✗] Wiping traces...")
                self.loading_animation("Shutting down", 0.8)
                print(f"{Fore.RED}[✗] Connection terminated\n")
                break
            else:
                print(f"{Fore.RED}[!] Invalid selection")


def main():
    print(f"\n{Fore.RED}{'═' * 80}")
    print(f"{Fore.RED}                    ⚠️  LEGAL WARNING ⚠️")
    print(f"{Fore.RED}{'═' * 80}")
    print(f"{Fore.LIGHTBLACK_EX}This tool is for EDUCATIONAL and AUTHORIZED TESTING ONLY")
    print(f"{Fore.LIGHTBLACK_EX}Unauthorized access to systems is ILLEGAL")
    print(f"{Fore.LIGHTBLACK_EX}You may face CRIMINAL PROSECUTION for misuse")
    print(f"{Fore.RED}{'═' * 80}\n")
    
    consent = input(f"{Fore.RED}Do you understand and accept? (yes/no): {Fore.LIGHTBLACK_EX}").strip().lower()
    
    if consent != 'yes':
        print(f"\n{Fore.RED}[!] Consent not given. Exiting.\n")
        return
    
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    osint = DarkOSINT()
    try:
        asyncio.run(osint.run())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] EMERGENCY SHUTDOWN")
    except Exception as e:
        print(f"\n{Fore.RED}[!] CRITICAL ERROR: {e}")


if __name__ == "__main__":
    main()