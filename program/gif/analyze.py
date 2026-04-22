import sys
from pathlib import Path
from PIL import Image
from ..prints.debug import BrLogs

def analyze_gif(path, duration, fps):
    if fps is None:
        fps = 60

    try:
        with Image.open(path) as img:
            if img.format != "GIF":
                BrLogs.error("Given file isnt a gif. wtf are you doing?")
                return

            width, height = img.size

            # Count frames
            frame_count = 0
            try:
                while True:
                    img.seek(frame_count)
                    frame_count += 1
            except EOFError:
                pass  # End of frames

            if duration is not None:
                if duration > frame_count:
                    BrLogs.error(f"Specified duration ({BrLogs.BOLD}{BrLogs.BRIGHT_RED}{duration}{BrLogs.RED}{BrLogs.NO_BOLD_NO_DIM}) is higher than the total gif length: ({BrLogs.BOLD}{BrLogs.BRIGHT_RED}{frame_count}{BrLogs.RED}{BrLogs.NO_BOLD_NO_DIM})")
                    sys.exit(1)

            BrLogs.info(f"   - {BrLogs.DIM}{BrLogs.BLUE} File:     {BrLogs.RESET}{BrLogs.BLUE}{path.resolve()}")
            BrLogs.info(f"   - {BrLogs.DIM}{BrLogs.BLUE} Width:    {BrLogs.RESET}{BrLogs.BLUE}{width}")
            BrLogs.info(f"   - {BrLogs.DIM}{BrLogs.BLUE} Height:   {BrLogs.RESET}{BrLogs.BLUE}{height}")
            BrLogs.info(f"   - {BrLogs.DIM}{BrLogs.BLUE} Frames:   {BrLogs.RESET}{BrLogs.BLUE}{frame_count}")
            BrLogs.info(f"   - {BrLogs.DIM}{BrLogs.BLUE} Original duration: {BrLogs.RESET}{BrLogs.BLUE}{frame_count/fps} seconds")
            if duration is not None:
                BrLogs.info(f"   - {BrLogs.BOLD}{BrLogs.DIM}{BrLogs.CYAN} New duration: {BrLogs.RESET}{BrLogs.BOLD}{BrLogs.CYAN}{duration/fps} seconds")

            return width, height

    except Exception as e:
        BrLogs.error(f"Error reading file: {e}")


def gif_to_binary_array(gif_input, args, save_path="generated.gif"):
    frames_data = []
    preview_frames = []
    durations = []

    invert = False
    if args.invert is not None:
        invert = True

    threshold = 50
    if args.threshold is not None:
        threshold = int(args.threshold)
    BrLogs.info(
        f"   - {BrLogs.DIM}{BrLogs.BLUE}Gamma threshold for detection: "
        f"{BrLogs.RESET}{BrLogs.BLUE}{BrLogs.BOLD}{threshold}"
    )

    with Image.open(gif_input) as img:
        n_frames = getattr(img, "n_frames", 1)
        count = range(n_frames)
        if args.duration is not None:
            count = range(0, int(args.duration))
            if args.duration > n_frames:
                BrLogs.error(f"Specified duration ({BrLogs.BOLD}{BrLogs.BRIGHT_RED}{args.duration}{BrLogs.RED}{BrLogs.NO_BOLD_NO_DIM}) is higher than the total gif length: ({BrLogs.BOLD}{BrLogs.BRIGHT_RED}{range(n_frames)}{BrLogs.RED}{BrLogs.NO_BOLD_NO_DIM})")
                sys.exit(1)

        total_sum = 0
        total_pixels = 0
        debug_frames = []

        for frame_index in count:
            BrLogs.note(
                f"   - Converting frame: {BrLogs.BRIGHT_CYAN} {frame_index}"
            )

            sys.stdout.write("\033[1A\r")
            sys.stdout.flush()

            img.seek(frame_index)

            gray = img.convert("L")
            width, height = gray.size

            frame_array = []
            debug_frame = []
            preview_img = Image.new("1", (width, height))  # binary image

            for y in range(height):
                row = []
                debug_row = []
                for x in range(width):
                    pixel = gray.getpixel((x, y))
                    if invert:
                        value = 1 if pixel <= threshold else 0
                    else:
                        value = 1 if pixel >= threshold else 0

                    row.append(value)
                    debug_row.append(pixel)

                    total_pixels += pixel
                    total_sum += 1

                    # write pixel to preview image
                    if invert:
                        preview_img.putpixel((x, y), 255 if value == 0 else 0)
                    else:
                        preview_img.putpixel((x, y), 255 if value == 1 else 0)

                debug_frame.append(debug_row)
                frame_array.append(row)

            debug_frames.append(debug_frame)
            frames_data.append(frame_array)
            preview_frames.append(preview_img)

            durations.append(img.info.get("duration", 100))

    print("")
    BrLogs.success("   - Binary frames created")

    BrLogs.info(f"   - {BrLogs.DIM}average threshold is: {BrLogs.NO_BOLD_NO_DIM}{BrLogs.BOLD}{total_pixels/total_sum}")

    if args.debug is not None:
        save_debug_txt("thresholds.txt", debug_frames)
        BrLogs.warning(f"   - {BrLogs.BOLD}DEBUG{BrLogs.NO_BOLD_NO_DIM}{BrLogs.DIM} debug enabled. pixel thresholds exported to: {BrLogs.GREY}thresholds.txt")

    if save_path and preview_frames:
        preview_frames[0].save(
            save_path,
            save_all=True,
            append_images=preview_frames[1:],
            loop=0,
            duration=durations,
            disposal=2
        )
        BrLogs.success(f"   - Preview GIF saved: {BrLogs.DIM}{save_path}")

    return frames_data



## Fuck ass gifs thresholds are annoying as fuck... ugh.
def save_debug_txt(path, frames_debug_data):
    with open(path, "w", encoding="utf-8") as f:
        for fi, frame in enumerate(frames_debug_data):
            f.write(f"FRAME {fi}\n")

            # print(frame)
            for row in frame:
                # print(row)
                f.write(" ".join(f"{px:<3}" for px in row))
                f.write("\n")

            f.write("\n\n")
        f.close()