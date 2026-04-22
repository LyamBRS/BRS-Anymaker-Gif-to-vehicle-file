from PIL import Image, ImageSequence
from io import BytesIO
from ..prints.debug import BrLogs

def resize_gif(path, width=None, height=None, aspect_ratio=None, save_path="resized.gif"):
    try:
        with Image.open(path) as img:
            if img.format != "GIF":
                raise ValueError("File is not a GIF")

            # If nothing is specified, just copy original
            if width is None and height is None and aspect_ratio is None:
                output = BytesIO()
                img.save(output, format="GIF")
                output.seek(0)

                if save_path:
                    with open(save_path, "wb") as f:
                        f.write(output.getvalue())

                BrLogs.note("   original gif size unchanged")
                return output, img.width, img.height

            frames = []
            durations = []

            original_width, original_height = img.size

            # Determine target size
            if aspect_ratio is not None:
                BrLogs.info(f"   aspect ratio option specified: {BrLogs.BOLD}{aspect_ratio}")
                target_width = int(original_width * aspect_ratio)
                target_height = int(original_height * aspect_ratio)
            else:
                target_width = width if width is not None else original_width
                target_height = height if height is not None else original_height

            BrLogs.info(
                f"   Resizing gif from: {BrLogs.BOLD}{original_width}x{original_height} "
                f"to {BrLogs.BRIGHT_CYAN}{BrLogs.BOLD}{target_width}x{target_height}"
            )

            # Process frames
            for frame in ImageSequence.Iterator(img):
                frame = frame.convert("RGBA")

                resized = frame.resize(
                    (target_width, target_height),
                    Image.Resampling.NEAREST
                )

                frames.append(resized)
                durations.append(frame.info.get("duration", 100))

            BrLogs.success("   frames resized")

            # Rebuild GIF in memory
            output = BytesIO()
            frames[0].save(
                output,
                format="GIF",
                save_all=True,
                append_images=frames[1:],
                loop=img.info.get("loop", 0),
                duration=durations,
                disposal=2
            )

            output.seek(0)

            if save_path:
                with open(save_path, "wb") as f:
                    f.write(output.getvalue())
                BrLogs.success(f"   Saved resized GIF → {save_path}")

            BrLogs.info(
                f"   Final gif size: {target_width}x{target_height}"
            )

            return output, target_width, target_height

    except Exception as e:
        BrLogs.error(f"Error processing GIF: {e}")
        return None