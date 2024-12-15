import student, general_info, enrollment

class Main:
    def __init__(self):
        print("+------------------------------------------------------+")
        print("|						       |")
        print("|		   HARBARD CHATBOT		       |")
        print("|						       |")
        print("+------------------------------------------------------+\n")
        self.harbie()


    def main_menu(self) -> int:
        print("Harbie : Good Afternoon, Dear Student! How can I assist")
        print("	 you today?")       
        print("	 1 -> Student Services")       
        print("	 2 -> Enrollment")       
        print("	 3 -> General Information")       
        print("	 0 -> Exit\n")

        while True:
            try:
                choice = int(input("Scholar: "))

                if choice > 3 or choice < 0:
                    print("\nHarbie : Please select from the choices...\n")
                    continue

                break
            except (TypeError, ValueError) as ex:
                print("\nHarbie : Sorry I can't understand that...\n")

        return choice

    
    def harbie(self):
        running = True
        gen_info = general_info.General_Information()

        while running:
            choice = self.main_menu()
            
            match choice:
                case 1:
                    student.Student()
                case 2:
                    enrollment.Enrollment()
                case 3:
                    gen_info.menu()
                case 0:
                    self.exit()
                    running = False
                    break


    def exit(self):
        print("\n+------------------------------------------------------+\n")
        print("Harbie : Farewell, Scholar...\n")


if __name__ == "__main__":
    Main()
