import sys
from pathlib import Path

from program.params import handle_args
from program.prints.debug import BrLogs
from program.prints.header import print_header
from program.gif.handling import handle_gif
from program.generator.handler import handle_generator
from program.saver.path_getters import get_appdata, get_save_folder
from program.saver.handler import handle_saving

def main(argv = None):
    print_header()
    args = handle_args(args=argv)

    path = Path(sys.argv[1])

    BrLogs.new_step("Anymaker data gathering")
    appdata = get_appdata()
    save_folder = get_save_folder(appdata)

    BrLogs.success("Arguments validated")

    width, height, frames = handle_gif(args)
    data, meta = handle_generator(width, height, frames, args)
    handle_saving(data, meta, save_folder)

if __name__ == "__main__":
    main()