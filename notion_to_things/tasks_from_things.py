import sqlite3
import os
import webbrowser
import urllib
from .task import Task
from sys import exit

from dotenv import load_dotenv

THINGS_AUTH_TOKEN = os.environ['THINGS_AUTH_TOKEN']


def update_things_status(notion_task, id):
    print("Updating task in Things: {}".format(notion_task))
    completed = notion_task.status_things == 3
    webbrowser.open(
        "things:///update?id={}&completed={}&auth-token={}".format(id, str(completed).lower(), THINGS_AUTH_TOKEN))


def create_things_task(notion_task):
    print("Creating task in Things: {}".format(notion_task))
    title = urllib.parse.quote(notion_task.title)
    completed = notion_task.status_things == 3
    webbrowser.open(
        "things:///add?title={}&completed={}&tags=notion".format(title, str(completed).lower()))


def get_things_tasks():
    load_dotenv()
    tasks = []
    SQLITE_DB = os.getenv('THINGS_DB')
    if not SQLITE_DB:
        exit("No value set for THINGS_DB environment variable")
    try:
        conn = sqlite3.connect(SQLITE_DB)
    except sqlite3.OperationalError:
        exit("Unable to open database at {}".format(SQLITE_DB))
    cur = conn.cursor()
    for task in cur.execute("SELECT title, status, uuid, userModificationDate FROM TMTask"):
        tasks.append(Task(task[0], task[1], task[2], task[3]))
    conn.close()
    return tasks


if __name__ == '__main__':
    for t in get_things_tasks():
        print(t)
