import argparse
from .validators import valid_int_range, valid_path, valid_float_range, valid_name

def build_parser():
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument("path", nargs="?", type=valid_path)

    parser.add_argument("-p", "--path", type=valid_path)

    parser.add_argument("-w", "--width", type=valid_int_range(1,70))
    parser.add_argument("-h", "--height", type=valid_int_range(1,70))
    parser.add_argument("-r", "--ratio", type=valid_float_range(0.01,3))

    parser.add_argument("-f", "--fps", type=valid_int_range(1,60))
    parser.add_argument("-t", "--threshold", type=valid_int_range(1,255))
    parser.add_argument("-d", "--duration", type=valid_int_range(min_val=1))
    parser.add_argument("-s", "--skip", type=valid_int_range(min_val=1))

    parser.add_argument("-n", "--name", type=valid_name)

    parser.add_argument("--help", action="store_true")

    return parser