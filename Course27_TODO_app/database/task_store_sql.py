import sqlite3
from typing import List

from database.task_store import TaskStore



class TaskStoreSql(TaskStore):
    def get_all(self) -> List[dict]:
        connection = sqlite3.connect('database/Tasksdb.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        connection.close()
        dict = [{'name': x[0], 'type': x[1]} for x in tasks]
        return dict