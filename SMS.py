# from tabulate import tabulate


def open_file():
    try:
        with open("students.txt", "rt") as students:
            data = students.readlines()
            return data

    except FileNotFoundError:
        print("\n\tFile Not Found! :0")
        return False


def validate_id2(student_id, data):

    if len(student_id) != 4 or not student_id.isdigit():
        return "Invalid ID! ID must be exactly 4 digits."

    if not any(student_id in line for line in data):
        return "Student ID  not exists! Try again."

    return False


def validate_id(student_id, data):

    if len(student_id) != 4 or not student_id.isdigit():
        return "Invalid ID! ID must be exactly 4 digits."

    if any(student_id in line for line in data):
        return "Student ID  not exists! Try again."

    return False


def st_detailf(student_id, name, g_name, books):
    print(f"\n\tStudent ID: {student_id}")
    print(f"\tStudent Name: {name}")
    print(f"\tGuardian Name: {g_name}")
    print(f"\tBorrowed Books: {books}")


def add_student():
    data = open_file()
    while True:
        student_id = input("\n\tEnter the student ID to add or [e] to exit: ").strip()

        if student_id.lower() == "e":
            print("\n\tExiting the menu. ;)")
            break

        validation = validate_id(student_id, data)
        if validation:
            continue

        else:
            name = input("\tEnter the student name: ").strip().capitalize()
            g_name = input("\tEnter the guardian name: ").strip().capitalize()

            while True:
                books = input(
                    "\n\tEnter the number of book(s) or [e] to exit: "
                ).strip()

                if books == "e":
                    print("\n\tExiting the menu. ;)")
                    break

                elif int(books) > 10:
                    print("\n\tCannot borrow more than 10 books! Try again. :0")
                    continue

                elif int(books) < 0:
                    print("\n\tYou haven't borrowed any books yet.")
                    print("\tThat's why you are here to enter your data, right?")
                    print("\tPlease check your input and try again. ;)")
                    continue

                else:
                    with open("students.txt", "at") as students:
                        students.write(f"{student_id},{name},{g_name},{books}\n")

                    print("\nStudent details added successfully! ;)")
                    print("\nAdded Student Details:")
                    st_detailf(student_id, name, g_name, books)
                    break

            break


def update_student():
    print("\nUpdate Menu:")

    data = open_file()

    while True:
        student_id = input(
            "\n\tEnter the Student ID to update or [e] to exit: "
        ).strip()

        if student_id.lower() == "e":
            print("\n\tExiting the menu. ;)")
            break

        validation = validate_id2(student_id, data)
        if validation:
            continue

        else:
            for line in data:
                if f"{student_id}" in line:
                    old_books = int(line.strip().split(",")[3])
                    break

            name = input("\tEnter the Student Name: ").strip().capitalize()
            g_name = input("\tEnter the Guardian Name: ").strip().capitalize()

            print(f"\n\tPreviously borrowed books: {old_books}")
            print(
                "\n\tEnter [+/-] before the number to borrow or to return the book(s)."
            )

            while True:
                books = input(
                    "\n\tEnter the number of book(s) or [e] to exit.: "
                ).strip()
                input_val = books

                if books.lower() == "e":
                    print("\n\tExiting the menu. ;)")
                    break

                elif input_val.lstrip("+-").isdigit():
                    total_books = old_books + int(books)

                    if total_books > 10:
                        print("\n\tCannot borrow more than '10' books! Try Again. :0")
                        print(f"\tCurrent total: {old_books}")
                        continue

                    elif total_books < 0:
                        print(
                            "\n\tCannot return more than borrowed books! Try Again. :0"
                        )
                        print(f"\tCurrent total: {old_books}")
                        continue

                    else:
                        with open("students.txt", "wt") as students:
                            for line in data:
                                if f"{student_id}" in line:
                                    students.write(
                                        f"{student_id},{name},{g_name},{total_books}\n"
                                    )
                                else:
                                    students.write(line)

                        print("\nRecord updated successfully. ;)")
                        print("\nUpdated Student Details:")
                        st_detailf(student_id, name, g_name, books)
                        print(f"\tCurrent number of books: {total_books}")

                        break

                else:
                    print("\n\tInvalid Input! Try again. :0")
                    continue

            break


