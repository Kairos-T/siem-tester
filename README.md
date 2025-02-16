# siem-tester

This program is used to create traffic to simulate different types of attacks to various servers in a network to test the effectiveness of SIEM solutions.
It is developed by Kairos, Jia Xuan, Paige, Yong Xin and Wayne as part of our Cyber Operations and Threat Intelligence project, and is intended only for our use case.

Do expect to make edits to the code to suit your own use case, and we are not responsible for any misuse of this program.

## Installation

This program is intended to run on various operating systems, including Windows and Linux (Ubuntu).

**Pre-requisites:**

- Windows:
  - Python 3.8 or higher
  - pip
  - git
- Linux:
  - Python 3.8 or higher
  - pip
  - git
  - sqlmap (websvr profile)
  - dirb (websvr profile)
  - mail (mailsvr profile)

**Steps:**

1. Clone the repository:

   ```bash
   git clone https://www.github.com/kairos-t/siem-tester
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Program Guide

### Profiles

| Profiles | Description                                        |
| -------- | -------------------------------------------------- |
| all      | (LINUX ONLY) Runs all benign log generation events |
| websvr   | Simulates traffic to a mail server                 |
| mailsvr  | Simulates traffic to an IIS web server             |
| linhost  | Simulates traffic to a Linux host                  |
| winhost  | Simulates traffic to a Windows host                |

### Options

| Options   | Description                                             |
| --------- | ------------------------------------------------------- |
| --tests   | Specify the tests to run (space delimited)              |
| --profile | Specify the profile to run                              |
| -b        | Run benign log generation events for a specific profile |

### Tests

| Profile | Tests             | Description                                                                                  |
| ------- | ----------------- | -------------------------------------------------------------------------------------------- |
| mailsvr | data_exfiltration | Generates logs that reflect large volumes of data being transferred through the mail server. |
| mailsvr | phishing_ioc      | Sends emails with known phishing indicators.                                                 |
| mailsvr | phishing_campaign | Sends emails containing links to, or originating from blacklisted domains/URLs.              |
| websvr  | brute_force       | Generates logs that reflect multiple failed login attempts.                                  |
| websvr  | sqli              | Generates logs that reflect SQL injection attempts.                                          |
| websvr  | xss               | Generates logs that reflect cross-site scripting attempts.                                   |
| websvr  | badbot            | Generates logs that reflect bad bot traffic.                                                 |
| linhost | syn_flood | Generates logs that reflect SYN flood attacks. |
| linhost | udp_flood | Generates logs that reflect UDP flood attacks. |
| winhost | malware | Generates logs that reflect a host connecting to a C2/malware server. |
| winhost | phishing | Generates logs that reflect a host connecting to a phishing site. |

### Examples

1. Run data exfiltration test on mail server profile:
   ```bash
   python main.py --profile mailsvr --tests data_exfiltration
   ```
2. Run phishing IOC and phishing campaign tests on mail server profile:
   ```bash
   python main.py --profile mailsvr --tests phishing_ioc phishing_campaign
   ```
3. Run brute force, SQLi, XSS and bad bot tests on web server profile:
   ```bash
   python main.py --profile websvr --tests brute_force sqli xss badbot
   ```
4. Run benign log generation events for mail server profile:
   ```bash
   python main.py --profile mailsvr -b
   ```
