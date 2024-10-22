#!/usr/bin/python3
import requests
import sys

def todo_of(employee_id):
    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user_list = requests.get("https://jsonplaceholder.typicode.com/users").json()

    user_name = user_list[employee_id]["name"]
    user_id = user_list[employee_id]["id"]

    # Get all tasks for the user
    done = [task for task in todo_list if task["userId"] == user_id]

    # Count total tasks and completed tasks for this user
    total_tasks = len(done)  # Total tasks assigned to this user
    completed_tasks = sum(1 for task in done if task["completed"])  # Count of completed tasks

    if done:
        # Output in the desired format
        print(f"Employee {user_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in done:
            print(f"\t{task['title']}")
    else:
        print(f"Employee {user_name} has no tasks.")


if __name__ == "__main__":
    # Check if an argument was passed
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument.")
    else:
        # Capture the employee ID from command line argument
        employee_id = int(sys.argv[1])  # Convert to integer
        todo_of(employee_id)
