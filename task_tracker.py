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
      "task": "Buy groceries",
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

import argparse
import json

from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Raodmap.sh Task Tracker")
    subparsers = parser.add_subparsers(dest='command', help='subcommand help')

    parser.add_argument('--init', action='store_true', help='init help')
    #init_parser = subparsers.add_parser('init', help='init help')

    status_choices = ['todo', 'in-progress', 'done']

    add_parser = subparsers.add_parser('add', help='update help')
    add_parser.add_argument('title', type=str, help='Task title')
    add_parser.add_argument('--description', type=str, help='Task description')
    add_parser.add_argument('--status', type=str, default='todo', choices=status_choices, help='status help')

    delete_parser = subparsers.add_parser('delete', help='update help')
    delete_parser.add_argument('id', type=str, help='Task ID to delete')

    update_parser = subparsers.add_parser('update', help='update help')
    update_parser.add_argument('--id', type=int, help='id help')
    update_parser.add_argument('--status', type=str, choices=status_choices, help='status help')

    list_parser = subparsers.add_parser('list', help='list help')
    list_parser.add_argument('status', type=str, choices=status_choices.append('all'), help='list status help')

    return parser.parse_args()


def add_task(task_file, title, description, status='todo'):
    '''
    Add a new task to the json file
    
    :param task: task
    :param task: status

    add_parser.add_argument('title', type=str, help='Task title')
    add_parser.add_argument('--description', type=str, help='Task description')
    add_parser.add_argument('--status', type=str, default='todo', choices=status_choices, help='status help')
    '''

    task_json = open_json_file(task_file, op='r')

    task_id = len(task_json['tasks']) + 1
    ## ensure add a new task with new id, description, status - default "todo"
    new_task = {'id': task_id,
                'title': title,
                'description': description,
                'status': status
               }
    task_json['tasks'].append(new_task)

    open_json_file(task_file, op='w', data=task_json)


def list_tasks(task_file, list_option="all"):
    
    task_json = open_json_file(task_file)
    for tasks in task_json['tasks']:
        id = tasks['id']
        title = tasks['title']
        status = tasks['status']
        description = tasks['description']

        if list_option == 'all':
            print(f'{id}\t{title}\t{status}')
        elif status == list_option:
            print(f'{id}\t{title}\t{status}')
        else: 
            continue
    return True


def update_task(task_file, task_id, status):

    task_json = open_json_file(task_file, op='r')

    for tasks in task_json['tasks']:
        if tasks['id'] == task_id:
            tasks['status'] = status
    
    open_json_file(task_file, op='w', data=task_json)

    return task_json


def open_json_file(path, op='r', data=None):
    if op == 'r':
        with open(path, op) as f:
            json_file = json.load(f)
        return json_file
    if op == 'w' and data:
        with open(path, op) as f:
            json.dump(data, f, indent=4)


def main():
    args = parse_args()

    task_file_name = 'tasks.json'
    task_file = Path(Path(__file__).parent, task_file_name)

    if args.init:
        if not task_file.exists():
            default_data = {'tasks': []}
            open_json_file(task_file, op='w', data=default_data)
        else:
            print('tasks.json exists, only run on setup')

    if args.command == 'add':
        add_task(task_file, args.title, args.description, args.status)

    if args.command == 'list':
        list_tasks(task_file, args.status)

    if args.command == 'update':
        if not args.status:
            print('Provide a new status with `--status`')
        else:
            update_task(task_file, task_id=args.update, status=args.status)



if __name__ == '__main__':
    main()