import argparse
import sys

def custom_help():
    print("\033[92m=== MY TOOL ===\033[0m")
    print("\033[96mUsage:\033[0m script.py [OPTIONS] path\n")
    
    print("\033[95mOptions:\033[0m")
    print("  \033[96m-w, --width <int>\033[0m    Set width")
    print("  \033[96m-v, --verbose\033[0m        Enable verbose")
    print("  \033[96m-h, --help\033[0m           Show this help\n")


parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("-w", "--width", type=int)
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-h", "--help", action="store_true")

args, unknown = parser.parse_known_args()

if args.help:
    custom_help()
    sys.exit(0)