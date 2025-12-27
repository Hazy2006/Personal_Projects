# To-Do List Manager

A command-line application to manage your daily tasks with persistent storage using JSON.

## Features

- Add tasks with priority levels (high, medium, low)
- View all tasks or only pending tasks
- Mark tasks as completed
- Delete tasks
- Clear all completed tasks
- Data persistence using JSON file storage
- Timestamps for task creation

## Usage

```bash
python todo.py
```

## Example

```
To-Do List Manager
==================================================

Menu:
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. Complete Task
5. Delete Task
6. Clear Completed Tasks
7. Exit

Select option (1-7): 1
Enter task description: Complete Python project
Priority (high/medium/low) [medium]: high
Task added: Complete Python project
```

## Data Storage

Tasks are stored in `tasks.json` in the same directory as the script.
