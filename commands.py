import json
import status
from datetime import datetime

def add(task_file_path: str,
        arguments: list) -> None:
  
  with open(task_file_path, 'r', encoding='utf-8') as file:
    tasks_added = json.load(file)
    ids = [int(id_str) for id_str in tasks_added.keys()]
    if len(ids) == 0:
      ids = [0]
    new_id = max(ids) + 1
    tasks_added[new_id] = {"id": new_id,
                                 "description": arguments[0],
                                 "status": status.TODO,
                                 "createdAt": datetime.now().astimezone().isoformat(),
                                 "updatedAt": datetime.now().astimezone().isoformat()
                                 }
    
  with open(task_file_path, 'w', encoding='utf-8') as file:
    json.dump(tasks_added, file)
  print(f"Task added successfully! (ID: {(new_id)})")