import os
from utils.console_logger import log
from helpers.config import WEB_SVR, BAD_BOT_USER_AGENT


def generate_benign():
    '''
    Generates a benign HTTP request to the web server. This should not trigger any alerts.
    '''
    os.system(f"curl -s http://{WEB_SVR}")
    log("success", "Benign HTTP request sent")


def badbot():
    '''
    Generates a HTTP request to the web server with a known bad bot user agent. This should trigger an alert.
    '''
    os.system(f"curl -s -A \"{BAD_BOT_USER_AGENT}\" http://{WEB_SVR}")
    log("success", "Bad bot HTTP request sent")
