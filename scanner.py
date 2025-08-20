Python
import requests
from bs4 import BeautifulSoup

def scan(url):
    issues = []
    # SQL Injection Test
try:
    test_url = f"{url}?id=1'"
    response = requests.get(test_url, timeout=5)
    if "error" in response.text.lower():
        issues.append("SQL Injection vulnerability detected")
except:
    pass

# XSS Test
try:
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.find_all("script"):
        issues.append("Potential XSS vulnerability (unsafe scripts detected)")
except:
    pass

# Security Headers Check
try:
    response = requests.get(url, timeout=5)
    headers = response.headers
    if "X-XSS-Protection" not in headers:
        issues.append("Missing XSS protection header")
    if "Content-Security-Policy" not in headers:
        issues.append("Missing Content Security Policy header")
except:
    pass

return issues
