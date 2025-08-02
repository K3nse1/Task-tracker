import sys
import json

def get_help():
        return '''
        add: add a task to the list. Must specify a string between double quotes

        delete: remove a task from the list. Specify the number of the task as an integer
        
        mark-in-progress: change the task status to in-progress. Specify the number of the task as an integer
        
        mark-done: change the task status to done. Specify the number of the task as an integer
        
        list_tasks: show the whole list of tasks
'''
class TaskTracker:
    
    def __init__(self):
        self.file_path = "tasks.json"
        self.file = None
        self.valid_commands = ['add', 'delete', 'mark-in-progress', 'mark-done', 'list-tasks']

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
        if self.file is None:
            self.open_file('r+')
        new_file = {}
        for idx, key in enumerate(list(self.file.keys())):
            new_file[f"task{idx + 1}"] = self.file[key]
        self.file = new_file
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
        print("\n📋 YOUR TASKS:")
        print("=" * 60)
        
        for task_id, task in self.file.items():
            id_num = task_id.replace('task', '')
            status_emoji = "✅" if task['status'] == "Done" else "🔄" if task['status'] == "In progress" else "⏳"
            
            print(f"{status_emoji} [{id_num}] {task['title']} ({task['status']})")
        
        print("=" * 60)
    
    def main(self):

        try:
            command = sys.argv[1]
        except IndexError:
            print(f'''Please, provide a valid command:\n{get_help()}''')
            return
        
        if command not in self.valid_commands:
            print(f'''Wrong command. The app support these:
            {get_help()}''')
            return

        if len(sys.argv) == 1:
             print(get_help())
             return

        if (len(sys.argv) == 2) and (command in self.valid_commands) and (command != 'list-tasks'):
            print(f"TODO: Here we'll specify the arguments that the user must provide with that command")
            return
        
        if command in self.valid_commands:
            if command == 'add':
                self.add(sys.argv[2])
            elif command == 'delete':
                self.delete(int(sys.argv[2]))
            elif command == 'mark-in-progress':
                self.mark_in_progress(sys.argv[2])
            elif command == 'mark-done':
                self.mark_done(sys.argv[2])
            elif command == 'list-tasks':
                self.list_tasks()

if __name__ == '__main__':
    app = TaskTracker()
    app.main()