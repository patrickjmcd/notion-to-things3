import os
import webbrowser
import urllib.parse
from dotenv import load_dotenv

from .tasks_from_notion import get_notion_tasks, update_notion_status
from .tasks_from_things import get_things_tasks, create_things_task, update_things_status

load_dotenv()


def check_task_status(notion_task, things_task):
    if notion_task.title == things_task.title:
        if notion_task.status_things != things_task.status_things:
            if notion_task.last_updated > things_task.last_updated:
                return 'update_things'
            else:
                return 'update_notion'
        return 'nothing'
    return False


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
                if operation == 'update_notion':
                    nt.status_things = tt.status_things

        if operation == 'create':
            create_things_task(nt)
        elif operation == 'update_things':
            update_things_status(nt, update_id)
        elif operation == 'update_notion':
            update_notion_status(nt)


if __name__ == '__main__':
    main()
