import sys
import json
import os
import datetime

class TaskTracker:
    
    def __init__(self):
        self.file_path = "C:/rfp-ai-agent/try/tasks.json"
        self.file = None
        self.valid_commands = ['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list']

    def get_help(self):
            print("TODO: Here we'll provide help with commands")

    def open_file(self, mode:str):
        '''We don't need full permisions in the file to do every task. This method provides us the possibility to open the file in the right mode for each task'''
        with open (self.file_path, mode) as f:
            self.file = json.load(f)
    
    def save_file(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.file, f, indent=4)

    def add(self, title:str):
        self.open_file('r+')
        task_id = f"task{len(self.file) + 1}"
        self.file[task_id] = {
            "id": len(self.file),
            "title": title,
            "status": "To do"
        }
        self.save_file()
        return self.file

    def update_task_numbers(self):
        self.open_file('r+')
        for idx, key in enumerate(self.file.keys()):
            self.file[f"task{idx}"] = self.file[key]
            del self.file[key]
            self.file[f"task{idx}"]['id'] = idx
        return self.file

    def delete(self, id:int):
        self.open_file('r+')
        del self.file[f"task{id}"]
        self.update_task_numbers()
        self.save_file()
        return self.file

    def mark_in_progress(self, id:int):
        self.open_file('r+')
        self.file[f"task{id}"]['status'] = "In progress"
        self.save_file()
        return self.file

    def mark_done(self):
        self.open_file('r+')
        self.file[f"task{id}"]['status'] = "Done"
        self.save_file()
        return self.file

    def list(self):
        self.open_file('r')
        return self.file
    
    def main(self):
        if len(sys.argv) == 1:
             self.get_help()
             return

        if (len(sys.argv) == 2) and (sys.argv[1] in self.valid_commands):
            print(f"TODO: Here we'll specify the arguments that the user must provide with that command")
            return
        
        if sys.argv[1] in self.valid_commands:
            commands = {
                'add': self.add(),
                'delete': self.delete(),
                'update': self.update(),
                'mark-in-progress': self.mark_in_progress(),
                'mark-done': self.mark_done(),
                'list': self.list(),
            }


if __name__ == '__main__':
    app = TaskTracker()
    app.update_ids()
    # app.add('Complete the add method')
    app.delete(3)
