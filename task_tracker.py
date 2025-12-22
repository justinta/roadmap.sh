'''
Task tracker project from https://roadmap.sh/projects/task-tracker

Requirements:
  - Run from cli
  - add, update, delete tasks
  - mark tasks complete
  - list all tasks
  - list completed tasks
  - list not completed tasks
  - list pending tasks

use a json file to store tasks
for better, use a db. but stretch goals. 

ex. 
{
  "tasks": [
    {
      "id": 1,
      "description": "Buy groceries",
      "status": "todo"  # possible values: todo, in-progress, done
    },
   ]
}


CLI examples

# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
'''


