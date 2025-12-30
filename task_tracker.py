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

from datetime import datetime
from pathlib import Path

### UTILS ###
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

    mark_parser = subparsers.add_parser('mark', help='mark help')
    mark_parser.add_argument('id', type=int, help='id help')
    mark_parser.add_argument('status', choices=status_choices, help='status help')

    update_parser = subparsers.add_parser('update', help='update help')
    update_parser.add_argument('id', type=int, help='id help')
    update_parser.add_argument('--title', type=str, help='title help')
    update_parser.add_argument('--description', type=str, help='description help')

    list_parser = subparsers.add_parser('list', help='list help')
    list_choices = status_choices + ['all']
    list_parser.add_argument('status', type=str, nargs='?', default='all', choices=list_choices, help='list status help')

    return parser.parse_args()


def open_json_file(path, op='r', data=None):
    if op == 'r':
        with open(path, op) as f:
            json_file = json.load(f)
        return json_file
    if op == 'w' and data:
        with open(path, op) as f:
            json.dump(data, f, indent=4)

### END UTILS ###

def add_task(task_file, title, description, status='todo'):
    '''
    Add a new task to the json file
    
    :param task: title
    :param task: description
    :param task: status
   '''

    task_json = open_json_file(task_file, op='r')

    task_id = len(task_json['tasks']) + 1
    ## ensure add a new task with new id, description, status - default "todo"

    created_time = datetime.now()
    time_format = '%Y-%m-%d %H:%M:%S'
    new_task = {
        'id': task_id,
        'title': title,
        'description': description,
        'status': status,
        'created_at': created_time.strftime(time_format)
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
        output = f'| {id} |\t| {title} |\t| {status} |'

        print('----------------------------------------')
        if list_option == 'all':
            print(output)
        elif status == list_option:
            print(output)
        else: 
            continue
    print('----------------------------------------')
    return True


def mark_task(task_file, task_id, status):

    task_json = open_json_file(task_file, op='r')

    for tasks in task_json['tasks']:
        if tasks['id'] == task_id:
            tasks['status'] = status
    
    open_json_file(task_file, op='w', data=task_json)

    return task_json


def update_task(task_file, task_id, title, description):
    updated_time = datetime.now()
    time_format = '%Y-%m-%d %H:%M:%S'
    task_json = open_json_file(task_file, op='r')

    for tasks in task_json['tasks']:
        if task_id == tasks['id']:
            pre_update = tasks
            print(f'Pre Update task: {pre_update}')
            if title:
                tasks['title'] = title
            if description:
                tasks['description'] = description
            tasks['updated_at'] = updated_time.strftime(time_format)
            print(f'Updated task #{tasks["id"]}: {tasks}')
    

def delete_task(task_file, task_id):
    print('Not Implemented')



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
    
    if args.command == 'update':
        update_task(task_file, args.id, args.title, args.description)

    if args.command == 'list':
        list_tasks(task_file, args.status)

    if args.command == 'mark':
        mark_task(task_file, task_id=args.id, status=args.status)
    
    if args.command == 'delete':
        delete_task(task_file, task_id=args.id)



if __name__ == '__main__':
    main()