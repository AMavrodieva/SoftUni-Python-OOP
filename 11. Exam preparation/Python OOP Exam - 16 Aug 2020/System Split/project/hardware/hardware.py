from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.available_capacity < software.capacity_consumption or self.available_memory < software.memory_consumption:
            raise Exception(f'Software cannot be installed')
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - sum(s.memory_consumption for s in self.software_components)
    
    @property
    def available_capacity(self):
        return self.capacity - sum(s.capacity_consumption for s in self.software_components)