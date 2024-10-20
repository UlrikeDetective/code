from datetime import datetime

def add_entry(journal_file, entry):
    with open(journal_file, 'a') as file:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{date}\n{entry}\n\n")

if __name__ == "__main__":
    journal_file = 'trekking_journal.txt'
    while True:
        entry = input("Enter your journal entry: ")
        add_entry(journal_file, entry)
        cont = input("Add another entry? (y/n): ")
        if cont.lower() != 'y':
            break
