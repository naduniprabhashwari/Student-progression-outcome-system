import Student_Version
from termcolor import cprint


def data_type_validation(name):
    """ getting pass value from user
    and validating
    """
    try:
        cprint(f"Please enter your credits at {name}:", "green", end=" ")
        credit = int(input())
        Student_Version.exit_program(credit)
        return credit
    except ValueError:
        cprint("Integer required", "magenta")


def range_validation(credit):
    """ checking the range
    of the values which user input
    """
    credit_range = [0, 20, 40, 60, 80, 100, 120]
    if credit not in credit_range:
        cprint("Out of range.", "magenta")
        return False
    else:
        return True

