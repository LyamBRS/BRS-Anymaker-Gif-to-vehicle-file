import os
import sys
from pathlib import Path

from ..prints.debug import BrLogs

def get_appdata():
    BrLogs.info("   - Appdata folder")
    if sys.platform == "win32":
        BrLogs.info("   - Windows detected")
        path = os.getenv("APPDATA")
        BrLogs.note(f"      - AppData: {BrLogs.DIM}{path}")
        if not path:
            BrLogs.error("FATAL - appadata folder not found.")
            raise EnvironmentError("APPDATA not found")
        
        path = Path(path)
        if not path.exists():
            BrLogs.error("Obtained app data path does not work")
            return
        return path

    # Linux/macOS fallback
    BrLogs.warning("   - UNTESTED, you're not on windows. Please pull requests if shit dont work")
    return Path.home() / ".local" / "share"


def get_save_folder(appdata, app_name="Anymaker/creations"):
    BrLogs.info("   - Creations folder")
    folder = appdata / app_name
    if not folder.exists():
        BrLogs.error("Could not find your save folder for anymaker")
        BrLogs.warning(f"folder: {folder}")
        return
    BrLogs.note(f"      - AppData: {BrLogs.DIM}{folder}")
    return folder