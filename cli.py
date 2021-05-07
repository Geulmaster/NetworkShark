import pyshark

capture = pyshark.LiveCapture(interface='enp0s3')

packets_list = capture.sniff_continuously(packet_count=5)

for index, packet in enumerate(packets_list):
    try:
        print("source: ", packet["ip"].src)
        print("destination: ", packet["ip"].dst)
    except:
        print(f"Packet {index} do not have an IP layer")

# TODO: cli that gets interface, number of packets, an option to return other values than IPs