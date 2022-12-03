from math import floor
from project.software.software import Software


class LightSoftware(Software):
    default_type = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.default_type, floor(capacity_consumption * 1.5), floor(memory_consumption * 0.5))
