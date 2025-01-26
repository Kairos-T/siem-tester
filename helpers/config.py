#########################
# Global Configurations #
#########################

TENANT_NAME = "agatha.com"
SPLUNK_HOST = "www.agatha.com:8000"

##################################
# Module-Specific Configurations #
##################################

# Web Server
WEB_SVR = "www.agatha.com"
# BAD_BOT_USER_AGENT = "sqlmap/1.3.11#stable (http://sqlmap.org)"
SQLMAP_QUERY_PATH = "orderdetail.aspx?Id=1"
WORD_LIST_PATH = "dataset/wordlist_mini.txt"

# Mail Server
MAIL_SVR = "agatha.com"
MAIL_PROFILE = "postfix"
DATA_EXFILTRATION_SIZE = 12500000
PHISHING_IOC_SUBJ = "Important"
PHISHING_IOC_BODY = "Dear customer, an important message is waiting for you. Please click the link below to view it:\n\n"
PHISHING_CAMPAIGN_DOMAIN = "duckdns.org"
PHISHING_CAMPAIGN_BODY = "Dear customer, please click the link below: helmutz.com.15-235-9-25.cprapid.com"
