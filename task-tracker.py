import sys
import json
import os
import datetime

class TaskTracker:
    
    def __init__(self):
        self.filename = 'tasks.json'
        self.valid_commands = ['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list']

    def get_help(self):
            print("TODO: Here we'll provide help with commands")

    def main(self):
        if len(sys.argv) == 1:
             self.get_help()
             return

        if (len(sys.argv) == 2) and (sys.argv[1] in self.valid_commands):
            print(f"TODO: Here we'll specify the arguments that the user must provide with that command")
            return
        



if __name__ == '__main__':
    app = TaskTracker()
    app.main()