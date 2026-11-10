import sys
import os
import json
from config import MIN_ARGUMENTS_NUMBER
from commands import add

TASK_FILE_PATH = "file.json"

if not os.path.exists(TASK_FILE_PATH):
      with open(TASK_FILE_PATH, 'w', encoding='utf-8') as file:  
            json.dump({}, file)
            
COMMANDS = {"add": add}

arguments = sys.argv[1:]

if len(arguments) < MIN_ARGUMENTS_NUMBER:
  print("given arguments number less than " + 
        f"the min number of arguments ({MIN_ARGUMENTS_NUMBER})", 
        file=sys.stderr)
  sys.exit(1)
  
  
command = arguments[0]
command_args = arguments[1:]

if command not in COMMANDS:
  print(f"there is no such command: {command}" + 
        f"\ncommands available: {", ".join(COMMANDS)}", file=sys.stderr)
  sys.exit(1)


COMMANDS[command](TASK_FILE_PATH, command_args)