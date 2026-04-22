#=====================================================#
# region Debug definitions
#=====================================================#
class BrLogs():
    #region ----------- docstring
    """
        BrLogs
        -----
        This class is responsible for the prints you
        see in the terminal.
    """
    #endregion
    #region ----------- Members
    RED:str = "\033[31m"
    GREEN:str = "\033[32m"
    YELLOW:str = "\033[33m"
    BLUE:str = "\033[34m"
    MAGENTA:str = "\033[35m"
    CYAN:str = "\033[36m"
    GREY:str = "\033[90m"
    RESET:str = "\033[0m"

    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED   = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW= "\033[93m"
    BRIGHT_BLUE  = "\033[94m"
    BRIGHT_MAGENTA="\033[95m"
    BRIGHT_CYAN  = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    DIM = "\033[2m"
    BOLD = "\033[1m"
    NO_BOLD_NO_DIM = "\033[22m"

    current_step:int = 0
    #endregion
    #region ----------- Methods
    # ---------------------------------------------------- Localized stylers
    def bolded(text:str):
        return f"{BrLogs.BOLD}{text}{BrLogs.NO_BOLD_NO_DIM}"

    # ----------------------------------------------------
    def new_step(text:str):
        """
            new_step
            -----
            This function writes an uniform new_step message
            inside the terminal.
        """
        BrLogs.current_step = BrLogs.current_step + 1
        BrLogs.step(text)
    # ----------------------------------------------------
    def line_start(color) -> str:
        return f"{BrLogs.DIM}{BrLogs.GREY}[{color}BRS{BrLogs.GREY}]{BrLogs.RESET}{BrLogs.GREY}:"

    # ----------------------------------------------------
    def error(text:str):
        """
            error
            -----
            This function writes an uniform error message
            inside the terminal.
        """
        print(f"{BrLogs.line_start(BrLogs.BRIGHT_RED)} {BrLogs.RED}{text}{BrLogs.RESET}")
    # ----------------------------------------------------
    def success(text:str=None):
        """
            success
            -------
            This function writes an uniform success message
            inside the terminal.
        """
        if(text == None):
            print(f"{BrLogs.line_start(BrLogs.BRIGHT_GREEN)} {BrLogs.DIM}{BrLogs.GREEN}-=[{BrLogs.RESET}{BrLogs.BRIGHT_GREEN}success{BrLogs.DIM}{BrLogs.GREEN}]=-{BrLogs.RESET}")
        else:
            print(f"{BrLogs.line_start(BrLogs.BRIGHT_GREEN)} {BrLogs.GREEN}{text}{BrLogs.RESET}")
    # ----------------------------------------------------
    def warning(text:str=None):
        """
            warning
            -------
            This function writes an uniform warning message
            inside the terminal.
        """
        if(text == None):
            print(f"{BrLogs.line_start(BrLogs.BRIGHT_YELLOW)} {BrLogs.DIM}{BrLogs.YELLOW}-=[{BrLogs.RESET}{BrLogs.BRIGHT_YELLOW}warning{BrLogs.DIM}{BrLogs.YELLOW}]=-{BrLogs.RESET}")
        else:
            print(f"{BrLogs.line_start(BrLogs.BRIGHT_YELLOW)} {BrLogs.YELLOW}{text}{BrLogs.RESET}")
    # ----------------------------------------------------
    def question(text:str):
        """
            Question
            --------
            This function writes an uniform question message
            inside the terminal.
        """
        print(f"{BrLogs.CYAN}[BRS][QUESTION]:\t {text}{BrLogs.RESET}")
    # ----------------------------------------------------
    def info(text:str):
        """
            Info
            --------
            This function writes unform information message
            inside the terminal.
        """
        print(f"{BrLogs.line_start(BrLogs.BRIGHT_BLUE)} {BrLogs.BLUE}{text}{BrLogs.RESET}")
    # ----------------------------------------------------
    def note(text:str):
        """
            Note
            --------
            This function writes unform note message
            inside the terminal.
        """
        print(f"{BrLogs.line_start(BrLogs.GREY)} {BrLogs.GREY}{text}{BrLogs.RESET}")
    # ----------------------------------------------------
    def step(text:str):
        """
            Note
            --------
            This function writes unform note message
            inside the terminal.
        """
        print(f"{BrLogs.line_start(BrLogs.BRIGHT_MAGENTA)} {BrLogs.GREY}[{BrLogs.MAGENTA}{BrLogs.current_step}{BrLogs.GREY}]: {BrLogs.MAGENTA}{text}{BrLogs.RESET}")
    #endregion
#endregion

def error_Line() -> bool:
    BrLogs.error(f"{BrLogs.GREY}===========================================")
    return False