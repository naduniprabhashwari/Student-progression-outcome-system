import Student_Validation
from termcolor import cprint
import time


def exit_program(inputs):
    """
    exit from the program
    from any part
    """
    if inputs == 5:
        cprint("\n*** Do you really want to exit? ***", "magenta")
        cprint("'/' for yes | any other key to continue", "magenta")
        exit_command = input()
        if exit_command == "/":
            cprint("\nThank you.................", "cyan")
            quit()


def student_version():
    """ intro for
    student version
    """
    print("------------------------------------------------------------")
    word = "Student Version"
    for i in word:
        cprint(i, "blue", end="")
        time.sleep(0.05)
    print()
    outcome = input_student_progression()
    return outcome


# --------------------------------------------------------------------


# Check progression outcomes of a student
def outcomes(credit_list):
    """ checking the progression
    outcome of a students by 3 parameters
    """
    if credit_list[0] >= 100:
        if(credit_list[1] == 0) and (credit_list[2] == 0):
            outcome = "Progress"
        else:
            outcome = "Progress(module trailer)"
    elif credit_list[2] <= 60:
        outcome = "Do not progress – module retriever"
    else:
        outcome = "Exclude"
    return outcome


# -------------------------------------------------------------------

# assigning global variables to 0
progress = trailer = retriever = exclude = 0


def input_student_progression():
    """ getting all 3 inputs by validating each input,
    display the progression for each student,
    calculating total number of students
    and calculating the number of students for each progression type
    """
    global progress, trailer, retriever, exclude

    credit = None
    credit_list = []

    while True:
        credit_list = []
        for name in["Pass", "Defer", "Fail"]:

            while True:
                credit = Student_Validation.data_type_validation(name)
                if credit is None:
                    continue
                else:
                    range_check = Student_Validation.range_validation(credit)
                if range_check:
                    credit_list.append(credit)
                    break
        total = credit_list[0] + credit_list[1] + credit_list[2]
        if total == 120:
            break
        else:
            cprint("Total is incorrect", "magenta")
            continue

    # calling outcomes()
    progression = outcomes(credit_list)
    cprint(progression, "yellow")  # printing progression of the student

    # calculating no of progressions
    if progression == "Progress":
        progress += 1
    elif progression == "Progress(module trailer)":
        trailer += 1
    elif progression == "Do not progress – module retriever":
        retriever += 1
    else:
        exclude += 1

    # returning calculated progressions
    return [progress, trailer, retriever, exclude]

