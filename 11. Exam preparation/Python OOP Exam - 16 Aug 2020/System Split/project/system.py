from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_hardware(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_hardware(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_hardware(hardware_name)
        software = System.find_software(software_name)
        if hardware is None or software is None:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory_software_consumption = sum(s.memory_consumption for s in System._software)
        total_memory_hardware_consumption = sum(h.memory for h in System._hardware)
        total_capacity_software_consumption = sum(s.capacity_consumption for s in System._software)
        total_capacity_hardware = sum(h.capacity for h in System._hardware)

        result = f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {total_memory_software_consumption} / {total_memory_hardware_consumption}
Total Capacity Taken: {total_capacity_software_consumption} / {total_capacity_hardware}"""
        return result

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"""Hardware Component - {hardware.name}
Express Software Components: {len([s for s in hardware.software_components if s.software_type == "Express"])}
Light Software Components: {len([s for s in hardware.software_components if s.software_type == "Light"])}
Memory Usage: {sum(s.memory_consumption for s in hardware.software_components)} / {hardware.memory}
Capacity Usage: {sum(s.capacity_consumption for s in hardware.software_components) } / {hardware.capacity}
Type: {hardware.hardware_type}
Software Components: {", ".join([s.name for s in hardware.software_components]) if len(hardware.software_components) > 0 else 'None'}
"""
        return result.strip()

    @staticmethod
    def find_hardware(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware
        return None

    @staticmethod
    def find_software(software_name):
        for software in System._software:
            if software.name == software_name:
                return software
        return None


