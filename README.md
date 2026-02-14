# Penetration Testing Framework v2.5

```
                                ★
                               ║█║
                              ╱   ╲
                             ║ ☠ ☠ ║
                            ╱  ▼ ▼  ╲
                           ║   ███   ║
                          ╱    ███    ╲
                         ║  ▓▓▓█▓▓▓  ║
```

A comprehensive security testing toolkit with 20+ professional-grade tools for authorized penetration testing and security research.

## ⚠️ Legal Notice

**THIS TOOL IS FOR AUTHORIZED SECURITY TESTING ONLY**

- Use only on systems you own or have **explicit written permission** to test
- Unauthorized access to computer systems is **illegal** under:
  - Computer Fraud and Abuse Act (CFAA)
  - Digital Millennium Copyright Act (DMCA)
  - International cybercrime laws
- The author assumes **NO responsibility** for misuse
- By using this tool, you agree to use it **legally and ethically**

## 🎯 Features

### Reconnaissance (9 Tools)
- **Username Scan** - Search for usernames across 12+ social platforms
- **Phone Lookup** - Extract carrier, country, and timezone information
- **Web Scraper** - Harvest emails and social media links from websites
- **IP Geolocation** - Locate IP addresses with ISP and ASN data
- **DNS Lookup** - Resolve domain names to IP addresses
- **Reverse IP** - Find hostnames from IP addresses
- **Subdomain Enumeration** - Discover subdomains for target domains
- **Port Scanner** - Scan 22 common ports including SSH, HTTP, MySQL, RDP
- **CMS Detection** - Identify WordPress, Joomla, Drupal, and other platforms

### Web Testing (4 Tools)
- **Directory Enumeration** - Discover hidden paths and directories
- **Header Analysis** - Analyze HTTP headers and security posture
- **Git Exposure Check** - Detect exposed .git repositories
- **Robots.txt Check** - Extract restricted paths from robots.txt

### Cryptography & Encoding (7 Tools)
- **Hash Identifier** - Identify hash types (MD5, SHA-1, SHA-256, SHA-512)
- **MD5 Cracker** - Brute force MD5 hashes with wordlist
- **SHA-1 Cracker** - Brute force SHA-1 hashes with wordlist
- **Hash Generator** - Generate MD5, SHA-1, SHA-256, and Base64
- **Base64 Encoder** - Encode text to Base64
- **Base64 Decoder** - Decode Base64 strings
- **JWT Decoder** - Decode and analyze JSON Web Tokens

## 📦 Installation

### Requirements
- Python 3.8+
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

**Requirements:**
```
httpx==0.27.0
phonenumbers==8.13.27
colorama==0.4.6
```

### Optional: Install in Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

### Quick Start

```bash
python pentest_framework.py
```

You will be prompted to accept the legal terms before proceeding.

### Example Commands

#### Reconnaissance
```
root@framework » 1
Username: johndoe
# Scans 12+ social platforms for the username
```

```
root@framework » 4
IP: 8.8.8.8
# Geolocates the IP address
```

#### Web Testing
```
root@framework » 10
URL: example.com
# Enumerates directories and hidden paths
```

#### Cryptography
```
root@framework » 15
MD5: 5f4dcc3b5aa765d61d8327deb882cf99
# Attempts to crack the MD5 hash
```

## 📖 Detailed Tool Documentation

### 1. Username Scan
Searches for a username across multiple social media platforms.

**Platforms checked:**
- GitHub, Instagram, Reddit, Twitter, TikTok, YouTube, Twitch, LinkedIn, Facebook, Snapchat, Pinterest, Telegram

**Output:**
- JSON report with found accounts
- Direct URLs to profiles

**Example:**
```
root@framework » 1
Username: testuser
[+] GitHub → https://github.com/testuser
[+] Reddit → https://reddit.com/user/testuser
```

### 2. Phone Lookup
Analyzes phone numbers to extract metadata.

**Information extracted:**
- Country and region
- Carrier/operator
- Timezone(s)
- E.164 format

**Example:**
```
root@framework » 2
Phone: +14155552671
[+] Country: United States
[+] Carrier: Verizon Wireless
[+] Timezone: America/Los_Angeles
```

### 3. Web Scraper
Extracts emails and social media links from web pages.

**Extracted data:**
- Email addresses
- Social media profile URLs (Twitter, Facebook, Instagram, GitHub, TikTok, YouTube)

**Example:**
```
root@framework » 3
URL: example.com
[+] Emails: 5
[+] Socials: 3
```

