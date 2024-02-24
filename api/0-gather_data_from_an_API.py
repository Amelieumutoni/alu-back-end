#!/usr/bin/python3
"""
getting data using api
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_Id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_data_url = "https://jsonplaceholder.typicode.com/users"

    user_response = requests.get(user_data_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Failed to fetch data from API.")
        sys.exit(1)

    todos = todo_response.json()
    users = user_response.json()

    employee_name = None

    for user in users:
        if user.get("id") == employee_Id:
            employee_name = user.get("name")
            break

    if employee_name is None:
        print("Employee ID not found.")
        sys.exit(1)

    # filter completed tasks
    done = []
    total = 0
    completed = 0

    for todo in todos:
        if todo.get("userId") == employee_Id:
            total += 1
            if todo.get("completed"):
                completed += 1
                done.append(todo.get("title"))

    # Display the progress information
    print(f"Employee Name: {employee_name}")
    print(f"Tasks Completed: {completed}/{total}")

    if completed > 0:
        print("Completed Tasks:")
        for idx, task in enumerate(done, 1):
            print(f"Task {idx}: {task}")
    else:
        print("No tasks completed.")

