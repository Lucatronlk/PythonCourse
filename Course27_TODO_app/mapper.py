from task import Task

class TaskMapper:
    @staticmethod
    def to_dict(task: Task) -> dict:
        return {
      'name': task.name,
      'type': task.task_type,
      'deadline': task.deadline,
      'difficulty': task.difficulty,
    }
