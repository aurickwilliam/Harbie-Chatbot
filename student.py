import database

records = database.Student_Record()

class Student:
    def __init__(self):
        running = True

        while running:
            std_info = self.get_credentials()
            
            has_records = records.check_student(std_info=std_info)
            go_back = False

            if not has_records:
                print("\nHarbie : Can't find you records...")
                while True:
                    print("\nHarbie : Do you want to go back(yes/no)?\n")
                    choice = input("Scholar: ").upper()

                    if choice != "YES" and choice != "NO":
                        print("\nHarbie : Sorry I can't understand that...\n")
                        continue
                    elif choice == "YES":
                        go_back = True
                        running = False
                        print("\n+------------------------------------------------------+\n")
                    elif choice == "NO":
                        running = True
                    break
                continue
            break

        if not go_back:
            self.student_services(std_no=std_info["std_no"])


    def student_services(self, std_no: int):
        running = True

        while running:            
            service = self.menu_services()
            info = records.get_student_info(std_no=std_no)
            print("\n+------------------------------------------------------+\n")
            match service:
                case 1:
                    self.view_info(records=info)
                case 2:
                    self.check_attendance(records=info)
                case 3:
                    self.check_tuition(records=info)
                case 0:
                    running = False

    
    def menu_services(self) -> int:
        print("\n+------------------------------------------------------+\n")

        print("Harbie : Here are the Student Services:")
        print("	 1 -> View Information")
        print("	 2 -> Check Attendance")
        print("	 3 -> Check Tuition Fee Balance")
        print("	 0 -> Go Back\n")

        while True:
            try:
                service_choice = int(input("Scholar: "))

                if service_choice > 3 or service_choice < 0:
                    print("\nHarbie : Please select from the choices...\n")
                    continue

                break
            except (TypeError, ValueError) as ex:
                print("\nHarbie : Sorry I can't understand that...\n")

        return service_choice

    
    def get_credentials(self) -> dict:
        print("\n+------------------------------------------------------+\n")
        print("Harbie : Please fill-up the information:")
        print("	 Enter your first name:\n")

        while True:
            fname = input("Scholar: ")

            if not fname or fname.isspace():
                print("\nHarbie : Sorry I can't understand that...\n")
                continue

            break
        
        print("\nHarbie : Enter your last name:\n")

        while True:
            lname = input("Scholar: ")

            if not lname or lname.isspace():
                print("\nHarbie : Sorry I can't understand that...\n")
                continue

            break

        print("\nHarbie : Enter your Student Number(ex. 2000XXXXXX):\n")

        while True:
            try:
                std_no = int(input("Scholar: "))

                if len(str(std_no)) < 10 or len(str(std_no)) > 10:
                    print("\nHarbie : Invalid Student Number...\n")
                    continue
                
                if not str(std_no)[:4] == '2000':
                    print("\nHarbie : Invalid Student Number...\n")
                    continue

                break
            except (ValueError, TypeError) as ex:
                print("\nHarbie : Sorry I can't understand that...\n")

        std_info = {
            "fname": fname.upper(),
            "lname": lname.upper(),
            "std_no": std_no
        }

        return std_info
    

    def view_info(self, records):
        no = records[0]
        name = records[1] + " " + records[2]
        age = records[3]
        level = records[4]
        program = records[5]
        gwa = records[10]
        
        print("Harbie : Here are your information Scholar...\n")

        print("+------------------------------------------------------+")
        print("| Information					       |")
        print("+------------------------------------------------------+")
        print(f"| Name: {name.ljust(46)} |")
        print("+------------------------------------------------------+")
        print(f"| Student Number : {str(no).ljust(35)} |")
        print(f"| Age            : {str(age).ljust(35)} |")
        print(f"| Level          : {str(level).ljust(35)} |")
        print(f"| Program        : {program.ljust(35)} |")
        print(f"| GWA            : {str(gwa).ljust(35)} |")
        print("+------------------------------------------------------+\n")


    def check_attendance(self, records):    
        name = records[1] + " " + records[2]
        no_present = records[6]
        no_absent = records[7]

        print("Harbie : Here are your Attendance for this Semester...\n")
        print("+------------------------------------------------------+")
        print(f"| Name: {name.ljust(46)} |")
        print("+------------------------------------------------------+")
        print("| Attendance					       |")
        print("+-------------------------------+----------------------+")
        print(f"| No. of Present		| {str(no_present).ljust(20)} |")
        print(f"| No. of Absent			| {str(no_absent).ljust(20)} |")
        print("+-------------------------------+----------------------+\n")
        

    def check_tuition(self, records):
        name = records[1] + " " + records[2]
        total_bal = records[8]
        monthly_bal = records[9]

        print("Harbie : Here are your Tuition Fee Balance ")
        print("	 for this Semester...\n")

        print("+------------------------------------------------------+")
        print(f"| Name: {name.ljust(46)} |")
        print("+------------------------------------------------------+")
        print("| Tution Fee Balance				       |")
        print("+-------------------------------+----------------------+")
        print(f"| Total Balance:		| P {str(total_bal).ljust(18)} |")
        print(f"| Balance for this Month:	| P {str(monthly_bal).ljust(18)} |")
        print("+-------------------------------+----------------------+\n")