################################################################################################
# - File containing all the logic related to parsing the script's given parameters.
# - Ensuring they are valid, and point to existing locations
################################################################################################
from .prints.usage import print_full_usage, incorrect_usage_header, print_line
from .prints.debug import BrLogs
from .arguments.parser import build_parser
from pathlib import Path
import sys

#-----------------------------------------------------------------------------------------------
def handle_args(args):
    """
        Give it all the arguments passed to the script's execution.
        Will automatically verify all of them
    """
    parser = build_parser()
    args = parser.parse_args(args)

    if args.help:
        print_full_usage(BrLogs.info)
        sys.exit(0)

    if args.path is None:
        incorrect_usage_header(BrLogs.error)
        BrLogs.error("You must specify the path to a .gif file")
        print_line()
        sys.exit(0)
        return False

    path_str = args.path
    path = Path(path_str)
    
    if not path.exists():
        incorrect_usage_header(BrLogs.error)
        BrLogs.error("Given gif path yielded no results")
        BrLogs.error(f"{BrLogs.GREY}path: \"{BrLogs.YELLOW}{path_str}{BrLogs.GREY}\"")
        print_line()
        return

    return args
