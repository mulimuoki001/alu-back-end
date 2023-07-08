#!/usr/bin/python3
"""MODULE"""


import json
import requests
import sys

# checking if the user id is provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide an employee id as a command line argument")
    sys.exit(1)

employee_id = sys.argv[1]

# Get request to the API endpoint to retrieve employee details
emp_response = requests.get(
    "https://jsonplaceholder.typicode.com/users/{employee_id}".format(
        employee_id=employee_id
    )
)

# Use the status code 200 to check if the request was successful
if emp_response.status_code == 200:
    # This code converts the data into a json format
    emp_data = emp_response.json()

    # Used to retrieve the employee name
    emp_name = emp_data["name"]

    # This code makes a Get request to retrieve the TODO list for the employee
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?useId={employee_id}"
    )

    # Check if the request was successful (status code 200)
    if todos_response.status_code == 200:
        todos = todos_response.json()

        # This code filters the completed tasks for the employee
        comp_tasks = [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": emp_name,
            }
            for todo in todos
        ]

        employee_tasks = {employee_id: comp_tasks}

        # Export the data to a JSON file
        filename = f"{employee_id}.json"
        with open(filename, "w") as file:
            json.dump(employee_tasks, file)

        print(f"Data exported to {filename} successfully.")
    else:
        print(f"Error: Failed for employee {employee_id}")
else:
    print(f"Error: Failed for employee {employee_id}")
