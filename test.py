import re
# log_pattern = re.compile(r'(?P<ip_address>\S+) \S+ \S+ \[.*?\] "(?P<method>\S+) (?P<request>\S+) \S+" (?P<status_code>\d+) \S+ "(?P<user_agent>.*?)"')
log_pattern = re.compile(r'(?P<ip_address>\S+) \S+ \S+ \[.*?\] "(?P<method>\S+) (?P<request>\S+) \S+" (?P<status_code>\d+) \S+ "(?P<user_agent>.*?)"')

match = log_pattern.match('172.16.0.1 - - [22/Nov/2023:12:43:50 +0000] "GET /styles/style3.css HTTP/1.1" 200 5432 "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"')
if match:
    print(True)