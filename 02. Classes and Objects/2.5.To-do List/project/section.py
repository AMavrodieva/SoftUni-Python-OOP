class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(task)
        return f'Task {task.details()} is added to the section'

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        initial = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        # remove_counter = 0
        # for task in self.tasks:
        #     if task.completed:
        #         self.tasks.remove(task)
        #         remove_counter += 4.1. Wild Cat Zoo
        return f'Cleared {initial - len(self.tasks)} tasks.'

    def view_section(self):
        result = ""
        result += f'Section {self.name}:\n'
        for task in self.tasks:
            result += task.details() + "\n"
        return result.strip()
