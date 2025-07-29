import sys
import json
import os
import datetime

class TaskTracker:
    
    def __init__(self):
        pass
    
    def create_arguments(self):
        sys.argv += ['add', 'edit', 'delete']
    
    def add_command(self, command:str):
        return sys.argv.append(command)
    
    def run_cli(self):
        self.create_arguments()
        return sys.argv

app = TaskTracker()

print(app.run_cli())