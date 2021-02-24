import sqlite3
from typing import List

from database.task_store import TaskStore



class TaskStoreSql(TaskStore):
    def get_all(self) -> List[dict]:
        connection = self.__get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        connection.close()
        dict = [{'name': x[0], 'type': x[1]} for x in tasks]
        return dict

    def __get_connection(self):
        connection = sqlite3.connect('database/Tasksdb.db')
        return connection

    def add(self, task_info: dict):
        # open the connection to the DB
        connection = self.__get_connection()
        cursor = connection.cursor()
        # on the cursor object  we execute our commands
        # command = "INSERT INTO tasks (name,type) VALUES ('" + task_info['name'] + "', '" + task_info['type'] + "')"
        #command = "INSERT INTO tasks (name,type) VALUES ('%s', '%s')" \
        #          % (task_info['name'], task_info['type'])
        name = task_info['name']
        task_type = task_info['type']
        command = f"INSERT INTO tasks (name,type) VALUES ('{name}','{task_type}')"

        cursor.execute(command)

        # save and close connection
        connection.commit()
        connection.close()

    def delete(self, task_name: str):
        # the variable after as takes the value form the function on the left
        # with calls connections.close() automatically even if errors
        with self.__get_connection() as connection:
            cursor = connection.cursor()
            command = f"DELETE FROM tasks WHERE name '{task_name}'"
            cursor.execute(command)
            connection.commit()

#