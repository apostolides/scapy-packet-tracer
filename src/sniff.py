from scapy.all import *
import threading

def add_to_source(packet):
    global source_ip
    source = str(packet[IP].src)
    if source != host:
      source_ip = source

def sniffer():
    global protocol, host, running
    while running:
        sniff(filter=f"{protocol} and host {host}",count=1,prn=add_to_source)

def start_sniffer():
    thread.start()

def end_sniffer():
    global running
    running = False
    thread.join()

def get_source():
    return source_ip

host = get_if_addr(conf.iface)
protocol = "tcp" 
source_ip = None

running = True
thread = threading.Thread(target=sniffer)
