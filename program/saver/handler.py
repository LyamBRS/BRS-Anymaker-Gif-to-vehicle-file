from ..prints.debug import BrLogs
from datetime import datetime

from .save_data import save_files, make_timestamp

def handle_saving(data, meta, save_folder, args):
    BrLogs.new_step("Generating creation name")
    if args.name is None:
        name = make_timestamp()
    else:
        BrLogs.info(f"   - Custom name was specified: {BrLogs.CYAN}{BrLogs.BOLD}{args.name}")
        name = args.name

    BrLogs.new_step("Saving created monitor")
    save_files(data, meta, save_folder, name)