import random
import time
import csv

# Function to suggest a random pose
def suggest_pose(poses):
    pose = random.choice(poses)
    print(f"How about trying the {pose} pose next?")
    return pose

# Function to start and track a yoga session
def start_yoga_session(poses, hold_time, session_name):
    completed_poses = []
    start_time = time.time()
    print("\nStarting your yoga session...\n")
    
    for _ in range(len(poses)):
        pose = suggest_pose(poses)
        completed_poses.append(pose)
        print(f"Holding {pose} for {hold_time} seconds...")
        time.sleep(hold_time)  # Simulate holding the pose
        print(f"{pose} complete!\n")

    # Calculate total session time
    end_time = time.time()
    total_time = end_time - start_time

    # Log session details into a CSV file
    with open('yoga_sessions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([session_name, time.strftime('%Y-%m-%d %H:%M:%S'), ', '.join(completed_poses), f"{total_time:.2f} seconds"])

    print(f"Session '{session_name}' complete! You held {len(completed_poses)} poses in {total_time:.2f} seconds.\n")

# Function to display progress from previous sessions
def show_progress():
    try:
        with open('yoga_sessions.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\nPrevious Yoga Sessions:\n")
            for row in reader:
                print(f"Session: {row[0]} | Date: {row[1]} | Poses: {row[2]} | Total Time: {row[3]}")
            print("\nEnd of session history.\n")
    except FileNotFoundError:
        print("\nNo previous yoga session data found. Start a session first!\n")

# Example usage
if __name__ == "__main__":
    poses = ["Downward Dog", "Warrior II", "Tree Pose", "Child's Pose", "Cobra Pose", "Mountain Pose"]
    hold_time = 10  # Time to hold each pose in seconds

    while True:
        print("1. Start a Yoga Session")
        print("2. View Past Sessions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            session_name = input("\nEnter a name for your session: ")
            start_yoga_session(poses, hold_time, session_name)
        elif choice == '2':
            show_progress()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
