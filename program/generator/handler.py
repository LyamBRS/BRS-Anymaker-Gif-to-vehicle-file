from ..prints.debug import BrLogs
from ..generator.grid_generator import generate_grid, generate_meta

def handle_generator(width, height, frames, args):
    BrLogs.new_step("Monitor backwall - data")
    data = generate_grid(frames, width, height, args.fps)

    BrLogs.new_step("Monitor backwall - meta")
    meta = generate_meta(width, height)

    return data, meta