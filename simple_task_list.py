import json

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(description, priority):
    tasks = load_tasks()
    tasks.append({"description": description, "priority": priority})
    save_tasks(tasks)
    print(f"✅ Task '{description}' added successfully!")

# Remove a task
def remove_task(description):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["description"].lower() != description.lower()]
    save_tasks(tasks)
    print(f"❌ Task '{description}' removed.")

# List all tasks sorted by priority
def list_tasks():
    tasks = load_tasks()
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 4))

    print("\n📌 Your Task List:")
    for i, task in enumerate(sorted_tasks, start=1):
        print(f"{i}. {task['description']} - {task['priority']}")
    print("-" * 40)

# Recommend a high-priority task
def recommend_task():
    tasks = load_tasks()
    high_priority_tasks = [task for task in tasks if task["priority"].lower() == "high"]
    
    if high_priority_tasks:
        print(f"\n🔥 Recommended Task: {high_priority_tasks[0]['description']}")
    else:
        print("\n✅ No high-priority tasks available.")

# Main menu
def main():
    while True:
        print("\n📋 Task Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Recommend Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            add_task(description, priority)
        elif choice == "2":
            description = input("Enter task description to remove: ")
            remove_task(description)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            recommend_task()
        elif choice == "5":
            print("🚀 Exiting Task Manager. Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
