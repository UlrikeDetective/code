class dayLog:
    def __init__(self):
        self.logs = []

    def add_log(self, first, second, third, honorary):
        log = {
            "First good thing": first,
            "Second good thing": second,
            "Third good thing": third,
            "honorary mentions": honorary,
        }
        self.logs.append(log)

    def display_logs(self):
        for idx, log in enumerate(self.logs, start=1):
            print(f"Good things Log #{idx}:")
            for key, value in log.items():
                print(f"{key}: {value}")
            print("\n")


def main():
    good_things_log = goodThings_Log()

    while True:
        print("\nGood Things Log Menu:")
        print("1. Add a new log")
        print("2. Display all logs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            first = input("Enter first good thing: ")
            second = input("Enter second good thing: ")
            third = input("Enter third good thing: ")
            honorary = input("Enter honorary mentions: ")


            good_things_log_log.add_log(first, second, third, honorary)
            print("Log added successfully!")

        elif choice == "2":
            if not good_things_log.logs:
                print("No logs to display.")
            else:
                good_things_log.display_logs()

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()