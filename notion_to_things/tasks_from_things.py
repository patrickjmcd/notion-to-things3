import sqlite3
import os
from .task import Task
from sys import exit

from dotenv import load_dotenv


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
    for task in cur.execute("SELECT title, status, uuid FROM TMTask"):
        tasks.append(Task(task[0], task[1], task[2]))
    conn.close()
    return tasks


if __name__ == '__main__':
    for t in get_things_tasks():
        print(t)
