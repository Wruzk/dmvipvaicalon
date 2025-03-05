import os, string, random, uuid, threading, time, subprocess, calendar
from unidecode import unidecode
from os import system
import requests
import re
import time
import sys
from bs4 import BeautifulSoup  # Đảm bảo dòng này tồn tại
from rich.progress import track
from time import sleep
from colorama import Fore, Style, init
import socks
import socket
from stem import Signal
from colorama import init, Fore, Back, Style
from rich.console import Console
def generate_random_name():
    ho = [
        "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đặng", "Bùi", "Đỗ", "Ngô", 
        "Hồ", "Lý", "Mai", "Phan", "Cao", "Nguyễn Văn", "Đinh", "Dương", "Tô", "Lâm", 
        "Võ", "Bảo", "Châu", "Lương", "Hà", "Đoàn", "Công", "Lạc", "Trương", "Vương", 
        "Bạch", "Phú", "Hải", "Hùng", "Đinh", "Hoài", "Thái", "Quyết"
    ]
    
    ten_dem = [
        "Văn", "Thị", "Hữu", "Quốc", "Minh", "Thanh", "Duy", "Anh", "Ngọc", "Trung", 
        "Tấn", "Quyên", "Lan", "Mai", "Vũ", "Kiều", "Linh", "Lệ", "Đoàn", "Khoa", 
        "Bình", "Hiền", "Hạ", "Như", "Linh", "Nhi", "Thảo", "Mỹ", "Lương", "Tú", 
        "Mỹ", "Ái", "Kim", "Cẩm", "Khánh", "Ánh", "Bích", "Thúy", "Quyên"
    ]
    
    ten = [
        "Tuấn", "Linh", "Hạnh", "Hùng", "Hà", "Sơn", "Khánh", "Phương", "Long", 
        "Tâm", "Như", "Nghĩa", "Bảo", "Vĩnh", "Hòa", "Lệ", "Sáng", "Hiếu", "Tú", 
        "Nhi", "Thảo", "Quỳnh", "Cẩm", "Khải", "An", "Phúc", "Bích", "Duy", "Lan", 
        "Mai", "Trang", "Hương", "Giang", "Nhật", "Tú Anh", "Lưu", "Trinh", "Hải", 
        "Hải Âu", "Ngân", "Bích"
    ]
    
    ho_va_ten = f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"
    username_base = unidecode(ho_va_ten).replace(" ", "").lower()
    username = f"{username_base}{random.randint(100, 999)}"

    return ho_va_ten, username
colors1 = [
    "FF9900", "FFFF33", "33FFFF", "FF99FF", "FF3366", "FFFF66", "FF00FF", "66FF99", "00CCFF", 
    "FF0099", "FF0066", "0033FF", "FF9999", "00FF66", "00FFFF", "CCFFFF", "8F00FF", "FF00CC", 
    "FF0000", "FF1100", "FF3300", "FF4400", "FF5500", "FF6600", "FF7700", "FF8800", "FF9900", 
    "FFaa00", "FFbb00", "FFcc00", "FFdd00", "FFee00", "FFff00", "FFFFFF", "FFEBCD", "F5F5DC", 
    "F0FFF0", "F5FFFA", "F0FFFF", "F0F8FF", "FFF5EE", "F5F5F5", "9B30FF", "FF6347", "FFD700", 
    "FF1493", "00BFFF", "48D1CC", "7FFF00", "DA70D6", "00FF7F", "FF4500", "2E8B57", "20B2AA", 
    "ADFF2F", "FF6347", "32CD32", "8A2BE2", "D2691E", "B8860B", "A52A2A", "DC143C", "8B0000", 
    "FF1493", "FF4500", "4682B4", "5F9EA0", "6495ED", "7FFF00", "32CD32", "800080", "9ACD32", 
    "A52A2A", "6B8E23", "BDB76B", "800000", "BC8F8F", "FFB6C1", "FAEBD7", "FFE4E1", "FFFAF0", 
    "F0E68C", "B0E0E6", "F4A460", "D3D3D3"
]

def hex_to_ansi_random():
    hex_color = random.choice(colors1)
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) 
    return f'\033[38;2;{r};{g};{b}m' 
    
def delay(delay_time):
    for t in range(delay_time, -1, -1):
        sys.stdout.write(f"\r{hex_to_ansi_random()}{Style.BRIGHT}- ĐANG CHỐNG BLOCK CHẠY LẠI SAU: {t}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\r                                                                            \r")
