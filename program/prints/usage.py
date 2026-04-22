from .debug import BrLogs as B

def print_line(print_function=B.note):
    print_function(f"{B.GREY}═════════════════════════════════════════")

def incorrect_usage_header(print_function=B.note):
    """Prints the header of the usage"""
    print_function(f"{B.GREY}{B.YELLOW} ◣◥◣◥◣   {B.BRIGHT_RED}Incorrect script usage!  {B.YELLOW}◥◣◥◣◥  {B.GREY}")
    print_line(print_function)

def print_full_usage(is_error=False):
    function = B.note
    if is_error:
        function = B.error
        incorrect_usage_header(function)

    section_header("Usage", print_function=function)
    function(f"{B.GREY}  encoder.py {B.DIM}<{B.RESET}{B.BRIGHT_BLUE}gif path{B.GREY}{B.DIM}> [{B.RESET}{B.BLUE}options{B.GREY}{B.DIM}]")
    function(f"{B.GREY}┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")
    print_options(print_function=function)

def section_header(name, print_function=B.note):
    print_function(f"▸{B.BRIGHT_CYAN} {name}{B.DIM}:")

def _short(name):
    return f"{B.GREY}[{B.RESET}{B.BOLD}{B.BRIGHT_MAGENTA}{B.DIM}-{B.RESET}{B.BOLD}{B.MAGENTA}{name}{B.RESET}{B.GREY}]{B.RESET}"

def _long(name):
    return f"{B.RESET}{B.BRIGHT_MAGENTA}{B.DIM}--{B.RESET}{B.MAGENTA}{name}{B.RESET}"

def _type(name):
    return f"{B.DIM}{B.BOLD}{B.BRIGHT_GREEN}<{B.RESET}{B.BOLD}{B.BRIGHT_GREEN}{name}{B.DIM}>{B.RESET}"

def _limit(type, amount):
    return f"{B.DIM}{B.BOLD}{B.BRIGHT_YELLOW}<{B.RESET}{B.DIM}{B.YELLOW}{type}{B.BOLD}{B.BRIGHT_YELLOW}>{B.RESET} {B.BLUE}{amount}"

def print_options(print_function=B.note):
    section_header("Miscellaneous", print_function=print_function)
    print_function(f"  {_long('help')}          {B.BLUE}Show this page")

    print_function(f"  {_short('p')}{B.GREY} {_long('path')} {_type('path')}")
    print_function(f"       {B.DIM}{B.BLUE}If the script can't find your Anymaker creation folder")
    print_function(f"       {B.DIM}{B.BLUE}Specify it with this flag")


    print_function("")

    section_header("Resizing", print_function=print_function)
    print_function(f"  {_short('w')}{B.GREY} {_long('width')} {_type('int')}")
    print_function(f"       {B.DIM}{B.BLUE}Stretch / compress the width of the gif, without affecting height")
    print_function(f"       {B.DIM}{B.BLUE}Defaults to original gif width, if not specified")
    print_function(f"       {_limit('min', '1')} {_limit('max', '70')}")

    print_function(f"  {_short('h')}{B.GREY} {_long('height')} {_type('int')}")
    print_function(f"       {B.DIM}{B.BLUE}Stretch / compress the height of the gif, without affecting width")
    print_function(f"       {B.DIM}{B.BLUE}Defaults to original gif height, if not specified")
    print_function(f"       {_limit('min', '1')} {_limit('max', '70')}")

    print_function(f"  {_short('r')}{B.GREY} {_long('ratio')} {_type('float')}")
    print_function(f"       {B.DIM}{B.BLUE}Stretch / compress the gif while keeping its aspect ratio")
    print_function(f"       {B.DIM}{B.BLUE}overwrites {B.MAGENTA}--width{B.BLUE} and {B.MAGENTA}--height")
    print_function(f"       {_limit('min', '> 0')} {_limit('max', '3.0')}")

    print_function("")
    section_header("Gif playback", print_function=print_function)
    print_function(f"  {_short('f')}{B.GREY} {_long('fps')} {_type('int')}")
    print_function(f"       {B.DIM}{B.BLUE}Amount of frames per seconds, Defaults to 60 or gif's default")
    print_function(f"       {_limit('min', '1')} {_limit('max', '60')}")

    print_function(f"  {_short('t')}{B.GREY} {_long('threshold')} {_type('int')}")
    print_function(f"       {B.DIM}{B.BLUE}Amount of light a pixel must emit in the gif in order for")
    print_function(f"       {B.DIM}{B.BLUE}the script to make the corresponding indicator turn on")
    print_function(f"       {B.DIM}{B.BLUE}Defaults to {B.BOLD}128")
    print_function(f"       {_limit('min', '1')} {_limit('max', '255')}")

    print_function(f"  {_short('d')}{B.GREY} {_long('duration')} {_type('int')}")
    print_function(f"       {B.DIM}{B.BLUE}Amount of frames the gif should last for")
    print_function(f"       {B.DIM}{B.BLUE}Defaults to {B.BOLD}gif length")
    print_function(f"       {_limit('min', '1')} {_limit('max', 'gif length')}")

    print_function(f"  {_short('s')}{B.GREY} {_long('skip')} {_type('int')}")
    print_function(f"       {B.DIM}{B.BLUE}Tell the script to skip x amount of frames")
    print_function(f"       {B.DIM}{B.BLUE}if 1, the output gif will keep half the frames")
    print_function(f"       {B.DIM}{B.BLUE}if 2, a frame is skipped every 2 frames")
    print_function(f"       {B.DIM}{B.BLUE}Defaults to {B.BOLD}0")
    print_function(f"       {_limit('min', '0')} {_limit('max', '5')}")


    print_function("")
    section_header("Vehicle", print_function=print_function)
    print_function(f"  {_short('n')}{B.GREY} {_long('name')} {_type('string')}")
    print_function(f"       {B.DIM}{B.BLUE}Give a custom name to the created gif vehicle")
    print_function(f"       {B.DIM}{B.BLUE}Defaults to a {B.BOLD}timestamp")
    print_function(f"       {_limit('min', '1')} {_limit('max', '16 characters')}")
    print_function(f"       {_limit('no special characters', '')}")