class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not len(value.strip()) > 0:
            raise ValueError(f'Planet name cannot be empty string or whitespace!')
        self.__name = value
