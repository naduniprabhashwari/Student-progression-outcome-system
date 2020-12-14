import Student_Version
import Staff_Version
from termcolor import cprint
import time


def alternative_staff_version():
    """ intro for alternative
    staff version
    """
    print("---------------------------------------------------------")
    word = "Alternative Staff Version"
    for i in word:
        cprint(i, "blue", end="")
        time.sleep(0.05)
    print()
    list_inputs()


def list_inputs():
    """ Take inputs from a two dimensional list
    and check progression types.
    Prints progression types.
    Prints number of students for each progression type
    as a horizontal histogram.
    """
    progress = trailer = retriever = exclude = 0

    # data list of students
    data_list = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 20], [40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]

    # checking the progression type for each inner lists in the data_list
    for outcome in data_list:
        outcomes = Student_Version.outcomes(outcome)
        cprint(outcomes, "yellow")

        # calculating no of progressions
        if outcomes == "Progress":
            progress += 1
        elif outcomes == "Progress(module trailer)":
            trailer += 1
        elif outcomes == "Do not progress – module retriever":
            retriever += 1
        else:
            exclude += 1

    # printing the no of students for each progression in a horizontal histogram
    Staff_Version.printing_list_horizontal([progress, trailer, retriever, exclude])

    # printing number of student's data in the lists
    count = len(data_list)
    print("\n", f"{count} outcomes in total.")

