from typing import List

from task import Task
import os
import json
from mapper import TaskMapper


class TaskRepository:
  file_name = 'tasks.json'
  def add(self, task: Task):
    list_of_tasks = self.__read_from_file()
    json_list = self.__add_task_info(list_of_tasks, task)
    self.__write_to_file(json_list)


  def get(self) -> List[Task]:
     saved_info = self.__read_from_file()
     tasks = [TaskMapper.to_object(info) for info in saved_info]
     return tasks


  def delete(self, task:Task):
    list_of_tasks = self.__read_from_file()
    tasks = [x for x in list_of_tasks if x['name'] != task.name]
    self.__write_to_file(tasks)


  def __add_task_info(self, list_of_tasks, task):
    # extract the info from the Task object
    list_of_tasks.append(TaskMapper.to_dict(task))

    return list_of_tasks

  def __write_to_file(self, list_of_tasks):
    # create a JSON
    file_content = json.dumps(list_of_tasks)
    # open the file for writing, create it if it does not exist
    file = open(self.file_name, 'w')
    # save it to the file
    file.write(file_content)
    file.close()

  def __read_from_file(self):
    # check if file was created
    if os.path.exists(self.file_name):
      # open the file for read
      file = open(self.file_name)
      # read and decode the file
      list_of_tasks = json.loads(file.read())
      file.close()
    else:
      # if no file => we have an empty list (no tasks were added)
      list_of_tasks = []
    return list_of_tasks


if __name__ == "__main__":
  task2 = Task('buy fruits', 'eating', difficulty=2)
  repo = TaskRepository()
  repo.delete(task2)
  tasks = repo.get()
  print(tasks)
