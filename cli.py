import pyshark
import argparse
import sys
import os
from configuration import change_config_file, config_reader

class Parser:

    def run_arguments(self):
        global args, parser
        parser = argparse.ArgumentParser(description="Check traffic")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-v", "--verbose", action="store_true")
        group.add_argument("-q", "--quiet", action="store_true")
        parser.add_argument("-inf", "--interface", help="Set interface")
        parser.add_argument("-a", "--amount", help="Set number of packets")
        parser.add_argument("-i", "--info", help="Set desired info")
        args = parser.parse_args()
        return args

config = config_reader()


def runner():
    if len(sys.argv) < 2:
        main()
    else:
        args_list = ["args.interface", "args.amount", "args.info"]
        for arg in args_list:
            if eval(arg):
                change_config_file(arg[5:], eval(arg))
                print(f"{arg[5:]} is set to {eval(arg)}")


def main():
    capture = pyshark.LiveCapture(interface=config["CONF"]["interface"])
    packets_list = capture.sniff_continuously(packet_count=int(config["CONF"]["amount"]))
    for index, packet in enumerate(packets_list):
        try:
            desired_info = config["CONF"]["info"].split()
            for type in desired_info:
                print("source: ", packet[type].src)
                print("destination: ", packet[type].dst)
        except:
            print(f"Packet {index} do not have an IP layer")


if __name__ == '__main__':
    parser = Parser()
    parser.run_arguments()
    runner()
