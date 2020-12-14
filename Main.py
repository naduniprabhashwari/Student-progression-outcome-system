# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID(Uow) : 18108086/1
# Student ID(IIT) : 20201224
# Date:  26/12/2020

import time
import Student_Version
import Staff_Version
import Alternative_Staff_Version
from termcolor import cprint

cprint("Welcome!", 'blue')
cprint("Progression Outcomes System", 'blue')
# --------------------------------------------------------------------

# main loop in the system
while True:
    print()
    cprint("------------------------------------------------------------\n", 'blue')
    time.sleep(0.5)

    # show the detail of the versions
    cprint("               Main Menu                    ", "blue")
    time.sleep(0.2)
    cprint("|---|---------------------------------------|", "blue")
    cprint("|No |           Menu of versions            |", "blue")
    cprint("|---|---------------------------------------|", "blue")
    cprint("| 1 | Student Version                       |", "blue")
    cprint("| 2 | Staff Version with Histogram          |", "blue")
    cprint("| 3 | Staff Version with Vertical Histogram |", "blue")
    cprint("| 4 | Alternative Staff Version             |", "blue")
    cprint("| 5 | Quit                                  |", "blue")
    cprint("|---|---------------------------------------|", "blue")
    print()
    time.sleep(0.2)
    cprint("*** Type '5' as any input to exit form anywhere ***", "red")
    print()
    time.sleep(0.5)

    # getting the version which user wants
    try:
        print("Which version do you want to use?")
        version = int(input("Enter the number of the version: "))
    except ValueError:
        cprint("Add the number. Please try again\n", "magenta")
        continue

    # checking the version and run
    if version == 1:
        Student_Version.student_version()

    elif version == 2:
        # making global variables zero
        Student_Version.exclude = Student_Version.progress = Student_Version.retriever = Student_Version.trailer = 0

        Staff_Version.staff_version_horizontal(version)

    elif version == 3:
        # making global variables zero
        Student_Version.exclude = Student_Version.progress = Student_Version.retriever = Student_Version.trailer = 0

        Staff_Version.staff_version_vertical(version)

    elif version == 4:
        Alternative_Staff_Version.alternative_staff_version()

    elif version == 5:
        Student_Version.exit_program(version)

    else:
        cprint("Wrong number. Please try again", "magenta")
