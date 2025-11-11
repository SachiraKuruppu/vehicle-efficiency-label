import pandas as pd
from typing import Iterator

from fastsim import vehicle


class FastSimVehicleList:
    def __init__(self, filename: str, to_rust: bool = False):
        self.vehdf = pd.read_csv(filename)

        self.to_rust = to_rust
        self.veh_file = filename
    
    @property
    def length(self) -> int:
        return self.end_index

    def get_vehicle(self, vnum: int) -> vehicle.Vehicle:
        return self.from_df(self.vehdf, vnum, self.veh_file, self.to_rust)

    def __iter__(self) -> Iterator[vehicle.Vehicle]:
        self.current_index = 0
        self.end_index = self.vehdf.shape[0]
        return self

    def __next__(self) -> vehicle.Vehicle:
        if self.current_index < self.end_index:
            veh = vehicle.Vehicle.from_df(self.vehdf, self.current_index, self.veh_file, self.to_rust)
            self.current_index += 1
            return veh
        else:
            raise StopIteration
