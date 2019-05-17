import sqlite3
import os
from task import Task

from dotenv import load_dotenv

load_dotenv()


def get_things_tasks():
    tasks = []
    SQLITE_DB = os.environ['THINGS_DB']
    conn = sqlite3.connect(SQLITE_DB)
    cur = conn.cursor()
    for task in cur.execute("SELECT title, status, uuid FROM TMTask"):
        tasks.append(Task(task[0], task[1], task[2]))
    conn.close()
    return tasks


if __name__ == '__main__':
    for t in get_things_tasks():
        print(t)
