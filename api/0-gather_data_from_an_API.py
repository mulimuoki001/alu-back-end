import requests

def get_employee_todo_progress(employee_id):
    # Make a GET request to the API endpoint
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        todos = response.json()  # Convert the response to JSON

        # Filter the completed tasks for the employee
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]

        # Display the employee TODO list progress
        print(f"Employee {todos[0]['username']} is done with tasks({len(completed_tasks)}/{len(todos)}):")
        for task in completed_tasks:
            print(f"    {task}")
    else:
        print(f"Error: Failed to retrieve TODO list for employee {employee_id}")

# Example usage
employee_id = 2
get_employee_todo_progress(employee_id)
