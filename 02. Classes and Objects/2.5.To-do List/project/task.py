class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    # def __str__(self):
    #     return self.name, self.due_date

    def change_name(self, new_name: str):
        if self.name == new_name:
            return f'Name cannot be the same.'
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return f'Date cannot be the same.'
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)
        return

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number < 0 or comment_number >= len(self.comments):
            return f'Cannot find comment.'
        # self.comments.pop(comment_number)
        # self.comments.insert(comment_number, new_comment)
        self.comments[comment_number] = new_comment
        return ", ".join(self.comments)

    def details(self):
        return f'Name: {self.name} - Due Date: {self.due_date}'
