import sys
import json
import os
import datetime

def get_help():
        print("TODO: Here we'll provide help with commands")

class TaskTracker:
    
    def __init__(self):
        self.file_path = "tasks.json"
        self.file = None
        self.valid_commands = ['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list_tasks']

    def open_file(self, mode:str):
        '''We don't need full permisions in the file to do every task. This method provides us the possibility to open the file in the right mode for each task'''
        try:
            with open (self.file_path, mode) as f:
                self.file = json.load(f)
        except FileNotFoundError:
            with open (self.file_path, 'w') as f:
                f.write("{}")
                self.file = json.load(f)
    
    def save_file(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.file, f, indent=4)

    def add(self, title:str):
        self.open_file('r+')
        task_id = f"task{len(self.file) + 1}"

        self.file[task_id] = {
            "title": title,
            "status": "To do"
        }
        self.save_file()
        return self.file

    def update_task_numbers(self):
        self.open_file('r+')
        for idx, key in enumerate(list(self.file.keys())):
            self.file[f"task{idx + 1}"] = self.file[key]
            del self.file[key]
        # idx = 0
        # keys_list = list(self.file.keys())
        # while idx < len(keys_list):
        #     self.file[f"task{idx + 1}"] = self.file[keys_list[idx]]
        #     del self.file[keys_list[idx]]
        #     idx += 1
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

    def mark_done(self, id:int):
        self.open_file('r+')
        self.file[f"task{id}"]['status'] = "Done"
        self.save_file()
        return self.file

    def list_tasks(self):
        self.open_file('r')
        return self.file
    
    def main(self):
        command = sys.argv[1]

        if command not in self.valid_commands:
            f'''Wrong command. The app support these:
            {get_help}'''
            return

        if len(sys.argv) == 1:
             get_help()
             return

        if (len(sys.argv) == 2) and (command in self.valid_commands):
            print(f"TODO: Here we'll specify the arguments that the user must provide with that command")
            return
        
        if command in self.valid_commands:
            if command == 'add':
                self.add(sys.argv[2])
            elif command == 'delete':
                self.delete(sys.argv[2])
            elif command == 'mark-in-progress':
                self.mark_in_progress(sys.argv[2])
            elif command == 'mark-done':
                self.mark_done(sys.argv[2])
            elif command == 'list_tasks':
                self.list_tasks()

if __name__ == '__main__':
    app = TaskTracker()
    # app.main()
    app.add('Hola')
    app.add('Hola')
    app.delete(2)
    # app.add('Complete the add method')