def loigm(delay_time):
    for t in range(delay_time, -1, -1):
        sys.stdout.write(f"\r{hex_to_ansi_random()}{Style.BRIGHT}- BẠN YÊU CẦU QUÁ NHIỀU GMAIL VUI LÒNG CHỜ: {t}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\r                                                                            \r")
def cho(delay_time):
    for t in range(delay_time, -1, -1):
        sys.stdout.write(f"\r{hex_to_ansi_random()}{Style.BRIGHT}- VUI LÒNG CHỜ: {t}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)                                                                          
        sys.stdout.write("\r                                                                            \r")
init(autoreset=True)
error = f"{Fore.RED}{Style.BRIGHT}LỖI{Style.RESET_ALL}"
def process_data():
    time.sleep(0.03)  
class TempMail:
    def __init__(self):
        self.api_url = "https://ext2.temp-mail.org"
        self.email = None
        self.token = None
        self.headers = {
            "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36", 
            "Authorization": "Bearer ",
        }

    def create_email(self):
        """Tạo email tạm thời."""
        response = requests.post(f"{self.api_url}/mailbox", headers=self.headers)
        loi1 = response.json()

        self.loigm = loi1.get("errorName")
        self.loigm1 = loi1.get("errorMessage")
        if response.status_code != 200:
            print(f"{error}{hex_to_ansi_random()}{Style.BRIGHT}- LỖI KHI TẠO EMAIL:{hex_to_ansi_random()}{Style.BRIGHT} {self.loigm1} {self.loigm}{Style.RESET_ALL}")
            loigm(120)
            return
        
        data = response.json()

        self.email = data.get("mailbox")
        self.token = data.get("token")

        if not self.email:
            print(f"{error}[-] Không thể tạo email tạm thời.")
            return

        if self.token:
            self.headers["Authorization"] += self.token

        print(f"{hex_to_ansi_random()}{Style.BRIGHT}- TẠO EMAIL TẠM THỜI:{hex_to_ansi_random()}{Style.BRIGHT} {self.email}{Style.RESET_ALL}")
        
    def check_inbox(self):
        """Kiểm tra email đến."""
        if not self.email:
            print(f"{error}[-] Chưa có email nào được tạo.")
            return []

        response = requests.get(f"{self.api_url}/messages", headers=self.headers)
        if response.status_code != 200:
            print(f"{error}[-] Lỗi khi kiểm tra hộp thư: {response.text}")
            return []

        data = response.json()
        return data.get("messages", [])

    def get_email_content(self, message_id):
        """Lấy nội dung email theo ID."""
        response = requests.get(f"{self.api_url}/messages/{message_id}", headers=self.headers)
        if response.status_code != 200:
            print(f"{error}[-] Lỗi khi lấy nội dung email:{hex_to_ansi_random()}{Style.BRIGHT} {response.text}")
            return ""

        data = response.json()
        return data.get("bodyHtml", "")

    def extract_code(self, content):
        """Trích xuất mã xác minh từ nội dung email."""
        match = re.search(r"\b\d{6}\b", content)
        if match:
            print(f"{hex_to_ansi_random()}{Style.BRIGHT}- MÃ XÁC MINH:{hex_to_ansi_random()}{Style.BRIGHT} {match.group(0)}{Style.RESET_ALL}")
        else:
            print(f"{error}[-] Không tìm thấy mã xác minh.")
        return match.group(0) if match else None
devices = [
    ("Android", "SM-A055F"),
    ("Android", "SM-A125F"),
    ("Android", "Pixel 5"),
    ("Android", "Galaxy S21"),
    ("iOS", "iPhone13,3"),
    ("iOS", "iPhone 12"),
    ("iOS", "iPad Pro"),
    ("Windows", "PC"),
    ("Macintosh", "MacBook Pro")
]
class MyHeaders:
    def __init__(self):
        self.head = {}
    def random_user_agent(self):
        browsers = [
            ("Chrome", lambda: f"{random.randint(80, 150)}.0.{random.randint(4000, 5000)}.{random.randint(100, 999)}"),
            ("Firefox", lambda: f"{random.randint(80, 150)}.0"),
            ("Edge", lambda: f"{random.randint(80, 150)}.0.{random.randint(6000, 7000)}.{random.randint(100, 999)}"),
            ("Opera", lambda: f"{random.randint(50, 90)}.0.{random.randint(2000, 3000)}.{random.randint(100, 999)}"),
        ]
        browser, version_generator = random.choice(browsers)
        version = version_generator()
        android_models = [
            "Pixel 6", "Pixel 7", "Pixel 5", "Pixel 4 XL", "Galaxy S22", "Galaxy S21", "Galaxy S20",
            "Galaxy Note 20", "Galaxy A71", "Galaxy A51", "Galaxy Z Fold 3", "Galaxy Z Flip 4",
            "Xiaomi Mi 11", "Xiaomi Redmi Note 10", "Xiaomi Poco X3", "Xiaomi Mi Mix Fold",
            "OnePlus 9", "OnePlus 10 Pro", "OnePlus Nord 2", "OnePlus 8T",
            "Oppo Reno 8", "Oppo Find X3 Pro", "Oppo A74", "Oppo F19 Pro",
            "Vivo X80", "Vivo Y21", "Vivo V23 Pro", "Vivo Z1 Pro",
            "Realme GT", "Realme Narzo 50", "Realme 8 Pro", "Realme X7",
            "Huawei P50 Pro", "Huawei Mate 40 Pro", "Huawei Nova 9", "Huawei Y9 Prime",
            "Honor 50", "Honor Magic4 Pro", "Honor 70", "Honor X8",
            "Sony Xperia 1 III", "Sony Xperia 5 II", "Sony Xperia 10 IV",
            "Asus ROG Phone 5", "Asus Zenfone 8", "Asus ROG Phone 6", "Nokia X20", "Nokia G50",
        ]
        model = random.choice(android_models)  # Random model từ danh sách
        user_agent = f"Mozilla/5.0 (Linux; Android {random.randint(7, 16)}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36"
        return user_agent
    def generate_headers(self):
        user_agent = self.random_user_agent()  # Gọi hàm random user-agent
        self.head = {
            'user-agent': user_agent,  
            'x-csrftoken': ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32)),
        }
