
NOTION_TO_THINGS_STATUS_MAP = {
    None: 0,
    "Not Started": 0,
    "In Progress": 0,
    "Completed": 3
}


class Task(object):
    def __init__(self, title, status="Not Started", things_id=None):
        self.title = title
        if not things_id:
            self.status_things = NOTION_TO_THINGS_STATUS_MAP[status]
        else:
            self.status_things = status
        self.things_id = things_id

    def __repr__(self):
        return "Task()"

    def __str__(self):
        return "things_id={}, title={}, status_things={}".format(self.things_id, self.title, self.status_things)
