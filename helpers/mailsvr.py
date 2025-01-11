import os
import datetime
from helpers.config import MAIL_PROFILE, MAIL_SVR, DATA_EXFILTRATION_SIZE, PHISHING_IOC_SUBJ, PHISHING_IOC_BODY, PHISHING_CAMPAIGN_DOMAIN
from utils.console_logger import log

def generate_benign():
    os.system(f"echo \"Test email\" | mail -s \"Benign traffic generation\" -- {MAIL_PROFILE}@{MAIL_SVR}")
    log("success", "Benign email sent")

def generate_data_exfiltration():
    log_line = f"from=<{MAIL_PROFILE}@{MAIL_SVR}> size={DATA_EXFILTRATION_SIZE} nrcpt=1 (queue active)"
    os.system(f"logger -t \"{MAIL_PROFILE}\" \"{log_line}\"")
    log("success", "Data exfiltration log generated")

def generate_phishing_ioc():
    os.system(f"echo \"{PHISHING_IOC_BODY}\" | mail -s \"Phishing IOC traffic generation\" -- {MAIL_PROFILE}@{MAIL_SVR}")
    os.system(f"echo \"Phishing IOC traffic generation\" | mail -s \"{PHISHING_IOC_SUBJ}\" -- {MAIL_PROFILE}@{MAIL_SVR}")
    log("success", "Phishing IOC email sent")

def generate_phishing_campaign():
    now = datetime.datetime.now()
    date = now.strftime("%a %b %d %H:%M:%S %Y")
    message_id = f"<{now.strftime('%Y%m%d%H%M%S')}.1.1@{PHISHING_CAMPAIGN_DOMAIN}>"
    log_line = f"from=test@{PHISHING_CAMPAIGN_DOMAIN}, date={date}, to={MAIL_PROFILE}@{MAIL_SVR}, subject=Phishing Campaign traffic Generation, message_id={message_id}, body=Phishing Campaign traffic Generation"
    os.system(f"/logger -t \"{MAIL_PROFILE}\" \"{log_line}\"")
