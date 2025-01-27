import argparse
import textwrap
from utils.console_logger import log


class RawFormatter(argparse.HelpFormatter):
    def _fill_text(self, text, width, indent):
        return "\n".join(
            [textwrap.fill(line, width) for line in textwrap.indent(textwrap.dedent(text), indent).splitlines()]
        )


def parse_arguments():
    program_description = '''
    This program is used to create traffic to simulate different types of attacks to various servers in a network to test the effectiveness of SIEM solutions.
    Note: This program is developed by Kairos, Jia Xuan, Paige, Yong Xin and Wayne as part of our Cyber Operations and Threat Intelligence project, and is intended only for our use case.
    Do expect to make edits to the code to suit your own use case, and we are not responsible for any misuse of this program.
    
    Profiles:
        - all - Run all benign log generation events.
        - mailsvr - Simulates traffic to a mail server.
        - websvr - Simulates traffic to an IIS web server.
    
    Tests and intended profiles:
        mailsvr:
            - data_exfiltration - Generates logs that reflect large volumes of data being transferred through the mail server.
            - phishing_ioc - Sends emails with known phishing indicators.
            - phishing_campaign - Sends emails containing links to, or originating from blacklisted domains/URLs.
        websvr:
            - brute_force - Generates logs that reflect multiple failed login attempts.
            - sqli - Generates logs that reflect SQL injection attempts.
            - xss - Generates logs that reflect cross-site scripting attempts. 
            - badbot - Generates logs that reflect bad bot traffic.
            - unusual_pattern - Generates logs that reflect unusual traffic patterns.
    '''
    parser = argparse.ArgumentParser(
        description=program_description, formatter_class=RawFormatter
    )
    parser.add_argument('-p', '--profile', type=str,
                        help='Specify profile of tests to run. Run -h for a list of profiles.')
    parser.add_argument('-b', '--benign', action='store_true',
                        help='Generate benign traffic only.')
    parser.add_argument('-t', '--tests', nargs='+',
                        help='Specify tests to run. Run -h for a list of tests.')
    return parser.parse_args()


class BaseProfile:
    def __init__(self, args):
        self.args = args

    def run_benign(self):
        """Run benign traffic generation."""
        raise NotImplementedError

    def run_tests(self):
        """Run specific tests."""
        raise NotImplementedError


class MailServerProfile(BaseProfile):
    BENIGN_FUNCTION = 'generate_benign'
    TEST_FUNCTIONS = {
        'data_exfiltration': 'generate_data_exfiltration',
        'phishing_ioc': 'generate_phishing_ioc',
        'phishing_campaign': 'generate_phishing_campaign',
    }

    def run_benign(self):
        from helpers.mailsvr import generate_benign
        generate_benign()

    def run_tests(self):
        from helpers.mailsvr import (
            generate_data_exfiltration,
            generate_phishing_ioc,
            generate_phishing_campaign,
        )

        for test in self.args.tests or []:
            function_name = self.TEST_FUNCTIONS.get(test)
            if function_name:
                locals()[function_name]()  # Dynamically call the test function
            else:
                log("error", f"Test '{test}' not found.")


class WebServerProfile(BaseProfile):
    BENIGN_FUNCTION = 'generate_benign'
    TEST_FUNCTIONS = {
        'badbot': 'generate_badbot',
        'unusual_pattern': 'generate_unusual_pattern',
        # 'brute_force': 'generate_brute_force',
        # 'sqli': 'generate_sqli',
        # 'xss': 'generate_xss',
    }

    def run_benign(self):
        from helpers.websvr import generate_benign
        generate_benign()

    def run_tests(self):
        from helpers.websvr import (
            generate_badbot,
            generate_unusual_pattern,
            # generate_brute_force,
            # generate_sqli,
            # generate_xss,
        )

        for test in self.args.tests or []:
            function_name = self.TEST_FUNCTIONS.get(test)
            if function_name:
                locals()[function_name]()  # Dynamically call the test function
            else:
                log("error", f"Test '{test}' not found.")


def main():
    args = parse_arguments()

    PROFILE_CLASSES = {
        'mailsvr': MailServerProfile,
        'websvr': WebServerProfile,
    }

    if not args.profile:
        log("error", "Please specify a profile to run. Run -h for help.")
        exit()

    if args.profile == 'all':
        log("info", "Running all benign log generation events...")
        for profile_class in PROFILE_CLASSES.values():
            profile = profile_class(args)
            profile.run_benign()
    elif args.profile in PROFILE_CLASSES:
        profile = PROFILE_CLASSES[args.profile](args)
        if args.benign:
            profile.run_benign()
        else:
            profile.run_tests()
    else:
        log("error", f"Profile '{args.profile}' not recognised. Please specify a valid profile or run -h for help.")
        exit()


if __name__ == '__main__':
    main()
