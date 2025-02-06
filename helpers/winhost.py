import os
from helpers.config import C2_DOMAIN, PHISHING_DOMAIN
from utils.console_logger import log


def generate_malware():
    """
    Generates a HTTP request to the C2 server. This should trigger an alert.
    """
    os.system(f"curl -s http://{C2_DOMAIN}")
    log("success", "Malware HTTP request sent")


def generate_phishing():
    """
    Generates a HTTP request to the phishing domain. This should trigger an alert.
    """
    os.system(f"curl -s http://{PHISHING_DOMAIN}")
    log("success", "Phishing HTTP request sent")