def load_proxies(file_path):
    with open(file_path, "r") as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

# Kiểm tra proxy hoạt động
def check_proxy(proxy):
    test_url = "https://httpbin.org/ip"  # URL kiểm tra IP
    try:
        response = requests.get(test_url, proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        return False
    return False

# Hàm trả về một proxy hoạt động
def proxies():
    file_path = "proxy.txt"  # File chứa danh sách proxy
    proxies_list = load_proxies(file_path)
    for proxy in proxies_list:
        if check_proxy(proxy):  # Chỉ trả về proxy đầu tiên hoạt động
            return {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }
    raise Exception("Không có proxy nào hoạt động!")        
class tao_acc_instagram:
    def __init__(self):
        self.done, self.error, self.run = 0, 0, True
        self.head = {"user-agent": f"Instagram 195.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"}
        self.claimed_response = ["challenge", '"account_created":true']
        self.check_response = ["username_is_taken", "username_held_by_others"]
        self.error_response = ["signup_block", "generic_request_error"]
        self.unknown_response = ["server error", "html"]
        self.device_id = uuid.uuid4()        
        self.temp_mail = None
        self.email = None
        self.signup_code = None
        self.headers = MyHeaders()  # Khởi tạo đối tượng MyHeaders
        self.headers.generate_headers()  # Gọi phương thức generate_headers để tạo headers
        self.heade = self.headers.head  # Gán thuộc tính head vào đối tượng Xnce
        print(f"{hex_to_ansi_random()}{Style.BRIGHT}- KHỞI ĐỘNG TOOL{Style.RESET_ALL}")
        for _ in track(range(100), description=f'\r{hex_to_ansi_random()}{Style.BRIGHT}-- LOADING\r'):process_data()
        print("\n\n")
        os.system("clear")
    def verify_email(self):
        self.temp_mail = TempMail()
        self.temp_mail.create_email()
        self.email = self.temp_mail.email
        self.token = self.temp_mail.token
        data = {
            "phone_id": uuid.uuid4(),
            "guid": uuid.uuid4(),
            "device_id": self.device_id,
            "email": self.email,
            "waterfall_id": uuid.uuid4(),
            "auto_confirm_only": "false"
        }
        req = requests.post("https://i.instagram.com/api/v1/accounts/send_verify_email/", headers=self.head, data=data)
        if "email_sent" in req.text:
            print(f"{hex_to_ansi_random()}{Style.BRIGHT}- MÃ XÁC MINH ĐƯỢC GỬI TỚI:{hex_to_ansi_random()}{Style.BRIGHT} {self.email}{Style.RESET_ALL}")
            
            self.coo = req.cookies
            
        else:
            print(f"{error}{hex_to_ansi_random()}{Style.BRIGHT}- LỖI KHI GỬI MÃ XÁC MINH:{hex_to_ansi_random()}{Style.BRIGHT} {req.text}{Style.RESET_ALL}")
            input()
            exit()
            
    def confirmation_code(self):
        print(f"{hex_to_ansi_random()}{Style.BRIGHT}- ĐANG CHỜ MÃ XÁC MINH {Style.RESET_ALL}")
        cho(10)
        
        while True:
            inbox = self.temp_mail.check_inbox()
            if inbox:
                for email in inbox:
                    content = self.temp_mail.get_email_content(email["_id"])
                    code = self.temp_mail.extract_code(content)
                    if code:
                        data = {
                            "code": code,
                            "device_id": self.device_id,
                            "email": self.email,
                            "waterfall_id": uuid.uuid4()
                        }
                        req = requests.post("https://i.instagram.com/api/v1/accounts/check_confirmation_code/", headers=self.head, data=data, cookies=self.coo)
                        try:
                            self.signup_code = req.json()["signup_code"]
                            print(f"{hex_to_ansi_random()}{Style.BRIGHT}- XÁC MINH THÀNH CÔNG:{hex_to_ansi_random()}{Style.BRIGHT} {self.signup_code} {Style.RESET_ALL}")
                            cho(10)
                            return
                        except Exception as e:
                            print(f"[-] {req.text}")
                            input()
                            exit()  

    def web_register(self):
        ho_ten, username = generate_random_name()
        birth_month = str(random.randint(1, 12))
        birth_day = str(random.randint(1, 30))
        birth_year = str(random.randint(1998, 2006))   
        self.password = f"{username}{birth_year}{birth_month}"    
        data = {
            'enc_password': f"#PWD_INSTAGRAM_BROWSER:0:{calendar.timegm(time.gmtime())}:{self.password}",
            'day': birth_day,
            'email': self.email,
            'first_name': ho_ten,
            'month': birth_month,
            'username': username,
            'year': birth_year,
            'client_id': self.device_id,
            'force_sign_up_code': self.signup_code,
        }        
        cho(10)
        try:
            self.req = requests.post("https://www.instagram.com/accounts/web_create_ajax/", headers=self.heade, data=data)
            if any(cl in self.req.text for cl in self.claimed_response):
                data = self.req.json()
                self.ok = data.get("user_id")
                print("\n\n")
                print(f"{hex_to_ansi_random()}{Style.BRIGHT}------------------------------{Style.RESET_ALL}")  
                print(f"{hex_to_ansi_random()}{Style.BRIGHT}- TẠO TÀI KHOẢN THÀNH CÔNG {Style.RESET_ALL}")
                print(f"{hex_to_ansi_random()}{Style.BRIGHT}- USER_ID:{hex_to_ansi_random()}{Style.BRIGHT} {self.ok}{Style.RESET_ALL}")
                print(f"{hex_to_ansi_random()}{Style.BRIGHT}- HỌ TÊN:{hex_to_ansi_random()}{Style.BRIGHT} {ho_ten}{Style.RESET_ALL}")
                print(f"{hex_to_ansi_random()}{Style.BRIGHT}- USERNAME:{hex_to_ansi_random()}{Style.BRIGHT} {username}{Style.RESET_ALL}")
                print(f"{hex_to_ansi_random()}{Style.BRIGHT}- PASSWORD:{hex_to_ansi_random()}{Style.BRIGHT} {self.password}{Style.RESET_ALL}")
                print(f"{hex_to_ansi_random()}{Style.BRIGHT}------------------------------{Style.RESET_ALL}\n\n")  
                with open("account.txt", "a") as f:
                    f.write(f"Email: {self.email}\nUser_id: {self.ok}\nUsername: {username}\nPassword: {self.password}\nTokenEmail: {self.token}\n\n") 
                with open("accounts.txt", "a") as f:
                    f.write(f"{username}\n") 
            elif any(ch in self.req.text for ch in self.check_response):
                self.done += 1
            elif any(er in self.req.text for er in self.error_response) or self.req.status_code == 429:
                self.error += 1
                print(f"{error}{hex_to_ansi_random()}{Style.BRIGHT}- LỖI: {hex_to_ansi_random()}{Style.BRIGHT}{self.req.text}{Style.RESET_ALL}")
            else:
                print(f"{error}{hex_to_ansi_random()}{Style.BRIGHT}- LỖI BỊ NGHI LÀ SỬ DỤNG PROXY FAKE IP: {self.req.text}{Style.RESET_ALL}\n\n")
        except Exception as e:
            print(f"{error}[-] Lỗi: {e}")
    def run_registration(self):
      while True:
        try:
            self.verify_email()
            self.confirmation_code()
            self.web_register()
            delay(80)
        except Exception as e:
            print(f"{error}[-] Lỗi khi thực hiện quy trình: {e}")
            cho(10)
tao_acc_instagram().run_registration()
