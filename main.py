import argparse
import textwrap
from utils.console_logger import log

class RawFormatter(argparse.HelpFormatter):
    def _fill_text(self, text, width, indent):
        return "\n".join([textwrap.fill(line, width) for line in textwrap.indent(textwrap.dedent(text), indent).splitlines()])


def parse_arguments():
    
    program_descripton = '''
    This program is used to create traffic to simulate different types of attacks to various servers in a network to test the effectiveness of SIEM solutions.
    Note: This program is developed by Kairos, Jia Xuan, Paige, Yong Xin and Wayne as part of our Cyber Operations and Threat Intelligence project, and is intended only for our use case.
    Do expect to make edits to the code to suit your own use case, and we are not responsible for any misuse of this program.
    
    Profiles:
        - mailsvr - Simulates traffic to a mail server.
    
    Tests and intended profiles:
        mailsvr:
            - data_exfiltration - Generates logs that reflect large volumes of data being transferred through the mail server.
            - phishing_ioc - Sends emails with known phishing indicators
    '''

    parser = argparse.ArgumentParser(description=program_descripton, formatter_class=RawFormatter)
        
    parser.add_argument('-p', '--profile', type=str, help='Specify profile of tests to run. Run -h for a list of profiles.')
    parser.add_argument('-b', '--benign', action='store_true', help='Generate benign traffic only.')
    parser.add_argument('-t', '--tests', nargs='+', help='Specify tests to run. Run -h for a list of tests.')
    return parser.parse_args()

def run_mailsvr_tests(args):
    from helpers.mailsvr import generate_benign, generate_data_exfiltration
    
    if args.benign:
        generate_benign()
    else:
        if args.tests:
            for test in args.tests:
                if test == 'data_exfiltration':
                    generate_data_exfiltration()
                else:
                    log("error", f"Test '{test}' not found.")
        else:
            log("warning", "No tests specified.")

def main():
    args = parse_arguments()

    if not args.profile or not (args.benign or args.tests):
        log("error", "Please specify a profile and test(s) to run.")
        exit()

    if args.profile == 'mailsvr':
        run_mailsvr_tests(args)
    else:
        log("error", f"Profile '{args.profile}' not recognized. Please specify a valid profile.")

if __name__ == '__main__':
    main()
