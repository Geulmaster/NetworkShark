import pyshark

capture = pyshark.LiveCapture(interface='Ethernet')

for packet in capture.sniff_continuously(packet_count=1):
    print("source: ", packet["ip"].src)
    print("destination: ", packet["ip"].dst)