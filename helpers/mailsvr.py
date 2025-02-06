import os
import datetime
from helpers.config import (
    MAIL_PROFILE,
    MAIL_SVR,
    DATA_EXFILTRATION_SIZE,
    PHISHING_IOC_SUBJ,
    PHISHING_IOC_BODY,
    PHISHING_CAMPAIGN_DOMAIN,
    PHISHING_CAMPAIGN_BODY,
)
from utils.console_logger import log


def generate_benign():
    """
    Generates a test email that is sent via the mail server. This should not trigger any alerts.
    """
    os.system(
        f'echo "Test email" | mail -s "Benign traffic generation" -- {MAIL_PROFILE}@{MAIL_SVR}'
    )
    log("success", "Benign email sent")


def generate_data_exfiltration():
    """
    Generates a log entry that simulates data exfiltration via email. This should trigger an alert.
    """
    log_line = f"from=<{MAIL_PROFILE}@{MAIL_SVR}> size={DATA_EXFILTRATION_SIZE} nrcpt=1 (queue active)"
    os.system(f'logger -t "{MAIL_PROFILE}" "{log_line}"')
    log("success", "Data exfiltration log generated")


def generate_phishing_ioc():
    """
    Generates an email that contains a phishing IOC. This should trigger an alert.
    """
    os.system(
        f'echo "{PHISHING_IOC_BODY}" | mail -s "Phishing IOC traffic generation" -- {MAIL_PROFILE}@{MAIL_SVR}'
    )
    os.system(
        f'echo "Phishing IOC traffic generation" | mail -s "{PHISHING_IOC_SUBJ}" -- {MAIL_PROFILE}@{MAIL_SVR}'
    )
    log("success", "Phishing IOC email sent")


def generate_phishing_campaign():
    """
    Generates a log entry and email that:
    1. Originates from a domain that is part of a phishing campaign
    2. Contains a link to a phishing website
    """
    now = datetime.datetime.now()
    date = now.strftime("%a %b %d %H:%M:%S %Y")

    # 1.
    message_id = f"<{now.strftime('%Y%m%d%H%M%S')}.1.1@{PHISHING_CAMPAIGN_DOMAIN}>"
    log_line = f"from=test@{PHISHING_CAMPAIGN_DOMAIN}, date={date}, to={MAIL_PROFILE}@{MAIL_SVR}, subject=Phishing Campaign traffic Generation, message_id={message_id}, body=Phishing Campaign traffic Generation"
    os.system(f'logger -t "{MAIL_PROFILE}" "{log_line}"')
    log("success", "Phishing campaign log (1/2) generated")

    # 2.
    os.system(
        f'echo "{PHISHING_CAMPAIGN_BODY}" | mail -s "Phishing Campaign traffic Generation" -- {MAIL_PROFILE}@{MAIL_SVR}'
    )
    log("success", "Phishing campaign email (2/2) sent")
