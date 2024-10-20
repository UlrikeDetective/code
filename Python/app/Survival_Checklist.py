def add_item(checklist, item):
    checklist.append(item)
    print(f"{item} added to checklist.")

def remove_item(checklist, item):
    if item in checklist:
        checklist.remove(item)
        print(f"{item} removed from checklist.")
    else:
        print(f"{item} not found in checklist.")

def view_checklist(checklist):
    print("Checklist:")
    for item in checklist:
        print(f"- {item}")

if __name__ == "__main__":
    checklist = ['Water', 'Map', 'Compass']
    while True:
        action = input("Choose action (add, remove, view, quit): ").lower()
        if action == "add":
            item = input("Enter item to add: ")
            add_item(checklist, item)
        elif action == "remove":
            item = input("Enter item to remove: ")
            remove_item(checklist, item)
        elif action == "view":
            view_checklist(checklist)
        elif action == "quit":
            break
