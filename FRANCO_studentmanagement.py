records = []
savename = None

while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====\n")
    print("[1] Open File")
    print("[2] Save File")
    print("[3] Save As File")
    print("[4] Show All Students Record")
    print("[5] Show Student Record")
    print("[6] Add Record")
    print("[7] Edit Record")
    print("[8] Delete Record")
    print("[9] Exit\n")

    opt = input("Enter option: ")
    print()

    if opt == '1':
        if savename is None:
            print("There is no file.")
        else:
            try:
                with open(savename, 'r') as file:
                    records.clear()
                    for line in file:
                        records.append(tuple(line.strip().split(", "))) #opens the file to load the inputs
                    print("File has been loaded.")
            except:
                print("File error.")

    elif opt == '2':
        if savename is None:
            print("There is no file.")
        else:
            with open(savename, 'w') as file:
                for student in records:
                    file.write(",".join(student) + "\n") #saves the file inputs
            print("Records have been saved.")

    elif opt == '3':
        savename = input("Enter the name of the file: ") #gives the filename and saves it
        with open(savename, 'w') as file:
            for student in records:
                file.write(", ".join(student) + "\n")
        print("Records have been saved.")

    elif opt == '4': 
        print("\n== Select an order of display ==\n")
        print("[1] Order by Last Name")
        print("[2] Order by Grade")

        choose = input("Enter option: ")

        sortedrec = list(records)

        if choose == '1':  #sorting by last name
            for i in range(len(sortedrec)):
                for j in range(len(sortedrec) - 1):
                    name1 = sortedrec[j][2]
                    name2 = sortedrec[j + 1][2]
                    if name1 > name2: #compares the names and switches their place aka bubble sorting
                        sortedrec[j], sortedrec[j + 1] = sortedrec[j + 1], sortedrec[j]

        elif choose == '2':  #sorting by grade
            for i in range(len(sortedrec)):
                for j in range(len(sortedrec) - 1):
                    g1 = (float(sortedrec[j][3]) * 0.6) + (float(sortedrec[j][4]) * 0.4)
                    g2 = (float(sortedrec[j + 1][3]) * 0.6) + (float(sortedrec[j + 1][4]) * 0.4)
                    if g1 < g2: #same logic to sorting by last name using bubble sort
                        sortedrec[j], sortedrec[j + 1] = sortedrec[j + 1], sortedrec[j]

        for stud in sortedrec:
            print("\n" + stud[1] + " " + stud[2])
            print("ID:", stud[0])
            print("Grade:", (float(stud[3]) * 0.6) + (float(stud[4]) * 0.4))
            print()

    elif opt == '5':
        studid = input("Enter Student ID: ")
        found = False
        for stud in records: #cycles through the list of records to find the match
            if stud[0] == studid:
                print("\n=== STUDENT RECORD ===\n")
                print("\n" + stud[1] + " " + stud[2])
                print("ID:", stud[0])
                print("Grade:", (float(stud[3]) * 0.6) + (float(stud[4]) * 0.4))
                found = True
                break
        if not found:
            print("Student not found.")

    elif opt == '6': #adding a record
        print("=== ADD RECORD ===\n")
        studid = input("Enter Student ID (6-digit): ")
        if len(studid) != 6 or not studid.isdigit():
            print("Invalid Student ID. Must be 6 digits.")
        else:
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            standing = input("Enter Class Standing Grade: ")
            major = input("Enter Major Exam Grade: ")
            records.append((studid, fname, lname, standing, major))
            print("Record added successfully.")

    elif opt == '7':  #editing record
        studid = input("Enter Student ID to edit: ")
        found = False
        for i in range(len(records)):
            if records[i][0] == studid:
                print("=== EDIT RECORD ===\n")
                print("You are editing the record of : ", records[i])
                fname = input("Enter First Name (leave blank to keep current): ") or records[i][1] #the or operator makes it so that if the input is blank it will keep the old value
                lname = input("Enter Last Name (leave blank to keep current): ") or records[i][2]
                standing = input("Enter Class Standing Grade (leave blank to keep current): ") or records[i][3]
                major = input("Enter Major Exam Grade (leave blank to keep current): ") or records[i][4]
                records[i] = (studid, fname, lname, standing, major)
                print("Record updated successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif opt == '8':  #delete record
        print("=== DELETE RECORD ===\n")
        studid = input("Enter Student ID to delete: ")
        newrecord = []
        for stud in records:  
            if stud[0] != studid: #if it is not the student then it will be kept back
                newrecord.append(stud)
        if len(newrecord) < len(records):
            records = newrecord
            print("Record deleted successfully.")
        else:
            print("Student not found.")

    elif opt == '9':  # Exit
        print("Exiting...")
        break

    else:
        print("Invalid option. Please try again.")
