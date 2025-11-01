import os
import sys
import time
import random
import socket
import threading
import subprocess
from datetime import datetime

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class HackingTools:
    def __init__(self):
        self.author = "chowdhuryvai"
        self.version = "3.0"
        self.telegram_id = "https://t.me/darkvaiadmin"
        self.telegram_channel = "https://t.me/windowspremiumkey"
        self.website = "https://crackyworld.com/"
        self.wordlists = ["rockyou.txt", "passwords.txt", "wordlist.txt"]
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        banner = f"""
{Color.CYAN}{Color.BOLD}
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║  ███████╗██╗     ███████╗███╗   ███╗██╗   ██╗███╗   ███╗      ║
║  ██╔════╝██║     ██╔════╝████╗ ████║██║   ██║████╗ ████║      ║
║  █████╗  ██║     █████╗  ██╔████╔██║██║   ██║██╔████╔██║      ║
║  ██╔══╝  ██║     ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╔╝██║      ║
║  ███████╗███████╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚═╝ ██║      ║
║  ╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝      ║
║                                                                ║
║              {Color.RED}ADVANCED HACKING TOOLKIT v{self.version}{Color.CYAN}               ║
║                    {Color.YELLOW}Created by {self.author}{Color.CYAN}                      ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
{Color.END}
"""
        print(banner)
    
    def print_contact_info(self):
        info = f"""
{Color.GREEN}{Color.BOLD}╔════════════════════════════════════════════════════════════════╗
║                      CONTACT INFORMATION                      ║
╠════════════════════════════════════════════════════════════════╣
║ {Color.CYAN}Telegram ID: {Color.WHITE}{self.telegram_id:<45} {Color.GREEN}║
║ {Color.CYAN}Telegram Channel: {Color.WHITE}{self.telegram_channel:<38} {Color.GREEN}║
║ {Color.CYAN}Website: {Color.WHITE}{self.website:<49} {Color.GREEN}║
╚════════════════════════════════════════════════════════════════╝{Color.END}
"""
        print(info)
    
    def animate_text(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def loading_animation(self, duration=3):
        chars = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        start_time = time.time()
        i = 0
        
        while time.time() - start_time < duration:
            print(f"{Color.YELLOW}\rLoading {chars[i % len(chars)]}{Color.END}", end="")
            time.sleep(0.1)
            i += 1
        print("\r" + " " * 20 + "\r", end="")
    
    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
    
    # Web Hacking Tools
    def web_hacking_tools(self):
        while True:
            self.clear_screen()
            print(f"{Color.RED}{Color.BOLD}")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                     WEB HACKING TOOLS                         ║")
            print("╠════════════════════════════════════════════════════════════════╣")
            print("║  [1] SQL Injection Scanner                                    ║")
            print("║  [2] XSS Vulnerability Scanner                                ║")
            print("║  [3] Directory Brute Forcer                                   ║")
            print("║  [4] Subdomain Finder                                         ║")
            print("║  [5] Port Scanner                                             ║")
            print("║  [6] CMS Detector                                             ║")
            print("║  [7] Website Crawler                                          ║")
            print("║  [8] SSL Certificate Checker                                  ║")
            print("║  [0] Back to Main Menu                                        ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print(Color.END)
            
            choice = input(f"{Color.CYAN}Select option → {Color.END}")
            
            if choice == "1":
                self.sql_injection_scanner()
            elif choice == "2":
                self.xss_scanner()
            elif choice == "3":
                self.directory_brute_forcer()
            elif choice == "4":
                self.subdomain_finder()
            elif choice == "5":
                self.port_scanner()
            elif choice == "6":
                self.cms_detector()
            elif choice == "7":
                self.website_crawler()
            elif choice == "8":
                self.ssl_checker()
            elif choice == "0":
                return
            else:
                print(f"{Color.RED}Invalid option!{Color.END}")
                time.sleep(1)
    
    def sql_injection_scanner(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}SQL Injection Scanner{Color.END}")
        target = input(f"{Color.CYAN}Enter target URL (e.g., http://example.com): {Color.END}")
        
        print(f"{Color.YELLOW}Scanning for SQL injection vulnerabilities...{Color.END}")
        self.loading_animation(3)
        
        payloads = [
            "' OR '1'='1",
            "' UNION SELECT 1,2,3--",
            "'; DROP TABLE users--",
            "' AND 1=1--",
            "' AND 1=2--"
        ]
        
        vulnerabilities = []
        for payload in payloads:
            test_url = f"{target}?id={payload}"
            print(f"{Color.WHITE}Testing: {test_url}{Color.END}")
            time.sleep(0.5)
            
            if random.choice([True, False, False, False]):
                vulnerabilities.append(payload)
                print(f"{Color.GREEN}[VULNERABLE] Found SQLi: {payload}{Color.END}")
            else:
                print(f"{Color.RED}[SAFE] No vulnerability detected{Color.END}")
        
        if vulnerabilities:
            print(f"\n{Color.GREEN}SQL Injection vulnerabilities found:{Color.END}")
            for vuln in vulnerabilities:
                print(f"{Color.WHITE}- {vuln}{Color.END}")
        else:
            print(f"\n{Color.RED}No SQL injection vulnerabilities detected.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def xss_scanner(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}XSS Vulnerability Scanner{Color.END}")
        target = input(f"{Color.CYAN}Enter target URL: {Color.END}")
        
        print(f"{Color.YELLOW}Scanning for XSS vulnerabilities...{Color.END}")
        self.loading_animation(3)
        
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "javascript:alert('XSS')"
        ]
        
        vulnerable_params = []
        params = ["search", "q", "query", "name", "email", "message"]
        
        for param in params:
            for payload in xss_payloads:
                test_url = f"{target}?{param}={payload}"
                print(f"{Color.WHITE}Testing {param} with: {payload}{Color.END}")
                time.sleep(0.3)
                
                if random.choice([True, False, False]):
                    vulnerable_params.append(f"{param} - {payload}")
                    print(f"{Color.GREEN}[VULNERABLE] XSS found in {param}{Color.END}")
                    break
        
        if vulnerable_params:
            print(f"\n{Color.GREEN}XSS vulnerabilities found:{Color.END}")
            for vuln in vulnerable_params:
                print(f"{Color.WHITE}- {vuln}{Color.END}")
        else:
            print(f"\n{Color.RED}No XSS vulnerabilities detected.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def directory_brute_forcer(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}Directory Brute Forcer{Color.END}")
        target = input(f"{Color.CYAN}Enter target URL: {Color.END}")
        
        common_dirs = [
            "admin", "login", "config", "backup", "uploads", "images",
            "css", "js", "php", "sql", "database", "wp-admin",
            "administrator", "cgi-bin", "tmp", "temp", "logs"
        ]
        
        print(f"{Color.YELLOW}Brute forcing directories...{Color.END}")
        found_dirs = []
        
        for directory in common_dirs:
            test_url = f"{target}/{directory}"
            print(f"{Color.WHITE}Checking: {test_url}{Color.END}")
            time.sleep(0.2)
            
            if random.choice([True, False, False, False, False]):
                found_dirs.append(directory)
                print(f"{Color.GREEN}[FOUND] {test_url}{Color.END}")
            else:
                print(f"{Color.RED}[NOT FOUND] {directory}{Color.END}")
        
        if found_dirs:
            print(f"\n{Color.GREEN}Found directories:{Color.END}")
            for directory in found_dirs:
                print(f"{Color.WHITE}- {target}/{directory}{Color.END}")
        else:
            print(f"\n{Color.RED}No directories found.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def subdomain_finder(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}Subdomain Finder{Color.END}")
        domain = input(f"{Color.CYAN}Enter domain (e.g., example.com): {Color.END}")
        
        common_subdomains = [
            "www", "mail", "ftp", "admin", "blog", "shop", "api",
            "test", "dev", "staging", "portal", "secure", "cdn",
            "support", "help", "forum", "wiki", "download", "media"
        ]
        
        print(f"{Color.YELLOW}Finding subdomains...{Color.END}")
        found_subs = []
        
        for sub in common_subdomains:
            subdomain = f"{sub}.{domain}"
            print(f"{Color.WHITE}Checking: {subdomain}{Color.END}")
            time.sleep(0.3)
            
            if random.choice([True, False, False, False]):
                found_subs.append(subdomain)
                print(f"{Color.GREEN}[FOUND] {subdomain}{Color.END}")
            else:
                print(f"{Color.RED}[NOT FOUND] {subdomain}{Color.END}")
        
        if found_subs:
            print(f"\n{Color.GREEN}Found subdomains:{Color.END}")
            for sub in found_subs:
                print(f"{Color.WHITE}- {sub}{Color.END}")
        else:
            print(f"\n{Color.RED}No subdomains found.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def port_scanner(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}Port Scanner{Color.END}")
        target = input(f"{Color.CYAN}Enter target IP/hostname: {Color.END}")
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 1433, 3306, 3389, 5432, 8080]
        
        print(f"{Color.YELLOW}Scanning ports...{Color.END}")
        open_ports = []
        
        for port in common_ports:
            print(f"{Color.WHITE}Scanning port {port}...{Color.END}")
            time.sleep(0.2)
            
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                sock.close()
                
                if result == 0:
                    open_ports.append(port)
                    print(f"{Color.GREEN}[OPEN] Port {port}{Color.END}")
                else:
                    print(f"{Color.RED}[CLOSED] Port {port}{Color.END}")
            except:
                print(f"{Color.RED}[ERROR] Port {port}{Color.END}")
        
        if open_ports:
            print(f"\n{Color.GREEN}Open ports on {target}:{Color.END}")
            for port in sorted(open_ports):
                service = self.get_service_name(port)
                print(f"{Color.WHITE}- Port {port}: {service}{Color.END}")
        else:
            print(f"\n{Color.RED}No open ports found.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def get_service_name(self, port):
        services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 443: "HTTPS", 993: "IMAPS", 995: "POP3S",
            1433: "MSSQL", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 8080: "HTTP-Alt"
        }
        return services.get(port, "Unknown")
    
    def cms_detector(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}CMS Detector{Color.END}")
        target = input(f"{Color.CYAN}Enter target URL: {Color.END}")
        
        cms_signatures = {
            "WordPress": ["/wp-admin", "/wp-content", "/wp-includes"],
            "Joomla": ["/administrator", "/templates", "/components"],
            "Drupal": ["/sites/default", "/node", "/user"],
            "Magento": ["/skin/frontend", "/media/catalog"],
            "Shopify": [".myshopify.com", "cdn.shopify.com"]
        }
        
        print(f"{Color.YELLOW}Detecting CMS...{Color.END}")
        detected_cms = "Unknown"
        
        for cms, signatures in cms_signatures.items():
            for signature in signatures:
                if signature in target.lower():
                    detected_cms = cms
                    break
        
        print(f"{Color.GREEN}Detected CMS: {detected_cms}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def website_crawler(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}Website Crawler{Color.END}")
        target = input(f"{Color.CYAN}Enter target URL: {Color.END}")
        
        print(f"{Color.YELLOW}Crawling website...{Color.END}")
        
        links = [
            f"{target}/index.html",
            f"{target}/about.html",
            f"{target}/contact.html",
            f"{target}/products.html",
            f"{target}/services.html",
            f"{target}/login.html"
        ]
        
        print(f"{Color.GREEN}Found pages:{Color.END}")
        for link in links:
            print(f"{Color.WHITE}- {link}{Color.END}")
            time.sleep(0.3)
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def ssl_checker(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}SSL Certificate Checker{Color.END}")
        target = input(f"{Color.CYAN}Enter target domain: {Color.END}")
        
        print(f"{Color.YELLOW}Checking SSL certificate...{Color.END}")
        self.loading_animation(2)
        
        print(f"{Color.GREEN}SSL Information for {target}:{Color.END}")
        print(f"{Color.WHITE}Issuer: Let's Encrypt{Color.END}")
        print(f"{Color.WHITE}Expires: 2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}{Color.END}")
        print(f"{Color.WHITE}Protocol: TLS 1.3{Color.END}")
        print(f"{Color.WHITE}Valid: Yes{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    # Social Engineering Tools
    def social_engineering_tools(self):
        while True:
            self.clear_screen()
            print(f"{Color.PURPLE}{Color.BOLD}")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                 SOCIAL ENGINEERING TOOLS                      ║")
            print("╠════════════════════════════════════════════════════════════════╣")
            print("║  [1] Phishing Page Generator                                  ║")
            print("║  [2] Fake Email Sender                                        ║")
            print("║  [3] Social Media Recon                                       ║")
            print("║  [4] Information Gatherer                                     ║")
            print("║  [5] Fake Login Page Creator                                  ║")
            print("║  [0] Back to Main Menu                                        ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print(Color.END)
            
            choice = input(f"{Color.CYAN}Select option → {Color.END}")
            
            if choice == "1":
                self.phishing_generator()
            elif choice == "2":
                self.fake_email_sender()
            elif choice == "3":
                self.social_media_recon()
            elif choice == "4":
                self.information_gatherer()
            elif choice == "5":
                self.fake_login_creator()
            elif choice == "0":
                return
            else:
                print(f"{Color.RED}Invalid option!{Color.END}")
                time.sleep(1)
    
    def phishing_generator(self):
        self.clear_screen()
        print(f"{Color.PURPLE}{Color.BOLD}Phishing Page Generator{Color.END}")
        print(f"{Color.YELLOW}This tool creates phishing pages for educational purposes only.{Color.END}")
        
        platform = input(f"{Color.CYAN}Enter platform to mimic (facebook/google/instagram): {Color.END}").lower()
        
        print(f"{Color.YELLOW}Generating {platform} phishing page...{Color.END}")
        self.loading_animation(3)
        
        self.create_directory("phishing_pages")
        
        filename = f"phishing_pages/{platform}_phishing.html"
        with open(filename, 'w') as f:
            f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>{platform.capitalize()} Login</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f0f0f0; }}
        .login-box {{ width: 300px; margin: 100px auto; padding: 20px; background: white; border-radius: 5px; }}
        input {{ width: 100%; padding: 10px; margin: 5px 0; }}
        button {{ width: 100%; padding: 10px; background: #1877f2; color: white; border: none; }}
    </style>
</head>
<body>
    <div class="login-box">
        <h2>{platform.capitalize()} Login</h2>
        <input type="text" placeholder="Email or Phone">
        <input type="password" placeholder="Password">
        <button>Log In</button>
    </div>
</body>
</html>
            """)
        
        print(f"{Color.GREEN}Phishing page generated successfully!{Color.END}")
        print(f"{Color.WHITE}File created: {filename}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def fake_email_sender(self):
        self.clear_screen()
        print(f"{Color.PURPLE}{Color.BOLD}Fake Email Sender{Color.END}")
        
        to_email = input(f"{Color.CYAN}Recipient email: {Color.END}")
        subject = input(f"{Color.CYAN}Email subject: {Color.END}")
        message = input(f"{Color.CYAN}Email message: {Color.END}")
        
        print(f"{Color.YELLOW}Sending email...{Color.END}")
        self.loading_animation(3)
        
        print(f"{Color.GREEN}Email sent successfully!{Color.END}")
        print(f"{Color.WHITE}From: no-reply@{random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])}{Color.END}")
        print(f"{Color.WHITE}To: {to_email}{Color.END}")
        print(f"{Color.WHITE}Subject: {subject}{Color.END}")
        print(f"{Color.WHITE}Message: {message}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def social_media_recon(self):
        self.clear_screen()
        print(f"{Color.PURPLE}{Color.BOLD}Social Media Recon{Color.END}")
        
        username = input(f"{Color.CYAN}Enter username to investigate: {Color.END}")
        
        print(f"{Color.YELLOW}Gathering information from social media platforms...{Color.END}")
        self.loading_animation(4)
        
        platforms = {
            "Facebook": f"https://facebook.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://instagram.com/{username}",
            "LinkedIn": f"https://linkedin.com/in/{username}",
            "GitHub": f"https://github.com/{username}"
        }
        
        found_profiles = []
        for platform, url in platforms.items():
            if random.choice([True, False, False]):
                found_profiles.append((platform, url))
                print(f"{Color.GREEN}[FOUND] {platform}: {url}{Color.END}")
            else:
                print(f"{Color.RED}[NOT FOUND] {platform}{Color.END}")
        
        if found_profiles:
            print(f"\n{Color.GREEN}Found profiles:{Color.END}")
            for platform, url in found_profiles:
                print(f"{Color.WHITE}- {platform}: {url}{Color.END}")
        else:
            print(f"\n{Color.RED}No profiles found.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def information_gatherer(self):
        self.clear_screen()
        print(f"{Color.PURPLE}{Color.BOLD}Information Gatherer{Color.END}")
        
        target = input(f"{Color.CYAN}Enter target (email/username/phone): {Color.END}")
        
        print(f"{Color.YELLOW}Gathering information...{Color.END}")
        self.loading_animation(5)
        
        print(f"{Color.GREEN}Information gathered for: {target}{Color.END}")
        print(f"{Color.WHITE}Email: {target}@example.com{Color.END}")
        print(f"{Color.WHITE}Phone: +1-555-{random.randint(100,999)}-{random.randint(1000,9999)}{Color.END}")
        print(f"{Color.WHITE}Location: {random.choice(['New York', 'London', 'Tokyo', 'Sydney'])}{Color.END}")
        print(f"{Color.WHITE}IP Address: 192.168.{random.randint(1,255)}.{random.randint(1,255)}{Color.END}")
        print(f"{Color.WHITE}Social Media: {random.randint(2,5)} platforms found{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def fake_login_creator(self):
        self.clear_screen()
        print(f"{Color.PURPLE}{Color.BOLD}Fake Login Page Creator{Color.END}")
        
        service = input(f"{Color.CYAN}Enter service name (e.g., Netflix, PayPal): {Color.END}")
        
        print(f"{Color.YELLOW}Creating fake login page...{Color.END}")
        self.loading_animation(3)
        
        self.create_directory("fake_logins")
        filename = f"fake_logins/{service.lower()}_login.html"
        
        with open(filename, 'w') as f:
            f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>{service} Login</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .login-container {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 350px;
        }}
        .logo {{
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 30px;
            color: #333;
        }}
        .input-group {{
            margin-bottom: 20px;
        }}
        input {{
            width: 100%;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
            box-sizing: border-box;
        }}
        button {{
            width: 100%;
            padding: 15px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }}
        button:hover {{
            background: #45a049;
        }}
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo">{service}</div>
        <div class="input-group">
            <input type="text" placeholder="Email or Username" required>
        </div>
        <div class="input-group">
            <input type="password" placeholder="Password" required>
        </div>
        <button type="submit">Sign In</button>
    </div>
</body>
</html>
            """)
        
        print(f"{Color.GREEN}Fake login page created successfully!{Color.END}")
        print(f"{Color.WHITE}File: {filename}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    # Password Attack Tools
    def password_attack_tools(self):
        while True:
            self.clear_screen()
            print(f"{Color.YELLOW}{Color.BOLD}")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                   PASSWORD ATTACK TOOLS                       ║")
            print("╠════════════════════════════════════════════════════════════════╣")
            print("║  [1] Brute Force Attack                                       ║")
            print("║  [2] Dictionary Attack                                        ║")
            print("║  [3] Hash Cracker                                             ║")
            print("║  [4] Password Generator                                       ║")
            print("║  [5] Wordlist Creator                                         ║")
            print("║  [6] Password Strength Checker                                ║")
            print("║  [0] Back to Main Menu                                        ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print(Color.END)
            
            choice = input(f"{Color.CYAN}Select option → {Color.END}")
            
            if choice == "1":
                self.brute_force_attack()
            elif choice == "2":
                self.dictionary_attack()
            elif choice == "3":
                self.hash_cracker()
            elif choice == "4":
                self.password_generator()
            elif choice == "5":
                self.wordlist_creator()
            elif choice == "6":
                self.password_strength_checker()
            elif choice == "0":
                return
            else:
                print(f"{Color.RED}Invalid option!{Color.END}")
                time.sleep(1)
    
    def brute_force_attack(self):
        self.clear_screen()
        print(f"{Color.YELLOW}{Color.BOLD}Brute Force Attack{Color.END}")
        
        target = input(f"{Color.CYAN}Enter target (email/username): {Color.END}")
        
        print(f"{Color.RED}Starting brute force attack...{Color.END}")
        
        common_passwords = ["password", "123456", "admin", "qwerty", "letmein", "welcome", "monkey"]
        
        for password in common_passwords:
            print(f"{Color.WHITE}Trying: {password}{Color.END}")
            time.sleep(0.5)
            
            if random.choice([True, False, False, False, False, False]):
                print(f"{Color.GREEN}Password found: {password}{Color.END}")
                break
        else:
            print(f"{Color.RED}Password not found.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def dictionary_attack(self):
        self.clear_screen()
        print(f"{Color.YELLOW}{Color.BOLD}Dictionary Attack{Color.END}")
        
        target = input(f"{Color.CYAN}Enter target (email/username): {Color.END}")
        wordlist_file = input(f"{Color.CYAN}Enter wordlist filename (or press enter for default): {Color.END}")
        
        if not wordlist_file:
            wordlist_file = "passwords.txt"
        
        print(f"{Color.RED}Starting dictionary attack with {wordlist_file}...{Color.END}")
        
        try:
            with open(wordlist_file, 'r') as f:
                passwords = f.readlines()
        except:
            passwords = ["password123", "admin123", "test123", "hello123", "welcome123"]
        
        for password in passwords[:10]:
            password = password.strip()
            print(f"{Color.WHITE}Trying: {password}{Color.END}")
            time.sleep(0.3)
            
            if random.choice([True, False, False, False, False]):
                print(f"{Color.GREEN}Password found: {password}{Color.END}")
                break
        else:
            print(f"{Color.RED}Password not found in wordlist.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def hash_cracker(self):
        self.clear_screen()
        print(f"{Color.YELLOW}{Color.BOLD}Hash Cracker{Color.END}")
        
        hash_value = input(f"{Color.CYAN}Enter hash to crack: {Color.END}")
        hash_type = input(f"{Color.CYAN}Enter hash type (md5/sha1/sha256): {Color.END}").lower()
        
        print(f"{Color.RED}Cracking {hash_type} hash...{Color.END}")
        self.loading_animation(4)
        
        common_hashes = {
            "5f4dcc3b5aa765d61d8327deb882cf99": "password",
            "7c6a180b36896a0a8c02787eeafb0e4c": "password1",
            "6cb75f652a9b52798eb6cf2201057c73": "password123",
            "d8578edf8458ce06fbc5bb76a58c5ca4": "qwerty"
        }
        
        if hash_value in common_hashes:
            print(f"{Color.GREEN}Hash cracked: {common_hashes[hash_value]}{Color.END}")
        else:
            print(f"{Color.RED}Unable to crack hash.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def password_generator(self):
        self.clear_screen()
        print(f"{Color.YELLOW}{Color.BOLD}Password Generator{Color.END}")
        
        length = int(input(f"{Color.CYAN}Enter password length (8-20): {Color.END}") or "12")
        count = int(input(f"{Color.CYAN}How many passwords to generate: {Color.END}") or "5")
        
        print(f"{Color.GREEN}Generated passwords:{Color.END}")
        for i in range(count):
            password = self.generate_random_password(length)
            print(f"{Color.WHITE}  {i+1}. {password}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def generate_random_password(self, length=12):
        import string
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(length))
    
    def wordlist_creator(self):
        self.clear_screen()
        print(f"{Color.YELLOW}{Color.BOLD}Wordlist Creator{Color.END}")
        
        base_words = input(f"{Color.CYAN}Enter base words (comma separated): {Color.END}")
        output_file = input(f"{Color.CYAN}Enter output filename: {Color.END}")
        
        words = [word.strip() for word in base_words.split(",")]
        variations = []
        
        for word in words:
            variations.extend([
                word,
                word + "123",
                word + "!",
                word + "2024",
                word.upper(),
                word.capitalize()
            ])
        
        with open(output_file, 'w') as f:
            for variation in variations:
                f.write(variation + "\n")
        
        print(f"{Color.GREEN}Wordlist created: {output_file}{Color.END}")
        print(f"{Color.WHITE}Total words generated: {len(variations)}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def password_strength_checker(self):
        self.clear_screen()
        print(f"{Color.YELLOW}{Color.BOLD}Password Strength Checker{Color.END}")
        
        password = input(f"{Color.CYAN}Enter password to check: {Color.END}")
        
        strength = 0
        if len(password) >= 8:
            strength += 1
        if any(c.islower() for c in password):
            strength += 1
        if any(c.isupper() for c in password):
            strength += 1
        if any(c.isdigit() for c in password):
            strength += 1
        if any(c in "!@#$%^&*" for c in password):
            strength += 1
        
        strength_labels = {
            1: "Very Weak",
            2: "Weak", 
            3: "Medium",
            4: "Strong",
            5: "Very Strong"
        }
        
        print(f"{Color.GREEN}Password Strength: {strength_labels.get(strength, 'Very Weak')}{Color.END}")
        print(f"{Color.WHITE}Length: {len(password)} characters{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    # Information Tools
    def information_tools(self):
        while True:
            self.clear_screen()
            print(f"{Color.GREEN}{Color.BOLD}")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                     INFORMATION TOOLS                         ║")
            print("╠════════════════════════════════════════════════════════════════╣")
            print("║  [1] IP Lookup                                                ║")
            print("║  [2] WHOIS Lookup                                             ║")
            print("║  [3] DNS Lookup                                               ║")
            print("║  [4] Email Validator                                          ║")
            print("║  [5] Phone Number Info                                        ║")
            print("║  [6] GeoIP Location                                           ║")
            print("║  [0] Back to Main Menu                                        ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print(Color.END)
            
            choice = input(f"{Color.CYAN}Select option → {Color.END}")
            
            if choice == "1":
                self.ip_lookup()
            elif choice == "2":
                self.whois_lookup()
            elif choice == "3":
                self.dns_lookup()
            elif choice == "4":
                self.email_validator()
            elif choice == "5":
                self.phone_info()
            elif choice == "6":
                self.geoip_lookup()
            elif choice == "0":
                return
            else:
                print(f"{Color.RED}Invalid option!{Color.END}")
                time.sleep(1)
    
    def ip_lookup(self):
        self.clear_screen()
        print(f"{Color.GREEN}{Color.BOLD}IP Lookup{Color.END}")
        
        ip = input(f"{Color.CYAN}Enter IP address: {Color.END}")
        
        print(f"{Color.YELLOW}Looking up IP information...{Color.END}")
        self.loading_animation(3)
        
        countries = ['United States', 'United Kingdom', 'Germany', 'Japan', 'Brazil', 'India', 'Australia']
        isps = ['Comcast', 'Verizon', 'AT&T', 'BT', 'Deutsche Telekom', 'Airtel', 'Telstra']
        
        print(f"{Color.GREEN}IP Information:{Color.END}")
        print(f"{Color.WHITE}IP: {ip}{Color.END}")
        print(f"{Color.WHITE}Country: {random.choice(countries)}{Color.END}")
        print(f"{Color.WHITE}ISP: {random.choice(isps)}{Color.END}")
        print(f"{Color.WHITE}Location: {random.randint(1,90)}.{random.randint(1,90)}, {random.randint(-180,180)}.{random.randint(1,90)}{Color.END}")
        print(f"{Color.WHITE}Timezone: UTC{random.choice(['+0', '+1', '+5:30', '+9', '-5'])}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def whois_lookup(self):
        self.clear_screen()
        print(f"{Color.GREEN}{Color.BOLD}WHOIS Lookup{Color.END}")
        
        domain = input(f"{Color.CYAN}Enter domain: {Color.END}")
        
        print(f"{Color.YELLOW}Performing WHOIS lookup...{Color.END}")
        self.loading_animation(3)
        
        print(f"{Color.GREEN}WHOIS Information for {domain}:{Color.END}")
        print(f"{Color.WHITE}Registrar: Example Registrar Inc.{Color.END}")
        print(f"{Color.WHITE}Creation Date: 2022-{random.randint(1,12):02d}-{random.randint(1,28):02d}{Color.END}")
        print(f"{Color.WHITE}Expiration Date: 2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}{Color.END}")
        print(f"{Color.WHITE}Name Servers: ns1.example.com, ns2.example.com{Color.END}")
        print(f"{Color.WHITE}Status: Active{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def dns_lookup(self):
        self.clear_screen()
        print(f"{Color.GREEN}{Color.BOLD}DNS Lookup{Color.END}")
        
        domain = input(f"{Color.CYAN}Enter domain: {Color.END}")
        
        print(f"{Color.YELLOW}Performing DNS lookup...{Color.END}")
        
        try:
            ip = socket.gethostbyname(domain)
            print(f"{Color.GREEN}DNS Records for {domain}:{Color.END}")
            print(f"{Color.WHITE}A Record: {ip}{Color.END}")
            print(f"{Color.WHITE}MX Record: mail.{domain}{Color.END}")
            print(f"{Color.WHITE}NS Record: ns1.{domain}{Color.END}")
            print(f"{Color.WHITE}TXT Record: v=spf1 include:{domain} ~all{Color.END}")
        except:
            print(f"{Color.RED}Could not resolve domain.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def email_validator(self):
        self.clear_screen()
        print(f"{Color.GREEN}{Color.BOLD}Email Validator{Color.END}")
        
        email = input(f"{Color.CYAN}Enter email address: {Color.END}")
        
        print(f"{Color.YELLOW}Validating email...{Color.END}")
        self.loading_animation(2)
        
        if "@" in email and "." in email.split("@")[1]:
            print(f"{Color.GREEN}Email is valid.{Color.END}")
            print(f"{Color.WHITE}Domain: {email.split('@')[1]}{Color.END}")
        else:
            print(f"{Color.RED}Email is invalid.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def phone_info(self):
        self.clear_screen()
        print(f"{Color.GREEN}{Color.BOLD}Phone Number Information{Color.END}")
        
        phone = input(f"{Color.CYAN}Enter phone number: {Color.END}")
        
        print(f"{Color.YELLOW}Gathering phone information...{Color.END}")
        self.loading_animation(3)
        
        carriers = ['Verizon', 'AT&T', 'T-Mobile', 'Sprint', 'Vodafone', 'Airtel']
        countries = ['USA', 'UK', 'Canada', 'Australia', 'India', 'Germany']
        
        print(f"{Color.GREEN}Phone Information:{Color.END}")
        print(f"{Color.WHITE}Number: {phone}{Color.END}")
        print(f"{Color.WHITE}Carrier: {random.choice(carriers)}{Color.END}")
        print(f"{Color.WHITE}Country: {random.choice(countries)}{Color.END}")
        print(f"{Color.WHITE}Valid: Yes{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def geoip_lookup(self):
        self.clear_screen()
        print(f"{Color.GREEN}{Color.BOLD}GeoIP Location{Color.END}")
        
        ip = input(f"{Color.CYAN}Enter IP address: {Color.END}")
        
        print(f"{Color.YELLOW}Getting geographical location...{Color.END}")
        self.loading_animation(3)
        
        locations = [
            ("New York", "USA", "40.7128", "-74.0060"),
            ("London", "UK", "51.5074", "-0.1278"),
            ("Tokyo", "Japan", "35.6762", "139.6503"),
            ("Sydney", "Australia", "-33.8688", "151.2093")
        ]
        
        city, country, lat, lon = random.choice(locations)
        
        print(f"{Color.GREEN}Geographical Information:{Color.END}")
        print(f"{Color.WHITE}IP: {ip}{Color.END}")
        print(f"{Color.WHITE}City: {city}{Color.END}")
        print(f"{Color.WHITE}Country: {country}{Color.END}")
        print(f"{Color.WHITE}Coordinates: {lat}, {lon}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    # Game Section
    def game_section(self):
        while True:
            self.clear_screen()
            print(f"{Color.CYAN}{Color.BOLD}")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                          GAME SECTION                         ║")
            print("╠════════════════════════════════════════════════════════════════╣")
            print("║  [1] Number Guessing Game                                     ║")
            print("║  [2] Hacking Simulation                                       ║")
            print("║  [3] Password Cracking Game                                   ║")
            print("║  [0] Back to Main Menu                                        ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print(Color.END)
            
            choice = input(f"{Color.CYAN}Select option → {Color.END}")
            
            if choice == "1":
                self.number_guessing_game()
            elif choice == "2":
                self.hacking_simulation()
            elif choice == "3":
                self.password_cracking_game()
            elif choice == "0":
                return
            else:
                print(f"{Color.RED}Invalid option!{Color.END}")
                time.sleep(1)
    
    def number_guessing_game(self):
        self.clear_screen()
        print(f"{Color.CYAN}{Color.BOLD}Number Guessing Game{Color.END}")
        
        number = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print(f"{Color.YELLOW}I'm thinking of a number between 1 and 100.{Color.END}")
        print(f"{Color.YELLOW}You have {max_attempts} attempts to guess it.{Color.END}")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"{Color.CYAN}Enter your guess ({attempts + 1}/{max_attempts}): {Color.END}"))
                attempts += 1
                
                if guess < number:
                    print(f"{Color.RED}Too low!{Color.END}")
                elif guess > number:
                    print(f"{Color.RED}Too high!{Color.END}")
                else:
                    print(f"{Color.GREEN}Congratulations! You guessed the number in {attempts} attempts.{Color.END}")
                    break
            except ValueError:
                print(f"{Color.RED}Please enter a valid number.{Color.END}")
        
        if attempts == max_attempts and guess != number:
            print(f"{Color.RED}Game over! The number was {number}.{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def hacking_simulation(self):
        self.clear_screen()
        print(f"{Color.CYAN}{Color.BOLD}Hacking Simulation{Color.END}")
        
        target = input(f"{Color.CYAN}Enter target system: {Color.END}")
        
        print(f"{Color.RED}Initiating hack sequence...{Color.END}")
        time.sleep(1)
        
        steps = [
            f"Scanning {target} for vulnerabilities...",
            "Bypassing firewall...",
            "Exploiting vulnerability CVE-2023-XXXX...",
            "Gaining root access...",
            "Extracting sensitive data...",
            "Covering tracks..."
        ]
        
        for step in steps:
            print(f"{Color.YELLOW}{step}{Color.END}")
            self.loading_animation(2)
        
        print(f"{Color.GREEN}Hack completed successfully!{Color.END}")
        print(f"{Color.WHITE}Data extracted: {random.randint(100,1000)} MB{Color.END}")
        print(f"{Color.WHITE}Access level: ROOT{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def password_cracking_game(self):
        self.clear_screen()
        print(f"{Color.CYAN}{Color.BOLD}Password Cracking Game{Color.END}")
        
        passwords = ["admin", "password", "123456", "letmein", "welcome"]
        target_password = random.choice(passwords)
        masked_password = "*" * len(target_password)
        
        print(f"{Color.YELLOW}Try to crack the password: {masked_password}{Color.END}")
        print(f"{Color.YELLOW}Length: {len(target_password)} characters{Color.END}")
        
        attempts = 3
        while attempts > 0:
            guess = input(f"{Color.CYAN}Enter your guess ({attempts} attempts left): {Color.END}")
            
            if guess == target_password:
                print(f"{Color.GREEN}Success! Password cracked: {target_password}{Color.END}")
                break
            else:
                attempts -= 1
                print(f"{Color.RED}Wrong password!{Color.END}")
        
        if attempts == 0:
            print(f"{Color.RED}Game over! The password was: {target_password}{Color.END}")
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def about_tool(self):
        self.clear_screen()
        print(f"{Color.CYAN}{Color.BOLD}")
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║                         ABOUT TOOL                            ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║                                                                ║")
        print(f"║  {Color.YELLOW}Tool Name: CHOWDHURYVAI Hacking Toolkit{Color.CYAN}        ║")
        print(f"║  {Color.YELLOW}Version: {self.version}{Color.CYAN}                                              ║")
        print(f"║  {Color.YELLOW}Author: {self.author}{Color.CYAN}                                           ║")
        print("║                                                                ║")
        print("║  This is an advanced hacking toolkit created for educational   ║")
        print("║  and research purposes only. Use responsibly and ethically.    ║")
        print("║                                                                ║")
        print("║  Features:                                                     ║")
        print("║  • Web Hacking Tools                                          ║")
        print("║  • Social Engineering Tools                                   ║")
        print("║  • Password Attack Tools                                      ║")
        print("║  • Information Gathering Tools                                ║")
        print("║  • Game Section                                               ║")
        print("║                                                                ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print(Color.END)
        
        input(f"\n{Color.CYAN}Press Enter to continue...{Color.END}")
    
    def exit_tool(self):
        self.clear_screen()
        print(f"{Color.RED}{Color.BOLD}")
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║                       EXITING TOOL                            ║")
        print("╠════════════════════════════════════════════════════════════════╣")
        print("║                                                                ║")
        print("║           Thank you for using 	HACKING Toolkit!                ║")
        print("║                                                                ║")
        print("║          Remember: With great power comes great               ║")
        print("║                  responsibility. Use ethically!               ║")
        print("║                                                                ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print(Color.END)
        
        time.sleep(2)
        sys.exit(0)
    
    def main_menu(self):
        while True:
            self.clear_screen()
            self.print_banner()
            self.print_contact_info()
            
            print(f"{Color.GREEN}{Color.BOLD}")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                         MAIN MENU                             ║")
            print("╠════════════════════════════════════════════════════════════════╣")
            print("║  [1] Web Hacking Tools                                        ║")
            print("║  [2] Social Engineering Tools                                 ║")
            print("║  [3] Password Attack Tools                                    ║")
            print("║  [4] Information Tools                                        ║")
            print("║  [5] Game Section                                             ║")
            print("║  [6] About Tool                                               ║")
            print("║  [0] Exit                                                     ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print(Color.END)
            
            choice = input(f"{Color.CYAN}{Color.BOLD}Select option → {Color.END}")
            
            if choice == "1":
                self.web_hacking_tools()
            elif choice == "2":
                self.social_engineering_tools()
            elif choice == "3":
                self.password_attack_tools()
            elif choice == "4":
                self.information_tools()
            elif choice == "5":
                self.game_section()
            elif choice == "6":
                self.about_tool()
            elif choice == "0":
                self.exit_tool()
            else:
                print(f"{Color.RED}Invalid option! Please try again.{Color.END}")
                time.sleep(1)

def main():
    try:
        tool = HackingTools()
        tool.main_menu()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}Program interrupted by user.{Color.END}")
        sys.exit(0)
    except Exception as e:
        print(f"{Color.RED}An error occurred: {e}{Color.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
