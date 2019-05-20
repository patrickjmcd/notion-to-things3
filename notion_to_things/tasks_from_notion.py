import os
from dotenv import load_dotenv
from notion.client import NotionClient
from .task import Task

load_dotenv()


def check_task(task, user):
    """Checks to see if the task is assigned to the user."""
    if user in task.assign:
        return True

    elif task.assign == []:
        print("Unassigned Task: {}".format(task.name))


def get_notion_tasks():
    NOTION_TOKEN = os.environ['NOTION_TOKEN']
    notion_task_lists = os.environ['NOTION_TASK_LISTS'].split(",")
    tasks = []
    client = NotionClient(token_v2=NOTION_TOKEN)

    for url in notion_task_lists:
        cv = client.get_collection_view(url)
        for t in cv.collection.get_rows():
            if check_task(t, client.current_user):
                tasks.append(Task(t.name, t.status))

    return tasks


if __name__ == '__main__':
    for t in get_notion_tasks():
        print(t)
