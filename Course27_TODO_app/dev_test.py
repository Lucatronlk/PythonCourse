from database.task_store_sql import TaskStoreSql


if __name__  == "__main__":
     store = TaskStoreSql()
     store.delete("test")