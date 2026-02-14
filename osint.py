"""
═══════════════════════════════════════════════════════════════════════════
                            LEGAL NOTICE
This tool is for AUTHORIZED security testing and educational purposes only.
Unauthorized access to computer systems is illegal under federal law.
Use only on systems you own or have explicit written permission to test.
═══════════════════════════════════════════════════════════════════════════
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
from urllib.parse import urlparse, parse_qs, quote
import base64
import binascii
import string

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

class PentestFramework:
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
                {"site": "Snapchat", "url": "snapchat.com/add/{}", "err": "404"},
                {"site": "Pinterest", "url": "pinterest.com/{}", "err": "404"},
                {"site": "Telegram", "url": "t.me/{}", "err": "If you have"},
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
                "admin", "root", "toor", "pass", "test", "guest", "welcome",
                "login", "changeme", "password123", "Password1", "admin123"
            ]
            with open(self.wordlist_path, 'w') as f:
                f.write('\n'.join(common_passwords))

    def loading_animation(self, text="Processing", duration=1.0):
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f"\r{Fore.RED}{chars[i % len(chars)]} {text}...", end='', flush=True)
            time.sleep(0.08)
            i += 1
        print(f"\r{Fore.RED}✓ {text}{' ' * 20}")

    def print_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        banner = f"""{Fore.RED}{Style.BRIGHT}
                                    ★
                                   ║█║
                                  ╱   ╲
                                 ║ ☠ ☠ ║
                                ╱  ▼ ▼  ╲
                               ║   ███   ║
                              ╱    ███    ╲
                             ║  ▓▓▓█▓▓▓  ║
                            ╱   ▓▓███▓▓   ╲
                           ║    ▓█████▓    ║
                          ╱      █████      ╲
                         ║       █████       ║
                        ╱   ╱╲   █████   ╱╲   ╲
                       ║   ║ ║  ███████  ║ ║   ║
                           ║ ║ ▓███████▓ ║ ║
                           ╲_║_▓▓█████▓▓_║_╱
                              ▓▓▓▓███▓▓▓▓
                               ▓▓▓███▓▓▓
                                ▓▓███▓▓
                                 ▓███▓
                                  ███
{Fore.LIGHTBLACK_EX}        ════════════════════════════════════════════════════════
{Fore.RED}                    PENETRATION TESTING FRAMEWORK
{Fore.LIGHTBLACK_EX}        ════════════════════════════════════════════════════════
{Fore.RED}                           v2.5 | 45+ Tools
{Fore.LIGHTBLACK_EX}        ════════════════════════════════════════════════════════
{Fore.RED}"""
        print(banner)
        print(f"{Fore.LIGHTBLACK_EX}          Developed by: kapa | Contact: up2k")
        print(f"{Fore.RED}          For authorized security testing only")
        print(f"{Fore.LIGHTBLACK_EX}{'═' * 80}\n")

    def save_report(self, target, data, category):
        clean_target = re.sub(r'[^\w\s-]', '', str(target)).strip().replace(' ', '_')
        filename = f"report_{category}_{clean_target}_{datetime.date.today()}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"\n{Fore.RED}[+] Report saved: {Fore.LIGHTBLACK_EX}{filename}")

    async def check_platform(self, client, site_data, username):
        url = f"https://{site_data['url'].format(username)}"
        async with self.limit:
            try:
                resp = await client.get(url, timeout=8.0, follow_redirects=True)
                if resp.status_code == 200:
                    if site_data['err'] == "404" or site_data['err'].lower() not in resp.text.lower():
                        print(f"{Fore.RED}[+] {site_data['site']:12} → {Fore.LIGHTBLACK_EX}{url}")
                        return {"site": site_data['site'], "url": url}
                    else:
                        print(f"{Fore.LIGHTBLACK_EX}[-] {site_data['site']:12} → Not found")
                else:
                    print(f"{Fore.LIGHTBLACK_EX}[-] {site_data['site']:12} → Not found")
            except:
                print(f"{Fore.LIGHTBLACK_EX}[-] {site_data['site']:12} → Error")
        return None

    async def username_scan(self, username):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Username Intelligence: {Fore.LIGHTBLACK_EX}{username}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Scanning platforms", 1.0)
        self.ensure_json_exists()
        
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                db = json.load(f)
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
            return

        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            tasks = [self.check_platform(client, s, username) for s in db.get('Social', [])]
            results = await asyncio.gather(*tasks)
            found = [r for r in results if r]
        
        print(f"\n{Fore.RED}[+] Found {len(found)} accounts")
        if found:
            self.save_report(username, found, "username")
        print(f"{Fore.RED}{'═' * 80}\n")

    async def phone_lookup(self, phone):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Phone Analysis: {Fore.LIGHTBLACK_EX}{phone}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Querying databases", 1.2)
        
        try:
            parsed_num = phonenumbers.parse(phone, None)
            if not phonenumbers.is_valid_number(parsed_num):
                print(f"{Fore.RED}[!] Invalid format")
                return

            country = geocoder.description_for_number(parsed_num, "en")
            provider = carrier.name_for_number(parsed_num, "en")
            zones = timezone.time_zones_for_number(parsed_num)
            fmt_e164 = phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.E164)

            print(f"\n{Fore.RED}[+] Results:\n")
            print(f"  {Fore.RED}├─ Country:  {Fore.LIGHTBLACK_EX}{country}")
            print(f"  {Fore.RED}├─ Carrier:  {Fore.LIGHTBLACK_EX}{provider or 'Unknown'}")
            print(f"  {Fore.RED}├─ Timezone: {Fore.LIGHTBLACK_EX}{', '.join(zones)}")
            print(f"  {Fore.RED}└─ E164:     {Fore.LIGHTBLACK_EX}{fmt_e164}")

            self.save_report(fmt_e164, {"country": country, "carrier": provider, "zones": zones}, "phone")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def web_scraper(self, target_url):
        if not target_url.startswith("http"):
            target_url = "https://" + target_url
            
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Web Scraping: {Fore.LIGHTBLACK_EX}{target_url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Extracting data", 1.0)
        
        async with httpx.AsyncClient(headers=self.get_headers(), follow_redirects=True) as client:
            try:
                resp = await client.get(target_url, timeout=15.0)
                
                emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resp.text)))
                socials = list(set(re.findall(r'https?://(?:www\.)?(?:twitter\.com|facebook\.com|instagram\.com|github\.com|tiktok\.com|youtube\.com)/[a-zA-Z0-9_.-]+', resp.text)))
                
                print(f"\n{Fore.RED}[+] Extracted data:\n")
                print(f"  {Fore.RED}├─ Emails:  {Fore.LIGHTBLACK_EX}{len(emails)}")
                if emails:
                    for i, email in enumerate(emails[:10], 1):
                        print(f"  {Fore.LIGHTBLACK_EX}│  {i}. {email}")
                
                print(f"  {Fore.RED}└─ Socials: {Fore.LIGHTBLACK_EX}{len(socials)}")
                if socials:
                    for i, social in enumerate(socials[:10], 1):
                        print(f"     {Fore.LIGHTBLACK_EX}{i}. {social}")
                
                self.save_report(target_url.replace('https://', '').replace('http://', ''), 
                               {"emails": emails, "socials": socials}, "scrape")
                
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def ip_lookup(self, ip_address):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] IP Geolocation: {Fore.LIGHTBLACK_EX}{ip_address}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Geolocating", 1.5)
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            try:
                resp = await client.get(f"http://ip-api.com/json/{ip_address}", timeout=10.0)
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get('status') == 'success':
                        print(f"\n{Fore.RED}[+] Location data:\n")
                        print(f"  {Fore.RED}├─ IP:       {Fore.LIGHTBLACK_EX}{data.get('query')}")
                        print(f"  {Fore.RED}├─ Country:  {Fore.LIGHTBLACK_EX}{data.get('country')} ({data.get('countryCode')})")
                        print(f"  {Fore.RED}├─ City:     {Fore.LIGHTBLACK_EX}{data.get('city')}")
                        print(f"  {Fore.RED}├─ Lat/Lon:  {Fore.LIGHTBLACK_EX}{data.get('lat')}, {data.get('lon')}")
                        print(f"  {Fore.RED}├─ ISP:      {Fore.LIGHTBLACK_EX}{data.get('isp')}")
                        print(f"  {Fore.RED}└─ ASN:      {Fore.LIGHTBLACK_EX}{data.get('as')}")
                        self.save_report(ip_address, data, "ip")
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def port_scan(self, target):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Port Scanning: {Fore.LIGHTBLACK_EX}{target}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        try:
            ip = socket.gethostbyname(target)
        except:
            ip = target
        
        ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 1433: "MSSQL", 3306: "MySQL", 3389: "RDP",
            5432: "PostgreSQL", 5900: "VNC", 6379: "Redis", 8080: "HTTP-Proxy",
            8443: "HTTPS-Alt", 27017: "MongoDB", 5000: "Docker"
        }
        
        self.loading_animation("Scanning ports", 1.5)
        
        open_ports = []
        
        for port, service in ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                print(f"{Fore.RED}[+] Port {port:5} ({service:15}) → {Fore.LIGHTBLACK_EX}Open")
                open_ports.append({"port": port, "service": service})
            sock.close()
        
        print(f"\n{Fore.RED}[+] {len(open_ports)} open ports found")
        if open_ports:
            self.save_report(target, {"ip": ip, "open_ports": open_ports}, "portscan")
        print(f"{Fore.RED}{'═' * 80}\n")

    async def directory_enum(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Directory Enumeration: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        directories = [
            "admin", "login", "dashboard", "wp-admin", "phpmyadmin",
            "backup", "db", "config", "api", "dev", "test", "staging",
            ".git", ".env", "uploads", "files", "private", "internal",
            "assets", "static", "downloads", "logs", "tmp"
        ]
        
        self.loading_animation("Enumerating paths", 1.5)
        
        found = []
        
        async with httpx.AsyncClient(headers=self.get_headers(), follow_redirects=False) as client:
            for directory in directories:
                test_url = f"{url}/{directory}"
                try:
                    resp = await client.get(test_url, timeout=3.0)
                    if resp.status_code in [200, 301, 302, 401, 403]:
                        print(f"{Fore.RED}[{resp.status_code}] {test_url}")
                        if resp.status_code in [200, 301, 302]:
                            found.append({"path": test_url, "status": resp.status_code})
                except:
                    pass
        
        print(f"\n{Fore.RED}[+] {len(found)} accessible paths found")
        if found:
            self.save_report(url, found, "direnum")
        print(f"{Fore.RED}{'═' * 80}\n")

    async def subdomain_enum(self, domain):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Subdomain Enumeration: {Fore.LIGHTBLACK_EX}{domain}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        if domain.startswith('http://') or domain.startswith('https://'):
            domain = urlparse(domain).netloc
        
        subdomains = [
            'www', 'mail', 'ftp', 'admin', 'test', 'dev', 'staging', 'api',
            'blog', 'shop', 'forum', 'support', 'help', 'docs', 'portal',
            'cdn', 'images', 'static', 'assets', 'vpn', 'remote', 'git'
        ]
        
        self.loading_animation("Resolving subdomains", 1.0)
        
        found = []
        
        for sub in subdomains:
            full = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(full)
                print(f"{Fore.RED}[+] {full:30} → {Fore.LIGHTBLACK_EX}{ip}")
                found.append({"subdomain": full, "ip": ip})
            except socket.gaierror:
                pass
        
        print(f"\n{Fore.RED}[+] {len(found)} subdomains found")
        if found:
            self.save_report(domain, {"subdomains": found}, "subdomain")
        print(f"{Fore.RED}{'═' * 80}\n")

    async def header_analysis(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] HTTP Header Analysis: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Analyzing headers", 1.0)
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            try:
                resp = await client.get(url, timeout=10.0)
                
                print(f"\n{Fore.RED}[+] Headers:\n")
                print(f"  {Fore.RED}├─ Status: {Fore.LIGHTBLACK_EX}{resp.status_code}")
                
                important = ['server', 'x-powered-by', 'content-type', 'x-frame-options', 
                            'content-security-policy', 'strict-transport-security']
                
                for key, value in resp.headers.items():
                    if key.lower() in important:
                        print(f"  {Fore.RED}├─ {key}: {Fore.LIGHTBLACK_EX}{value}")
                
                # Security check
                print(f"\n{Fore.RED}[*] Security assessment:")
                if 'x-frame-options' not in [h.lower() for h in resp.headers.keys()]:
                    print(f"  {Fore.RED}[!] Missing X-Frame-Options")
                if 'content-security-policy' not in [h.lower() for h in resp.headers.keys()]:
                    print(f"  {Fore.RED}[!] Missing CSP")
                
                self.save_report(url, dict(resp.headers), "headers")
                
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def git_exposure_check(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Git Exposure Check: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        paths = [".git/config", ".git/HEAD", ".git/index", ".git/logs/HEAD"]
        
        self.loading_animation("Checking for .git", 1.5)
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            found = []
            for path in paths:
                test_url = f"{url}/{path}"
                try:
                    resp = await client.get(test_url, timeout=3.0)
                    if resp.status_code == 200:
                        print(f"{Fore.RED}[!] Exposed: {test_url}")
                        found.append(test_url)
                except:
                    pass
            
            if found:
                print(f"\n{Fore.RED}[!] .git repository exposed - source code leak")
            else:
                print(f"\n{Fore.LIGHTBLACK_EX}[+] No .git exposure detected")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def robots_txt_check(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Robots.txt Analysis: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Fetching robots.txt", 1.0)
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            try:
                resp = await client.get(f"{url}/robots.txt", timeout=5.0)
                
                if resp.status_code == 200:
                    disallows = re.findall(r'Disallow:\s*(.+)', resp.text)
                    
                    if disallows:
                        print(f"\n{Fore.RED}[+] Restricted paths ({len(disallows)}):\n")
                        for i, path in enumerate(disallows[:20], 1):
                            print(f"  {Fore.LIGHTBLACK_EX}{i}. {path.strip()}")
                        
                        self.save_report(url, {"paths": disallows}, "robots")
                else:
                    print(f"{Fore.LIGHTBLACK_EX}[i] robots.txt not found")
                    
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    async def cms_detection(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] CMS Detection: {Fore.LIGHTBLACK_EX}{url}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        cms_sigs = {
            "WordPress": ["/wp-content/", "/wp-includes/"],
            "Joomla": ["/administrator/", "com_content"],
            "Drupal": ["/sites/default/", "Drupal.settings"],
            "Magento": ["/skin/frontend/"],
            "Shopify": ["cdn.shopify.com"]
        }
        
        self.loading_animation("Fingerprinting", 1.5)
        
        async with httpx.AsyncClient(headers=self.get_headers()) as client:
            try:
                resp = await client.get(url, timeout=10.0)
                
                print(f"\n{Fore.RED}[+] Detection results:\n")
                
                detected = []
                for cms, sigs in cms_sigs.items():
                    for sig in sigs:
                        if sig in resp.text:
                            print(f"  {Fore.RED}[+] Detected: {Fore.LIGHTBLACK_EX}{cms}")
                            detected.append(cms)
                            break
                
                if not detected:
                    print(f"  {Fore.LIGHTBLACK_EX}[i] CMS not identified")
                
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    def hash_crack_md5(self, hash_value):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] MD5 Hash Crack: {Fore.LIGHTBLACK_EX}{hash_value}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.ensure_wordlist_exists()
        self.loading_animation("Loading wordlist", 0.8)
        
        try:
            with open(self.wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                wordlist = [line.strip() for line in f if line.strip()]
            
            start_time = time.time()
            
            for i, password in enumerate(wordlist, 1):
                hashed = hashlib.md5(password.encode()).hexdigest()
                
                if i % 10 == 0:
                    print(f"\r{Fore.RED}[*] Testing: {i}/{len(wordlist)}", end='', flush=True)
                
                if hashed.lower() == hash_value.lower():
                    elapsed = time.time() - start_time
                    print(f"\n\n{Fore.RED}[+] Password found: {Fore.LIGHTBLACK_EX}{password}")
                    print(f"{Fore.RED}[+] Time: {elapsed:.2f}s\n")
                    return
            
            print(f"\n\n{Fore.RED}[!] Password not in wordlist")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    def hash_crack_sha1(self, hash_value):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] SHA1 Hash Crack: {Fore.LIGHTBLACK_EX}{hash_value}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.ensure_wordlist_exists()
        self.loading_animation("Loading wordlist", 0.8)
        
        try:
            with open(self.wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                wordlist = [line.strip() for line in f if line.strip()]
            
            start_time = time.time()
            
            for i, password in enumerate(wordlist, 1):
                hashed = hashlib.sha1(password.encode()).hexdigest()
                
                if i % 10 == 0:
                    print(f"\r{Fore.RED}[*] Testing: {i}/{len(wordlist)}", end='', flush=True)
                
                if hashed.lower() == hash_value.lower():
                    elapsed = time.time() - start_time
                    print(f"\n\n{Fore.RED}[+] Password found: {Fore.LIGHTBLACK_EX}{password}")
                    print(f"{Fore.RED}[+] Time: {elapsed:.2f}s\n")
                    return
            
            print(f"\n\n{Fore.RED}[!] Password not in wordlist")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    def hash_identifier(self, hash_value):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Hash Identification")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        length = len(hash_value)
        
        print(f"{Fore.RED}[+] Analysis:\n")
        print(f"  {Fore.RED}├─ Length: {Fore.LIGHTBLACK_EX}{length}")
        
        if length == 32:
            print(f"  {Fore.RED}└─ Type:   {Fore.LIGHTBLACK_EX}MD5")
        elif length == 40:
            print(f"  {Fore.RED}└─ Type:   {Fore.LIGHTBLACK_EX}SHA-1")
        elif length == 64:
            print(f"  {Fore.RED}└─ Type:   {Fore.LIGHTBLACK_EX}SHA-256")
        elif length == 128:
            print(f"  {Fore.RED}└─ Type:   {Fore.LIGHTBLACK_EX}SHA-512")
        else:
            print(f"  {Fore.RED}└─ Type:   {Fore.LIGHTBLACK_EX}Unknown")
        
        print(f"\n{Fore.RED}{'═' * 80}\n")

    def base64_encode(self, text):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Base64 Encoding")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        result = base64.b64encode(text.encode()).decode()
        print(f"{Fore.RED}[+] Result: {Fore.LIGHTBLACK_EX}{result}\n")
        print(f"{Fore.RED}{'═' * 80}\n")

    def base64_decode(self, text):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Base64 Decoding")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        try:
            result = base64.b64decode(text).decode()
            print(f"{Fore.RED}[+] Result: {Fore.LIGHTBLACK_EX}{result}\n")
        except:
            print(f"{Fore.RED}[!] Invalid base64\n")
        
        print(f"{Fore.RED}{'═' * 80}\n")

    def hash_generator(self, text):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Hash Generation")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        print(f"{Fore.RED}[+] Hashes:\n")
        print(f"  {Fore.RED}├─ MD5:    {Fore.LIGHTBLACK_EX}{hashlib.md5(text.encode()).hexdigest()}")
        print(f"  {Fore.RED}├─ SHA1:   {Fore.LIGHTBLACK_EX}{hashlib.sha1(text.encode()).hexdigest()}")
        print(f"  {Fore.RED}├─ SHA256: {Fore.LIGHTBLACK_EX}{hashlib.sha256(text.encode()).hexdigest()}")
        print(f"  {Fore.RED}└─ Base64: {Fore.LIGHTBLACK_EX}{base64.b64encode(text.encode()).decode()}\n")
        
        print(f"{Fore.RED}{'═' * 80}\n")

    def jwt_decode(self, token):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] JWT Decoder")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        try:
            parts = token.split('.')
            
            if len(parts) != 3:
                print(f"{Fore.RED}[!] Invalid JWT format\n")
                return
            
            header = json.loads(base64.urlsafe_b64decode(parts[0] + '=='))
            payload = json.loads(base64.urlsafe_b64decode(parts[1] + '=='))
            
            print(f"{Fore.RED}[+] Header:")
            for key, value in header.items():
                print(f"  {Fore.LIGHTBLACK_EX}{key}: {value}")
            
            print(f"\n{Fore.RED}[+] Payload:")
            for key, value in payload.items():
                print(f"  {Fore.LIGHTBLACK_EX}{key}: {value}\n")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Decode error: {str(e)}\n")
        
        print(f"{Fore.RED}{'═' * 80}\n")

    async def dns_lookup(self, domain):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] DNS Lookup: {Fore.LIGHTBLACK_EX}{domain}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        if domain.startswith('http'):
            domain = urlparse(domain).netloc
        
        self.loading_animation("Resolving DNS", 1.0)
        
        try:
            ip = socket.gethostbyname(domain)
            print(f"\n{Fore.RED}[+] A Record: {Fore.LIGHTBLACK_EX}{ip}\n")
        except:
            print(f"\n{Fore.RED}[!] Resolution failed\n")
        
        print(f"{Fore.RED}{'═' * 80}\n")

    async def reverse_ip(self, ip):
        print(f"\n{Fore.RED}{'═' * 80}")
        print(f"{Fore.RED}[*] Reverse IP Lookup: {Fore.LIGHTBLACK_EX}{ip}")
        print(f"{Fore.RED}{'═' * 80}\n")
        
        self.loading_animation("Performing lookup", 1.0)
        
        try:
            hostname = socket.gethostbyaddr(ip)
            print(f"\n{Fore.RED}[+] Hostname: {Fore.LIGHTBLACK_EX}{hostname[0]}\n")
        except:
            print(f"\n{Fore.RED}[!] No PTR record found\n")
        
        print(f"{Fore.RED}{'═' * 80}\n")

    def show_menu(self):
        print(f"{Fore.RED}╔{'═' * 78}╗")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}RECONNAISSANCE{' ' * 61}{Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}1.  Username Scan      2.  Phone Lookup       3.  Web Scraper    {Fore.RED}║")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}4.  IP Geolocation     5.  DNS Lookup         6.  Reverse IP     {Fore.RED}║")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}7.  Subdomain Enum     8.  Port Scanner       9.  CMS Detection  {Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}WEB TESTING{' ' * 64}{Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}10. Directory Enum     11. Header Analysis    12. Git Check      {Fore.RED}║")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}13. Robots.txt Check                                            {Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}CRYPTO & ENCODING{' ' * 58}{Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}14. Hash Identifier    15. MD5 Crack          16. SHA1 Crack     {Fore.RED}║")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}17. Hash Generator     18. Base64 Encode      19. Base64 Decode  {Fore.RED}║")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}20. JWT Decoder                                                 {Fore.RED}║")
        print(f"{Fore.RED}╠{'═' * 78}╣")
        print(f"{Fore.RED}║ {Fore.LIGHTBLACK_EX}0.  Exit{' ' * 67}{Fore.RED}║")
        print(f"{Fore.RED}╚{'═' * 78}╝")

    async def run(self):
        self.print_banner()
        
        while True:
            self.show_menu()
            choice = input(f"\n{Fore.RED}root@framework {Fore.LIGHTBLACK_EX}» ").strip()
            
            if choice == "1":
                u = input(f"{Fore.RED}Username: {Fore.LIGHTBLACK_EX}").strip()
                if u: await self.username_scan(u)
            elif choice == "2":
                p = input(f"{Fore.RED}Phone: {Fore.LIGHTBLACK_EX}").strip()
                if p: await self.phone_lookup(p)
            elif choice == "3":
                url = input(f"{Fore.RED}URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.web_scraper(url)
            elif choice == "4":
                ip = input(f"{Fore.RED}IP: {Fore.LIGHTBLACK_EX}").strip()
                if ip: await self.ip_lookup(ip)
            elif choice == "5":
                d = input(f"{Fore.RED}Domain: {Fore.LIGHTBLACK_EX}").strip()
                if d: await self.dns_lookup(d)
            elif choice == "6":
                ip = input(f"{Fore.RED}IP: {Fore.LIGHTBLACK_EX}").strip()
                if ip: await self.reverse_ip(ip)
            elif choice == "7":
                d = input(f"{Fore.RED}Domain: {Fore.LIGHTBLACK_EX}").strip()
                if d: await self.subdomain_enum(d)
            elif choice == "8":
                t = input(f"{Fore.RED}Target: {Fore.LIGHTBLACK_EX}").strip()
                if t: await self.port_scan(t)
            elif choice == "9":
                url = input(f"{Fore.RED}URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.cms_detection(url)
            elif choice == "10":
                url = input(f"{Fore.RED}URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.directory_enum(url)
            elif choice == "11":
                url = input(f"{Fore.RED}URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.header_analysis(url)
            elif choice == "12":
                url = input(f"{Fore.RED}URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.git_exposure_check(url)
            elif choice == "13":
                url = input(f"{Fore.RED}URL: {Fore.LIGHTBLACK_EX}").strip()
                if url: await self.robots_txt_check(url)
            elif choice == "14":
                h = input(f"{Fore.RED}Hash: {Fore.LIGHTBLACK_EX}").strip()
                if h: self.hash_identifier(h)
            elif choice == "15":
                h = input(f"{Fore.RED}MD5: {Fore.LIGHTBLACK_EX}").strip()
                if h: self.hash_crack_md5(h)
            elif choice == "16":
                h = input(f"{Fore.RED}SHA1: {Fore.LIGHTBLACK_EX}").strip()
                if h: self.hash_crack_sha1(h)
            elif choice == "17":
                t = input(f"{Fore.RED}Text: {Fore.LIGHTBLACK_EX}").strip()
                if t: self.hash_generator(t)
            elif choice == "18":
                t = input(f"{Fore.RED}Text: {Fore.LIGHTBLACK_EX}").strip()
                if t: self.base64_encode(t)
            elif choice == "19":
                t = input(f"{Fore.RED}Base64: {Fore.LIGHTBLACK_EX}").strip()
                if t: self.base64_decode(t)
            elif choice == "20":
                t = input(f"{Fore.RED}JWT: {Fore.LIGHTBLACK_EX}").strip()
                if t: self.jwt_decode(t)
            elif choice == "0":
                print(f"\n{Fore.RED}[+] Exiting...\n")
                break
            else:
                print(f"{Fore.RED}[!] Invalid option\n")


def main():
    print(f"\n{Fore.RED}{'═' * 80}")
    print(f"{Fore.RED}                          LEGAL NOTICE")
    print(f"{Fore.RED}{'═' * 80}")
    print(f"{Fore.LIGHTBLACK_EX}For authorized security testing only")
    print(f"{Fore.LIGHTBLACK_EX}Unauthorized access is illegal")
    print(f"{Fore.RED}{'═' * 80}\n")
    
    confirm = input(f"{Fore.RED}Continue? (yes/no): {Fore.LIGHTBLACK_EX}").strip().lower()
    
    if confirm != 'yes':
        print(f"\n{Fore.RED}[!] Exiting\n")
        return
    
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    framework = PentestFramework()
    try:
        asyncio.run(framework.run())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Interrupted\n")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {e}\n")


if __name__ == "__main__":
    main()
