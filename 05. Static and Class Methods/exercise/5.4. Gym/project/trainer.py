class Trainer:
    ID = 1

    def __init__(self, name: str):
        self.id = self.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        result = Trainer.ID
        Trainer.ID += 1
        return result

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'
