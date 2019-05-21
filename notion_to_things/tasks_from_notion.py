import os
from dotenv import load_dotenv
from notion.client import NotionClient
from .task import Task

load_dotenv()

THINGS_TO_NOTION_STATUS_MAP = {
    0: "In Progress",
    3: "Completed"
}


def check_task(task, user):
    """Checks to see if the task is assigned to the user."""
    if user in task.assign:
        return True

    elif task.assign == []:
        print("Unassigned Task: {}".format(task.name))


def update_notion_status(things_task):
    """Updates a notion task."""
    print("Updating task in Notion: {}".format(things_task))

    all_tasks = get_all_notion_tasks()
    for t in all_tasks:
        if t.name == things_task.title:
            t.status = THINGS_TO_NOTION_STATUS_MAP[things_task.status_things]


def get_all_notion_tasks():
    """Fetch all notion tasks."""
    NOTION_TOKEN = os.environ['NOTION_TOKEN']
    notion_task_lists = os.environ['NOTION_TASK_LISTS'].split(",")
    tasks = []
    client = NotionClient(token_v2=NOTION_TOKEN)

    for url in notion_task_lists:
        cv = client.get_collection_view(url)
        for t in cv.collection.get_rows():
            tasks.append(t)
    return tasks


def get_notion_tasks():
    NOTION_TOKEN = os.environ['NOTION_TOKEN']
    client = NotionClient(token_v2=NOTION_TOKEN)

    all_tasks = get_all_notion_tasks()
    tasks = []
    for t in all_tasks:
        last_edited_time = float(t.get('last_edited_time')) / 1000
        if check_task(t, client.current_user):
            tasks.append(
                Task(t.name, t.status, last_updated=last_edited_time))
    return tasks


if __name__ == '__main__':
    for t in get_notion_tasks():
        print(t)
