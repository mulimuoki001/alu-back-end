#!/usr/bin/python3
"""MODULE"""


import json
import requests


# Get request to the API endpoint to retrieve employee details
emp_response = requests.get("https://jsonplaceholder.typicode.com/users")

# Use the status code 200 to check if the request was successful
if emp_response.status_code == 200:
    # This code converts the data into a json format
    emp_data = emp_response.json()

    # Used to retrieve the employee name
    all_employees_tasks = {}
    for employee in emp_data:
        employee_id = employee["id"]
        emp_name = employee["name"]

        # Get request to retrieve the TODO list for the employee
        todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )

        # Check if the request was successful (status code 200)
        if todos_response.status_code == 200:
            todos = todos_response.json()

            # This code filters the completed tasks for the employee
            comp_tasks = [
                {
                    "username": emp_name,
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
                for todo in todos
            ]

            all_employees_tasks[employee_id] = comp_tasks
        else:
            print(f"Error: Failed for employee {employee_id}")
        # Export the data to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(all_employees_tasks, file)

    print(f"Data exported to {filename} successfully.")
else:
    print("Error: Failed for employee employee data")
