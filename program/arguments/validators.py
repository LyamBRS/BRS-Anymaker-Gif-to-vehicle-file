import argparse
from pathlib import Path
import sys
from ..prints.debug import BrLogs as B
import re

def valid_path(value):
    path = Path(value)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"{B.RED}Path does not exist: {B.DIM}{value}{B.RESET}")
    return path

def valid_int_range(min_val=None, max_val=None):
    def validator(value):
        try:
            ivalue = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError(f"{B.RED}Must be an integer{B.RESET}")

        if min_val is not None and ivalue < min_val:
            raise argparse.ArgumentTypeError(f"{B.RED}Must be {B.BOLD}{B.BRIGHT_RED}>= {min_val}{B.RESET}")

        if max_val is not None and ivalue > max_val:
            raise argparse.ArgumentTypeError(f"{B.RED}Must be {B.BOLD}{B.BRIGHT_RED}<= {max_val}{B.RESET}")

        return ivalue

    return validator

def valid_float_range(min_val=None, max_val=None):
    def validator(value):
        try:
            fvalue = float(value)
        except ValueError:
            raise argparse.ArgumentTypeError(f"{B.RED}Must be a float{B.RESET}")

        if min_val is not None and fvalue < min_val:
            raise argparse.ArgumentTypeError(f"{B.RED}Must be {B.BOLD}{B.BRIGHT_RED}>= {min_val}{B.RESET}")

        if max_val is not None and fvalue > max_val:
            raise argparse.ArgumentTypeError(f"{B.RED}Must be {B.BOLD}{B.BRIGHT_RED}<= {max_val}{B.RESET}")

        return fvalue

    return validator

def valid_name(value):
    if len(value) > 16:
        raise argparse.ArgumentTypeError(f"{B.RED}Must be at most {B.BOLD}16 characters{B.RESET}{B.RED} long")

    if not re.fullmatch(r"[A-Za-z0-9_]+", value):
        raise argparse.ArgumentTypeError(
            "Only letters, numbers, and underscores are allowed"
        )

    return value