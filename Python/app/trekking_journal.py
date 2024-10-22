# python -m venv myenv

# source myenv/bin/activate

# python -m pip install toga briefcase

# Run the application - python trekking_journal.py

import toga
from toga.style import Pack, RGB
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime
import os

class JournalApp(toga.App):

    def startup(self):
        # Set up the main window with a custom background color
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Journal Entry Input
        self.entry_box = toga.MultilineTextInput(
            placeholder="Write your journal entry here...", 
            style=Pack(flex=1, padding=(10, 10, 10, 10), background_color="#4682B4")
        )

        # Action Buttons with custom background and text color
        add_button = toga.Button(
            "Add Entry", 
            on_press=self.add_entry, 
            style=Pack(padding=10, width=150, background_color="#EA8212", color="#FFFFFF")
        )
        view_button = toga.Button(
            "View Entries", 
            on_press=self.view_entries, 
            style=Pack(padding=10, width=150, background_color="#11454C", color="#FFFFFF")
        )
        edit_button = toga.Button(
            "Edit Entry", 
            on_press=self.edit_entry, 
            style=Pack(padding=10, width=150, background_color="#0A9195", color="#FFFFFF")
        )
        delete_button = toga.Button(
            "Delete Entry", 
            on_press=self.delete_entry, 
            style=Pack(padding=10, width=150, background_color="#b6cbee", color="#FFFFFF")
        )

        # Arrange buttons in a row with custom alignment
        button_box = toga.Box(
            children=[add_button, view_button, edit_button, delete_button], 
            style=Pack(direction=ROW, alignment=CENTER, padding=10)
        )

        # Add input area and buttons to the main column
        main_box = toga.Box(
            children=[self.entry_box, button_box], 
            style=Pack(direction=COLUMN, padding=10, flex=1, background_color="#64c5a5")
        )

        # Set the main box to the window and show the window
        self.main_window.content = main_box
        self.main_window.show()

    def add_entry(self, widget):
        journal_file = self.get_journal_file_path()
        entry = self.entry_box.value
        if entry.strip():
            with open(journal_file, 'a') as file:
                date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"{date}\n{entry}\n\n")
            self.entry_box.value = ""
            self.main_window.info_dialog("Success", "Journal entry added.")
        else:
            self.main_window.error_dialog("Error", "Please enter some text.")

    def view_entries(self, widget):
        journal_file = self.get_journal_file_path()
        try:
            with open(journal_file, 'r') as file:
                content = file.read()
                self.main_window.info_dialog("Journal Entries", content if content else "No entries found.")
        except FileNotFoundError:
            self.main_window.error_dialog("Error", "No journal entries found.")

    def edit_entry(self, widget):
        self.main_window.info_dialog("Info", "Edit feature not implemented yet.")

    def delete_entry(self, widget):
        self.main_window.info_dialog("Info", "Delete feature not implemented yet.")

    def get_journal_file_path(self):
        folder = '/Users/ulrike_imac_air/'
        os.makedirs(folder, exist_ok=True)  # Ensure the folder exists
        return os.path.join(folder, 'journal.txt')

def main():
    return JournalApp(formal_name="JournalApp", app_id="com.example.journalapp")

if __name__ == "__main__":
    app = main()
    app.main_loop()
