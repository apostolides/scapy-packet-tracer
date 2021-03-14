import sniff
import utils
import threading
import signal
import sys

def signal_handler(sig, frame):
    sniff.end_sniffer()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
sniff.start_sniffer()

current_source = None

while True:
    new_source = sniff.get_source()
    if new_source != current_source:
        current_source = new_source
        country_details = utils.country_from_ip(current_source)
        print(f'[*] IP: {current_source} Country: {country_details["country_name"]} | City: {country_details["city"]} | Region: {country_details["region"]}')
