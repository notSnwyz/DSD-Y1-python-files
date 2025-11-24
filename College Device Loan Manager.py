loans = [ ]

while True:
    option = input("Chose an option:\n1. Add a Loan\n2. View Loans\n3. Search by student ID\n4. Mark Loan as returned\n5. Extend Loan\n6. Delete Loan\n7. Exit\n")
    if option == '1':

        student_id = input("Enter student ID: ")
        device_name = input("Enter device name: ")
        loan_date = input("Enter loan date (DD/MM/YYYY): ")
        return_date = input("Enter return date (DD/MM/YYYY): ")

        loans.append({
            'student_id': student_id,
            'device_name': device_name,
            'loan_date': loan_date,
            'return_date': return_date
        })

        print("Loan added successfully.")

    elif option == '2':

        if not loans:
            print("No loans available.")

        else:
            for loan in loans:
                print(f"Student ID: {loan['student_id']}, Device: {loan['device_name']}, Loan Date: {loan['loan_date']}, Return Date: {loan['return_date']}")
    
    elif option == '3':

        search_id = input("Enter student ID to search: ")
        found = False

        for loan in loans:
            if loan['student_id'] == search_id:
                print(f"Student ID: {loan['student_id']}, Device: {loan['device_name']}, Loan Date: {loan['loan_date']}, Return Date: {loan['return_date']}")
                found = True
        
        if not found:
            print("No loans found for this student ID.")

    elif option == '4':
        search_id = input("Enter student ID to mark loan as returned: ")
        found = False

        for loan in loans:
            if loan['student_id'] == search_id:
                loans.remove(loan)
                print(f"Loan for student ID {search_id} marked as returned.")
                found = True
                break
        
        if not found:
            print("No loans found for this student ID.")
    
    elif option == '5':
        search_id = input("Enter student ID to extend loan: ")
        found = False

        for loan in loans:
            if loan['student_id'] == search_id:
                new_return_date = input("Enter new return date (DD/MM/YYYY): ")
                loan['return_date'] = new_return_date
                print(f"Loan for student ID {search_id} extended to {new_return_date}.")
                found = True
                break
        
        if not found:
            print("No loans found for this student ID.")
    
    elif option == '6':
        search_id = input("Enter student ID to delete loan: ")
        found = False

        for loan in loans:
            if loan['student_id'] == search_id:
                loans.remove(loan)
                print(f"Loan for student ID {search_id} deleted.")
                found = True
                break
        
        if not found:
            print("No loans found for this student ID.")

    elif option == "7":
        break