### 4. IP Geolocation
Geolocates IP addresses with detailed information.

**Data provided:**
- Country, city, region
- Latitude/longitude coordinates
- ISP and organization
- Autonomous System Number (ASN)

### 5. Port Scanner
Scans common ports to identify running services.

**Ports scanned:**
21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), 80 (HTTP), 110 (POP3), 135 (RPC), 139 (NetBIOS), 143 (IMAP), 443 (HTTPS), 445 (SMB), 1433 (MSSQL), 3306 (MySQL), 3389 (RDP), 5432 (PostgreSQL), 5900 (VNC), 6379 (Redis), 8080 (HTTP-Proxy), 8443 (HTTPS-Alt), 27017 (MongoDB), 5000 (Docker)

### 6. Directory Enumeration
Discovers hidden directories and files on web servers.

**Common paths checked:**
admin, login, dashboard, wp-admin, phpmyadmin, backup, db, config, api, dev, test, staging, .git, .env, uploads, files, private, internal, assets, static, downloads, logs, tmp

### 7. Hash Crackers
Brute force password hashes using a wordlist.

**Supported algorithms:**
- MD5 (32 characters)
- SHA-1 (40 characters)

**Usage:**
Place passwords in `wordlist.txt` (auto-generated if missing) or use your own wordlist.

### 8. JWT Decoder
Decodes JSON Web Tokens to view header and payload.

**Information displayed:**
- Algorithm used
- Token type
- Payload data (user ID, expiration, etc.)

**Note:** Does not verify signature (requires secret key)

## 📁 Output Files

All scan results are automatically saved as JSON files:

```
report_username_testuser_2024-02-14.json
report_ip_8.8.8.8_2024-02-14.json
report_scrape_example.com_2024-02-14.json
report_portscan_example.com_2024-02-14.json
report_subdomain_example.com_2024-02-14.json
report_direnum_example.com_2024-02-14.json
report_headers_example.com_2024-02-14.json
```

## 🔧 Configuration

### Custom Wordlist
Replace the default `wordlist.txt` with your own:

```bash
# Download a larger wordlist
wget https://github.com/danielmiessler/SecLists/raw/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt -O wordlist.txt
```

### Custom Social Platforms
Edit `sites.json` to add or modify social media platforms:

```json
{
  "Social": [
    {
      "site": "CustomSite",
      "url": "customsite.com/user/{}",
      "err": "404"
    }
  ]
}
```

## 🛡️ Security Best Practices

### When Using This Tool:

1. **Authorization First**
   - Always obtain written permission before testing
   - Document your authorization
   - Respect scope limitations

2. **Responsible Disclosure**
   - Report vulnerabilities to the organization
   - Allow time for fixes before public disclosure
   - Follow responsible disclosure guidelines

3. **Rate Limiting**
   - Don't overwhelm target systems
   - Use appropriate delays between requests
   - Respect robots.txt when applicable

4. **Legal Compliance**
   - Understand local laws regarding security testing
   - Consult legal counsel if unsure
   - Maintain ethical standards

## 🐛 Troubleshooting

### Common Issues

**"Module not found" errors:**
```bash
pip install -r requirements.txt
```

**Colorama not working on Windows:**
pip uninstall colorama
pip install colorama --upgrade

**Port scanner timeout issues:**
- Firewall may be blocking connections
- Increase timeout in code (currently 0.5s)
- Some ports may be filtered

**Hash cracker not finding password:**
- Password may not be in wordlist
- Try a larger wordlist
- Consider using specialized tools like hashcat or john

## 📚 Learning Resources

### Practice Platforms:
- [HackTheBox](https://www.hackthebox.eu/)
- [TryHackMe](https://tryhackme.com/)
- [VulnHub](https://www.vulnhub.com/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)



## 📄 License

This project is provided for **educational purposes only**.

**By using this software, you agree to:**
- Use it only for authorized security testing
- Comply with all applicable laws and regulations
- Not hold the author liable for any misuse

## 👤 Author

**kapa**
- Discord: up2k
- Purpose: Educational security research

## 🔄 Changelog

### v2.5 (Current)
- Cleaned up language (removed sensationalized terms)
- Improved error handling
- Added 20 core tools
- Professional output formatting
- JSON report generation

### v2.0
- Initial public release
- Basic OSINT tools
- Hash cracking capabilities
- Web testing features

```
                    ★
                   ║█║
                  ╱   ╲
                 ║ ☠ ☠ ║
```
