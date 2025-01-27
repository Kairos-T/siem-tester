import os
from utils.console_logger import log
from helpers.config import WEB_SVR, WORD_LIST_PATH, SQLMAP_QUERY_PATH


def generate_benign():
    '''
    Generates a benign HTTP request to the web server. This should not trigger any alerts.
    '''
    os.system(f"curl -s http://{WEB_SVR}")
    log("success", "Benign HTTP request sent")


def generate_badbot():
    '''
    Generates a HTTP request to the web server with a known bad bot user agent. This should trigger an alert.
    '''

    word_list_dir = os.getcwd() + "/" + WORD_LIST_PATH
    
    os.system(f"sqlmap -u http://{WEB_SVR}/{SQLMAP_QUERY_PATH} --dbs --batch")
    os.system(f"dirb http://{WEB_SVR} {word_list_dir} -r -S -a dirb") 
    
    log("success", "Bad bot HTTP request sent")

def generate_unusual_pattern():
    '''
    Generates a large number of HTTP requests to the web server in a short period of time. This should trigger an alert.
    '''
    
    os.system(f"ab -n 1000 -c 100 http://{WEB_SVR}/")
    
    log("success", "Unusual pattern HTTP request sent")
    