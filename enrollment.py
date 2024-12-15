import database, time, random

class Enrollment:
    def __init__(self):
        print("\n+------------------------------------------------------+\n")
        print("Harbie : Oh Hello! Our new Scholar!\n")
        print("Harbie : Are your enrolling for...")
        print("	 1 -> Senior High School")
        print("	 2 -> Tertiary")
        print("	 0 -> Go Back\n")

        while True:
            try:
                level_choice = int(input("Scholar: "))

                if level_choice > 2 or level_choice < 0:
                    print("\nHarbie : Please select from the choices...\n")
                    continue
                
                break
            except (ValueError, TypeError) as ex:
                print("\nHarbie : Sorry I can't understand that...\n")
        
        if level_choice == 0:
            return

        new_student_info = self.get_new_credentials()
        new_student_info["level"] = "Senior High School" if level_choice == 1 else "Tertiary"

        print(f"\nHarbie : Wow!, Nice to meet you {new_student_info["fname"]}")

        program = self.choose_program(new_student_info["level"])

        new_student_info["program"] = program
        new_student_info["student_no"] = self.generate_student_no()

        self.enroll_student(new_student_info)

    def get_new_credentials(self):
        print("\n+------------------------------------------------------+\n")
        print("Harbie : To process your enrollment, let me get your credentials\n")

        print("Harbie : Enter your First Name:\n")
        while True:
            fname = input("Scholar: ")

            if not fname or fname.isspace():
                print("\nHarbie : Sorry I can't understand that...\n")
                continue

            break
        
        print("\nHarbie : Enter your Last Name:\n")
        while True:
            lname = input("Scholar: ")

            if not lname or lname.isspace():
                print("\nHarbie : Sorry I can't understand that...\n")
                continue

            break

        print("\nHarbie : Enter your Age:\n")
        while True:
            try:
                age = int(input("Scholar: "))

                if age <= 0:
                    print("\nHarbie : Invalid Age...\n")
                    continue
                
                break
            except (ValueError, TypeError) as ex:
                print("\nHarbie : Sorry I can't understand that...\n")
        
        student_info = {
            "fname": fname.upper(),
            "lname": lname.upper(),
            "age": age,
        }
        return student_info
        

    def choose_program(self, level: str) -> str:
        courses = ["BSCS", "BSIT", "BSCPE", "BSA", "BMMA", "BSHM", "BSTM"]
        strands = ["STEM", "HUMSS", "ABM", "ICT", "CCT", "CULINARY", "GAS", "DIGITAL ARTS"]

        print("\n+------------------------------------------------------+\n")
        print(f"Harbie : Now what {"course" if level == "Tertiary" else "strand"} do you want to take?")
        
        choices_max = 0

        if level == "Tertiary":
            for i in range(len(courses)):
                print(f"	 {i + 1} -> {courses[i]}")
            choices_max = len(courses)
        elif level == "Senior High School":
            for j in range(len(strands)):
                print(f"	 {j + 1} -> {strands[j]}")
            choices_max = len(strands)
        
        print()

        while True:
            try:
                program = int(input("Scholar: "))

                if program > choices_max or program < 1:
                    print("\nHarbie : Please select from the choices...\n")
                    continue

                break
            except (ValueError, TypeError) as ex:
                print("\nHarbie : Sorry I can't understand that...\n")

        if level == "Tertiary":
            return courses[program - 1]
        else:
            return strands[program - 1]
    

    def generate_student_no(self):
        records = database.Student_Record()

        while True:
            number = random.randint(100000, 999999)
            number = "2000" + str(number)
            if records.check_std_no_exists(number=int(number)):
                continue

            break

        return number

    
    def enroll_student(self, student_info: dict):
        print("\n+------------------------------------------------------+\n")
        print("Harbie : Processing your enrollment...\n")
        time.sleep(5)

        records = database.Student_Record()
        records.insert_student(student_info=student_info)

        name = student_info["fname"] + " " + student_info["lname"]
        
        print(f"\nHarbie : Name: {name}")
        print(f"	 Student No.: {student_info["student_no"]}\n")

        print(f"\nHarbie : Great, you are now enrolled in {student_info["program"]}")
        print("\nHarbie : May I wish you success in your future ")
        print("	 pursuits or endeavors!\n")
