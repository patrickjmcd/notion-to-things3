import os
import webbrowser
import urllib.parse
from dotenv import load_dotenv

from tasks_from_notion import get_notion_tasks
from tasks_from_things import get_things_tasks

load_dotenv()

THINGS_AUTH_TOKEN = os.environ['THINGS_AUTH_TOKEN']


def check_task_status(notion_task, things_task):
    if notion_task.title == things_task.title:
        if notion_task.status_things != things_task.status_things:
            return 'update'
        return 'nothing'
    return False


def update_task_status(notion_task, id):
    print("Updating task: {}".format(notion_task))
    completed = notion_task.status_things == 3
    webbrowser.open(
        "things:///update?id={}&completed={}&auth-token={}".format(id, str(completed).lower(), THINGS_AUTH_TOKEN))


def create_task(notion_task):
    print("Creating task: {}".format(notion_task))
    title = urllib.parse.quote(notion_task.title)
    completed = notion_task.status_things == 3
    webbrowser.open(
        "things:///add?title={}&completed={}&tags=notion".format(title, str(completed).lower()))


def main():
    things_tasks = get_things_tasks()
    notion_tasks = get_notion_tasks()

    for nt in notion_tasks:
        operation = 'create'
        update_id = ""
        for tt in things_tasks:
            task_operation = check_task_status(nt, tt)
            if task_operation:
                operation = task_operation
                update_id = tt.things_id

        if operation == 'create':
            create_task(nt)
        elif operation == 'update':
            update_task_status(nt, update_id)


if __name__ == '__main__':
    main()
