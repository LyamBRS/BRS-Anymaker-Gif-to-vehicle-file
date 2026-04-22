### First step of the pipeline
from ..prints.debug import BrLogs
from ..gif.analyze import analyze_gif, gif_to_binary_array
from ..gif.sizing import resize_gif

def handle_gif(args):
    path = args.path
    target_width = args.width
    target_height = args.height
    target_aspect_ratio = args.ratio
    duration = args.duration
    fps = args.fps

    BrLogs.new_step("Gif analysis")
    analyze_gif(path, duration, fps)

    BrLogs.new_step("Gif Resizing")
    gif, width, height = resize_gif(path, target_width, target_height, target_aspect_ratio)

    BrLogs.new_step("Binary convertion")
    frames = gif_to_binary_array(gif, args)

    return width, height, frames