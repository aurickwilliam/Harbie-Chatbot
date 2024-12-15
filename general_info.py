class General_Information:
    def menu(self):
        running = True

        while running:
            print("\n+------------------------------------------------------+\n")
            
            print("Harbie : What information do you want to know?")
            print("	 1 -> University's Calendar")
            print("	 2 -> Contact Directory")
            print("	 0 -> Go Back\n")

            while True:
                try:
                    menu_choice = int(input("Scholar: "))

                    if menu_choice > 2 or menu_choice < 0:
                        print("\nHarbie : Please select from the choices...\n")
                        continue
                    break
                except (ValueError, TypeError) as ex:
                    print("\nHarbie : Sorry I can't understand that...\n")
            
            print("\n+------------------------------------------------------+\n")
            match menu_choice:
                case 1:
                    self.display_calender()
                case 2:
                    self.display_contacts()
                case 0:
                    running = False


    def display_calender(self):
        print("\nHarbie : Here are Harbard University Calendar:\n")

        print("+------------------------------------------------------+")
        print("| Harbard University Calendar			       |")
        print("+-------------------------------+----------------------+")
        print("| Finals Examination            | Dec. 14 - 18         |")
        print("| Start of Second Semester	| Jan. 20	       |")
        print("+-------------------------------+----------------------+\n")

    
    def display_contacts(self):
        print("\nHarbie : Here are Harbard University Contacts:\n")
        
        print("+------------------------------------------------------+")
        print("| Harbard University Contacts			       |")
        print("+------------------------+-----------------------------+")
        print("| Admission		 | 0919 123 1234	       |")
        print("| Registrar		 | 0919 123 1234	       |")
        print("| Cashier		 | 0919 123 1234	       |")
        print("| Student Affairs Office | 0919 123 1234	       |")
        print("| MIS			 | 0919 123 1234	       |")
        print("+------------------------+-----------------------------+\n")