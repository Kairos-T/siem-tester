import os
from helpers.config import MAIL_PROFILE, MAIL_SVR
from utils.console_logger import log

def generate_benign():
    os.system(F"echo \"Test email\" | mail -s \"Benign traffic generation\" -- {MAIL_PROFILE}@{MAIL_SVR}")
    log("success", "Benign email sent")