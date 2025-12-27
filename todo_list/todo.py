"""
To-Do List Application
A command-line application to manage your daily tasks with persistent storage.
"""

import json
import os
from datetime import datetime


class TodoList:
    """A simple to-do list manager with file persistence."""
    
    def __init__(self, filename="tasks.json"):
        """Initialize the to-do list with a file for persistence."""
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from the JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, description, priority="medium"):
        """Add a new task to the list."""
        # Generate unique ID by finding max ID and adding 1
        max_id = max([task["id"] for task in self.tasks], default=0)
        task = {
            "id": max_id + 1,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")
    
    def view_tasks(self, show_completed=True):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks found!")
            return
        
        print("\n" + "=" * 80)
        print("YOUR TASKS".center(80))
        print("=" * 80)
        
        for task in self.tasks:
            if not show_completed and task["completed"]:
                continue
            
            status = "✓" if task["completed"] else "○"
            priority_symbols = {"high": "!!!", "medium": "!!", "low": "!"}
            priority = priority_symbols.get(task["priority"], "!!")
            
            print(f"\n[{status}] Task #{task['id']} {priority}")
            print(f"    {task['description']}")
            print(f"    Created: {task['created_at']}")
            if task["completed"]:
                print(f"    Status: Completed")
        
        print("\n" + "=" * 80)
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"Task #{task_id} marked as completed!")
                return
        print(f"Task #{task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task from the list."""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task deleted: {deleted_task['description']}")
                return
        print(f"Task #{task_id} not found!")
    
    def clear_completed(self):
        """Remove all completed tasks."""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task["completed"]]
        removed = initial_count - len(self.tasks)
        self.save_tasks()
        print(f"Removed {removed} completed task(s)!")


def main():
    """Main function to run the to-do list application."""
    todo = TodoList()
    
    print("=" * 50)
    print("To-Do List Manager".center(50))
    print("=" * 50)
    
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Clear Completed Tasks")
        print("7. Exit")
        
        choice = input("\nSelect option (1-7): ").strip()
        
        if choice == '7':
            print("Goodbye!")
            break
        
        elif choice == '1':
            description = input("Enter task description: ").strip()
            if description:
                priority = input("Priority (high/medium/low) [medium]: ").strip().lower()
                if priority not in ['high', 'medium', 'low']:
                    priority = 'medium'
                todo.add_task(description, priority)
            else:
                print("Task description cannot be empty!")
        
        elif choice == '2':
            todo.view_tasks(show_completed=True)
        
        elif choice == '3':
            todo.view_tasks(show_completed=False)
        
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Invalid task ID!")
        
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid task ID!")
        
        elif choice == '6':
            confirm = input("Clear all completed tasks? (yes/no): ").strip().lower()
            if confirm == 'yes':
                todo.clear_completed()
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
