from dataclasses import dataclass


@dataclass
class Boat:
    """
    Dataclass for a boat
    """
    make: str
    model: str
    year: int
    length: float
    serial_number: str

    def print_infos(self):
        print(
            f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Length: {self.length},'
            f' Serial Number: {self.serial_number}'
        )
