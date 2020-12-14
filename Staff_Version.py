import Student_Version
from termcolor import cprint
import time


def staff_version_horizontal(version):
    """ intro for staff version
    which prints a horizontal histogram
    """
    print("---------------------------------------------------------")
    word = "Staff Version with Histogram"
    for i in word:
        cprint(i, "blue", end="")
        time.sleep(0.05)
    print()
    staff_input_data(version)


# ---------------------------------------------------------------------------------


def staff_version_vertical(version):
    """ intro for staff version
    which prints a vertical histogram
    """
    print("---------------------------------------------------------")
    word = "Staff Version with Vertical Histogram"
    for i in word:
        cprint(i, "blue", end="")
        time.sleep(0.05)
    print()
    staff_input_data(version)


# ------------------------------------------------------------------------


# printing progressions as in Part 3
def printing_list_horizontal(outcomes):
    """ prints a horizontal
    histogram
    """
    print()
    print(f"Progress  {outcomes[0]}  : {'*'*outcomes[0]}")
    print(f"Trailer   {outcomes[1]}  : {'*'*outcomes[1]}")
    print(f"Retriever {outcomes[2]}  : {'*'*outcomes[2]}")
    print(f"Excluded  {outcomes[3]}  : {'*'*outcomes[3]}")

# --------------------------------------------------------------------------------


# printing progression as in Past 4
def printing_list_vertical(outcomes):
    """ prints a vertical
    histogram
    """
    print()

    # printing names of types
    list_no = 0
    for i in ["Progress", "Trailing", "Retriever", "Excluded"]:
        print(f"{i} {outcomes[list_no]} | ", end="  ")
        list_no += 1

    # printing stars
    number = 1  # calculating 1 to until end the programme
    while True:
        space = 0  # calculating number of spaces prints
        print()

        # check the values in progressions
        for value in outcomes:
            if value >= number:
                print("     *", end="         ")
            else:
                print("      ", end="         ")
                space += 1  # in any progression type if space is printed

        number += 1  # number increment

        # if space = 4 in any run in the loop,break
        if space == 4:  # break the loop after knowing all are empty
            break

# ------------------------------------------------------------------------------


def staff_input_data(version):
    """ getting multiple inputs of many number of students,
    and printing it as a vertical or horizontal histogram
    according to the version number (2/3)
    """
    count = 1

    # inputting students data
    while True:
        print()

        # getting no of students progressions
        outcomes = Student_Version.input_student_progression()

        enter = ""
        while enter != "q" and enter != "y":  # validating the input
            enter = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            try:
                Student_Version.exit_program(int(enter))
            except ValueError:
                print()

        if enter == "q":
            break
        elif enter == "y":
            count += 1  # calculating no of students
            continue

    # print progressions  according to the version selected
    if version == 2:
        printing_list_horizontal(outcomes)
    elif version == 3:
        printing_list_vertical(outcomes)

    # printing no of outcomes
    print("\n", f"{count} outcomes in total.")
    print("---------------------------------------------------------")
