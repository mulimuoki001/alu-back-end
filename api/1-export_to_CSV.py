#!/usr/bin/python3
"""Module"""

import csv
import requests
import sys


def main():
    if len(sys.argv) < 2:
        print("Please provide an employee id as a command line argument")
        sys.exit(1)
    employee_id = sys.argv[1]

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{employee_id}".format(
            employee_id=employee_id
        )
    )

    if response.status_code == 200:
        data = response.json()
        emp_name = data["name"]
        username = data["username"]
        todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/?userId={employee_id}"
        )
        if todos_response.status_code == 200:
            todos = todos_response.json()
            comp_tasks = [todo["title"] for todo in todos if todo.get("completed")]
            filename = f"{employee_id}.csv"
            # Open the csv file in write mode
            with open(filename, "w", newline="") as file:
                # Create a csv writer object
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)

                # Write the data rows
                for todo in todos:
                    task_status = "True" if todo.get("completed") else "False"
                    task_title = todo.get("title")
                    writer.writerow(
                        [
                            f"{employee_id}",
                            f"{emp_name}",
                            f"{task_status}",
                            f"{task_title}",
                        ]
                    )

        else:
            print(f"Error: Failed for employee {employee_id}")
    else:
        print(f"Error: Failed for employee {employee_id}")


if __name__ == "__main__":
    main()
