from ..prints.debug import BrLogs
from pathlib import Path
import os
import sys
import json
from datetime import datetime

from .save_data import save_files, make_timestamp

def handle_saving(data, meta, save_folder):
    BrLogs.new_step("Generating creation name")
    name = make_timestamp()

    BrLogs.new_step("Saving created monitor")
    save_files(data, meta, save_folder, name)