def student_services():
    student_info = get_credentials()
    print(student_info["name"])
    print(student_info["program"])

    print("\n+------------------------------------------------------+\n")
    print("Harbie : Here are the Student Services:")
    print("\t\t 1 -> View Grades")
    print("\t\t 2 -> Check Attendance")
    print("\t\t 3 -> Check Tuition Fee Balance")
    print("\t\t 4 -> Go Back\n")

    while True:
        try:
            student_services_choice = int(input("Scholar: "))

            if student_services_choice > 4 or student_services_choice < 1:
                print("\nHarbie : Sorry I can't understand that...")
                print("\t\t Please pick from the choices..")
                continue

            break

        except TypeError:
            print("\nHarbie : Sorry I can't understand that...\n")
        except ValueError:
            print("\nHarbie : Sorry I can't understand that...\n")

    match student_services_choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass


def enrollment():
    pass


def general_information():
    pass


def get_credentials():
    student_info = {}

    print("Harbie : Please fill-up the information:")
    print("	 Enter your name:\n")

    while True:
        name = input("Scholar: ")

        if name == '':
            print("\nHarbie : Sorry I can't understand that...\n")
            continue

        student_info["name"] = name
        break

    print("\nHarbie : Enter your Course/Strand(eg. BSCS):\n")
    while True:
        program = input("Scholar: ")

        if program == '':
            print("\nHarbie : Sorry I can't understand that...\n")
            continue

        student_info["program"] = program
        break

    return student_info


def main_menu():
    print("\nHarbie : Good Afternoon, Dear Student! How can I assist")
    print("	 you today?")
    print("	 1 -> Student Services")
    print("	 2 -> Enrollment")
    print("	 3 -> General Information")
    print("	 0 -> Exit\n")

    while True:
        try:
            menu_choice = int(input("Scholar: "))

            if menu_choice > 3 or menu_choice < 0:
                print("\nHarbie : Please select from the choices...\n")
                continue
            break
        except TypeError:
            print("\nHarbie : Sorry I can't understand that...\n")
        except ValueError:
            print("\nHarbie : Sorry I can't understand that...\n")

    return menu_choice


def harbie_chatbot():
    is_running = True

    while is_running:
        choice = main_menu()

        print("\n+------------------------------------------------------+\n")
        match choice:
            case 1:
                student_services()
                break
            case 2:
                enrollment()
                break
            case 3:
                general_information()
                break
            case 0:
                print("\nHarbie : Farewell my Scholar...\n")
                is_running = False


if __name__ == "__main__":
    print("+------------------------------------------------------+")
    print("|						       |")
    print("|		  HARBARD CHATBOT		       |")
    print("|						       |")
    print("+------------------------------------------------------+")
    harbie_chatbot()