def list_student():
    print("\nListing Menu:")

    data = open_file()

    while True:
        student_id = input("\n\tEnter the Student ID to list or [e] to exit: ").strip()

        if student_id.lower() == "e":
            print("\n\tExiting the menu. ;)")
            break

        elif (len(student_id) != 4) or (not (student_id.isdigit())):
            print("\n\tInvalid ID! Try again. :0")
            continue

        elif not any(f"{student_id}" in line for line in data):
            print("\n\tStudent ID does not exist! Try again. :0")
            continue

        else:
            for line in data:
                if f"{student_id}" in line:
                    student_id, name, g_name, books = line.strip().split(",")
                    print("\nStudent Details:")
                st_detailf(student_id, name, g_name, books)

                break

            break


def list_all_students():
    print("\nListing all students:\n")

    data = open_file()

    # You can use [A] part if you do not have the "tabulate" library installed.

    # [A]: {
    for line in data:
        student_id, name, g_name, books = line.strip().split(",")
        st_detailf(student_id, name, g_name, books)
    #    }

    #    # [B]: {
    #    headers = ["Student ID", "Student Name", "Guardian Name", "Borrowed Books"]

    #    table = []
    #    for line in data:
    #        student_id, name, g_name, books = line.strip().split(",")
    #        table.append([student_id, name, g_name, books])

    #    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    # }

    print(f"\nTotal number of students: {len(data)}")


def delete_student():
    print("\nDelete Menu:")

    data = open_file()

    while True:
        student_id = input(
            "\n\tEnter the Student ID to delete or [e] to exit: "
        ).strip()

        if student_id.lower() == "e":
            print("\n\tExiting the menu. ;)")
            break

        elif (len(student_id) != 4) or (not (student_id.isdigit())):
            print("\n\tInvalid ID! Try again. :0")
            continue

        elif not any(f"{student_id}" in line for line in data):
            print("\n\tStudent ID does not exist! Try again. :0")
            continue

        else:
            for line in data:
                if f"{student_id}" in line:
                    student_id, name, g_name, book = line.strip().split(",")
                    print("\nStudent Details:")
                st_detailf(student_id, name, g_name, book)

            while True:
                choice = input("\n\tAre you sure? [yes/no]: ")

                if choice.lower() == "yes":

                    updated_data = [
                        line for line in data if f"{student_id}" not in line
                    ]

                    with open("students.txt", "wt") as students:
                        students.writelines(updated_data)

                    print("\n\tStudent record deleted successfully!")
                    break

                elif choice.lower() == "no":
                    print("\n\tExiting the menu. ;)")
                    break

                else:
                    print("\n\tInvlid Input! Try again. :0")
                    continue

            break


def available_ids():
    data = open_file()
    if not data:
        return None

    used_ids = {line.split(",")[0] for line in data}

    print("\n\tAvailable IDs:", end=" ")

    count = 0
    for i in range(10000):
        ids = f"{i:04d}"
        if ids not in used_ids:
            print(f"{ids}", end=",")
            count += 1
            if count == 5:
                break

    if count == 0:
        print("House Full! No IDs available. :0")
    else:
        print(".....")

    return None


def main():
    print("\nWELCOME TO LIBRARY MANAGEMENT SYSTEM")
    print("\n=(Where Students Can Borrow Books!)=")

    while True:
        print("\nMain Menu:")
        print("\n\t[1] Add Student")
        print("\t[2] Update Student")
        print("\t[3] List Student")
        print("\t[4] List All Students")
        print("\t[5] Delete Student")
        print("\t[6] Available IDs")
        print("\t[e] Exit")

        choice = input("\n\tEnter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            list_student()
        elif choice == "4":
            list_all_students()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            available_ids()
        elif choice.lower() == "e":
            print("\nExiting the program. Bye! ;)\n")

            break
        else:
            print("\n\tInvalid Choice! Please try again. :0")


main()
