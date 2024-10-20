from datetime import datetime

def add_entry(journal_file, entry):
    with open(journal_file, 'a') as file:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{date}\n{entry}\n\n")

def view_entries(journal_file):
    try:
        with open(journal_file, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Journal file not found. Please add an entry first.")

def edit_entry(journal_file):
    try:
        with open(journal_file, 'r') as file:
            entries = file.readlines()

        # Display entries with indices for editing
        for i in range(0, len(entries), 3):  # 3 lines per entry (date, entry, newline)
            print(f"{i // 3 + 1}: {entries[i].strip()} - {entries[i+1].strip()}")

        # Select the entry to edit
        entry_num = int(input("Enter the number of the entry to edit: "))
        new_entry = input("Enter the new text: ")

        # Replace the old entry with the new one
        entries[(entry_num - 1) * 3 + 1] = f"{new_entry}\n"

        # Write the updated entries back to the file
        with open(journal_file, 'w') as file:
            file.writelines(entries)

        print("Entry updated successfully.")
    except (FileNotFoundError, ValueError, IndexError):
        print("Error editing the entry. Make sure the file exists and the entry number is correct.")

def delete_entry(journal_file):
    try:
        with open(journal_file, 'r') as file:
            entries = file.readlines()

        # Display entries with indices for deleting
        for i in range(0, len(entries), 3):  # 3 lines per entry (date, entry, newline)
            print(f"{i // 3 + 1}: {entries[i].strip()} - {entries[i+1].strip()}")

        # Select the entry to delete
        entry_num = int(input("Enter the number of the entry to delete: "))

        # Remove the selected entry
        del entries[(entry_num - 1) * 3:(entry_num - 1) * 3 + 3]

        # Write the updated entries back to the file
        with open(journal_file, 'w') as file:
            file.writelines(entries)

        print("Entry deleted successfully.")
    except (FileNotFoundError, ValueError, IndexError):
        print("Error deleting the entry. Make sure the file exists and the entry number is correct.")

if __name__ == "__main__":
    journal_file = 'trekking_journal.txt'
    while True:
        print("\nOptions:")
        print("1. Add a new entry")
        print("2. View all entries")
        print("3. Edit an entry")
        print("4. Delete an entry")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            entry = input("Enter your journal entry: ")
            add_entry(journal_file, entry)
        elif choice == '2':
            view_entries(journal_file)
        elif choice == '3':
            edit_entry(journal_file)
        elif choice == '4':
            delete_entry(journal_file)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose a valid number.")
