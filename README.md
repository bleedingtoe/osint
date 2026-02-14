##                                                                                   V2.5

⚠️Remember to update wordlist/add more common passwords. https://github.com/danielmiessler/SecLists/tree/master/Passwords⚠️
##
🎯Plans for the next version :
Credential stealer
Cookie logger
API for breach searches
Option to create a py file for IP stealing via discord webhook
##
A toolkit for authorized security research and penetration testing.

⚠️ Legal Notice
AUTHORIZED USE ONLY. Accessing systems without explicit permission is illegal (CFAA, DMCA, and international laws). The author is not responsible for misuse. Use this ethically.

🎯 Toolset
Reconnaissance
Username Scan: Check 12+ social platforms for a specific handle.

Phone Lookup: Extract carrier, region, and timezone data.

Web Scraper: Pull emails and social links from a URL.

IP/DNS: Geolocation, ISP data, DNS resolution, and Reverse IP.

Scanner: Discover subdomains and scan 22 common ports (SSH, SQL, RDP, etc.).

CMS Detection: Identify WordPress, Joomla, and Drupal.

Web Testing
Directory Brute: Search for hidden paths (/admin, .git, .env).

Analysis: Header security posture and robots.txt extraction.

Crypto & Encoding
Hash Tools: ID hash types and brute force MD5/SHA-1 via wordlist.

Utilities: Base64 encoding/decoding and JWT payload analysis.

📦 Setup
Requirements: Python 3.8+

Bash
pip install httpx phonenumbers colorama
python pentest_framework.py
🚀 Usage
Run the script and follow the menu prompts.

Examples:

IP Geo: Option 4 -> 8.8.8.8

Dir Enum: Option 10 -> example.com

MD5 Crack: Option 15 -> [hash] (Uses wordlist.txt)

📁 Output
Reports are auto-saved to JSON for later analysis:
report_username_testuser_2024-02-14.json
report_portscan_example.com_2024-02-14.json

🛡️ Best Practices
Scope: Stay within authorized boundaries.

Noise: Don't flood targets; use reasonable timeouts.

Disclosure: Report bugs responsibly to the affected organization.

Author: kapa (Discord: up2k)
License: Educational purposes only.
