import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import os
import csv

class MyApp(toga.App):

    def startup(self):
        # Set up the main window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Create a button
        save_button = toga.Button("Save CSV", on_press=self.save_csv)

        # Add the button to the app's layout
        box = toga.Box(children=[save_button], style=Pack(direction=COLUMN, padding=10))
        self.main_window.content = box

        # Show the window
        self.main_window.show()

    def save_csv(self, widget):
        # CSV data to save
        data = [
            ['Name', 'Age', 'City'],
            ['Alice', '24', 'New York'],
            ['Bob', '30', 'Los Angeles'],
        ]

        # Path to save the CSV file (Downloads folder)
        csv_filename = "user_data.csv"
        save_path = os.path.join(os.path.expanduser('~'), 'Downloads', csv_filename)

        # Write the CSV data
        with open(save_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        # Display a message to the user
        self.main_window.info_dialog("Success", f"CSV file saved to: {save_path}")

def main():
    return MyApp()

if __name__ == '__main__':
    main().main_loop()
