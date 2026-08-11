print("__________________) Cat Library Management System (__________________")
print(r"""
                   _____       _     _     _ _                          
            /  __ \     | |   | |   (_) |                         
            | /  \/ __ _| |_  | |    _| |__  _ __ __ _ _ __ _   _ 
            | |    / _` | __| | |   | | '_ \| '__/ _` | '__| | | |
            | \__/\ (_| | |_  | |___| | |_) | | | (_| | |  | |_| |
             \____/\__,_|\__| \_____/_|_.__/|_|  \__,_|_|   \__, |
                                                             __/ |
                                                            |___/ 
      """)
print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣤⡤⣤⡀⠀⠀⠀⠀⠀⠀⠀
...
""")

# Current Books Available In Cat University Library
books = {
    1: {"title": "Catching Fire", "overdue_fine_each_day":5},
    2: {"title": "The Witness", "overdue_fine_each_day": 4},
    3: {"title": "Just Listen", "overdue_fine_each_day": 2},
    4: {"title": "Atomic Habits", "overdue_fine_each_day": 2},
    5: {"title": "Divergent", "overdue_fine_each_day": 5},
}

# Will use to keep a record of the books borrowed by students
borrowing_record = []

# Display Main Menu Function
def main_menu():
    while True:
        print("\nWelcome To the Main Menu!\nOptions:")
        print("1. Book Borrowing")
        print("2. Book Returning")
        print("3. Borrowed Log Viewing")
        print("4. Exit Menu")
        option = input("Please enter your choice: ")

        if option == "1":
            borrowing_books()
        elif option == "2":
            returning_books()
        elif option == "3":
            viewing_logs()
        elif option == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#
def show_available_books():
    print("\nBooks Currently Available:")
    for book_id, book_details in books.items():
        print(f"ID no:{book_id}, Title: {book_details['title']}, Overdue Fine for each Day: ${book_details['overdue_fine_each_day']}")


# Staff Member can use this function to record books borrowed by students
def borrowing_books():
    show_available_books()
    book_id = int(input("\nPlease input the ID of the book borrowed: "))
    student_name = (input("Please enter the student's name: "))
    days_borrowed = int(input("Please enter the number of days this book has been borrowed for: "))
    days_overdue = int(input("Enter overdue days (if not overdue please input '0'): "))
    fine = calculate_overdue_fine(days_overdue, books[book_id]["overdue_fine_each_day"])
    borrowing_record.append({
        "student": student_name,
        "book_id": book_id,
        "book_title": books[book_id]["title"],
        "days_borrowed": days_borrowed,
        "days_overdue": days_overdue,
        "fine": fine
    })
    print(f"\n{student_name} borrowed '{books[book_id]['title']}' for {days_borrowed} days.")
    if days_overdue > 0:
        print(f"Overdue Fine: ${fine}")


# Using formula to calculate overdue fine from stored value and input taken from student
def calculate_overdue_fine(days_overdue, overdue_fine_each_day):
    return days_overdue * overdue_fine_each_day

# Function to return a book
def returning_books():
    if not borrowing_record:
        print("\nNo books in the log to return.")
        return
    print("\nBorrowed Books:")
    for idx, log in enumerate(borrowing_record):
        print(f"{idx + 1}. Student: {log['student']}, Book: {log['book_title']}, Days Borrowed: {log['days_borrowed']}")
    record_id = int(input("\nEnter the record number of the book to return: "))
    if 1 <= record_id <= len(borrowing_record):
        returned_log = borrowing_record.pop(record_id - 1)
        print(f"\n'{returned_log['book_title']}' returned by {returned_log['student']}.")

# Function to view borrowing logs
def viewing_logs():
    print("\nBorrowing Logs:")
    if not borrowing_record:
        print("No records found.")
    for log in borrowing_record:
        print(f"Student: {log['student']}, Book: {log['book_title']}, Days Borrowed: {log['days_borrowed']}, Overdue Days: {log['days_overdue']}, Fine: ${log['fine']}")

# Start the System using main menu
main_menu()

