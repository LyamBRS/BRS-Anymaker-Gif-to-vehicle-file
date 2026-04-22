from ..prints.debug import BrLogs
from pathlib import Path
import os
import sys
import json
from datetime import datetime

def make_timestamp():
    now = datetime.now()
    # Only numbers + underscores
    name = now.strftime("%Y%m%d_%H%M%S_%f")
    BrLogs.info(f" - creation will be named: {BrLogs.BRIGHT_CYAN}{name}")
    return name

def save_files(data_json, meta_json, save_dir, vehicle_name):

    data_path = save_dir / f"{vehicle_name}.data"
    meta_path = save_dir / f"{vehicle_name}.meta"

    with open(data_path, "w") as f:
        json.dump(data_json, f, indent=4)
    BrLogs.success(f" - {data_path}")

    with open(meta_path, "w") as f:
        json.dump(meta_json, f, indent=4)
    BrLogs.success(f" - {meta_path}")

    return data_path, meta_path