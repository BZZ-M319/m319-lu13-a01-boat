from dataclasses import dataclass


@dataclass
class Boat:
    make: str
    model: str
    year: int
    length: float
    serial_number: str

    def print_infos(self):
        print(
            f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Length: {self.length}, Serial Number: {self.serial_number}')