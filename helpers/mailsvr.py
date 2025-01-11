import os
from helpers.config import MAIL_PROFILE, MAIL_SVR, DATA_EXFILTRATION_SIZE
from utils.console_logger import log

def generate_benign():
    os.system(f"echo \"Test email\" | mail -s \"Benign traffic generation\" -- {MAIL_PROFILE}@{MAIL_SVR}")
    log("success", "Benign email sent")

def generate_data_exfiltration():
    LOG_TAG = MAIL_PROFILE
    log_line = f"from=<{MAIL_PROFILE}@{MAIL_SVR}> size={DATA_EXFILTRATION_SIZE} nrcpt=1 (queue active)"
    os.system(f"logger -t \"{LOG_TAG}\" \"{log_line}\"")
    log("success", "Data exfiltration log generated")
