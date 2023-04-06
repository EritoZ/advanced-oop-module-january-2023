from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def search_software_or_hardware(name, somewhere):
        return next(filter(lambda x: x.name == name, somewhere))

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)

        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)

        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            found_hardware: Hardware = System.search_software_or_hardware(hardware_name, System._hardware)

        except StopIteration:
            return "Hardware does not exist"

        System.__install_software(name, capacity_consumption, memory_consumption, found_hardware, ExpressSoftware)

    @staticmethod
    def register_light_software(hardware_name, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            found_hardware: Hardware = System.search_software_or_hardware(hardware_name, System._hardware)

        except StopIteration:
            return "Hardware does not exist"

        System.__install_software(name, capacity_consumption, memory_consumption, found_hardware, LightSoftware)

    @staticmethod
    def __install_software(name: str, capacity_consumption: int, memory_consumption: int, hardware_obj: Hardware,
                           class_obj):

        new_software = class_obj(name, capacity_consumption, memory_consumption)

        hardware_obj.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            found_hardware: Hardware = System.search_software_or_hardware(hardware_name, System._hardware)

        except StopIteration:
            return "Some of the components do not exist"

        try:
            found_software: Software = System.search_software_or_hardware(software_name,
                                                                          found_hardware.software_components)

        except StopIteration:
            return "Some of the components do not exist"

        found_hardware.uninstall(found_software)

        System._software.remove(found_software)

    @staticmethod
    def analyze():
        total_memory_used_software = sum(s.memory_consumption for s in System._software)
        total_memory = sum(h.memory for h in System._hardware)
        total_capacity_used_software = sum(s.capacity_consumption for s in System._software)
        total_capacity = sum(h.capacity for h in System._hardware)

        return f'''System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {total_memory_used_software} / {total_memory}
Total Capacity Taken: {total_capacity_used_software} / {total_capacity}'''

    @staticmethod
    def __hardware_component_message(hardware: Hardware):
        names = []
        total_installed_express_software = 0
        total_installed_light_software = 0

        for s in hardware.software_components:
            names.append(s.name)

            if s.__class__.__name__ == 'ExpressSoftware':
                total_installed_express_software += 1

            elif s.__class__.__name__ == 'LightSoftware':
                total_installed_light_software += 1

        return f'''Hardware Component - {hardware.name}
Express Software Components: {total_installed_express_software}
Light Software Components: {total_installed_light_software}
Memory Usage: {abs(hardware.current_memory - hardware.memory)} / {hardware.memory}
Capacity Usage: {abs(hardware.current_capacity - hardware.capacity)} / {hardware.capacity}
Type: {hardware.hardware_type}
Software Components: {', '.join(names) if names else None}'''

    @staticmethod
    def system_split():
        return '\n'.join(System.__hardware_component_message(h) for h in System._hardware)
