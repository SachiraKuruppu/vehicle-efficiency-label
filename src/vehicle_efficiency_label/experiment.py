
import logging

from fastsim import vehicle, cycle, simdrive


# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Log format
)
logger = logging.getLogger(__name__)

def run():
    print("Loading vehicle and cycle data...")
    veh = vehicle.Vehicle.from_vehdb(10)
    veh = vehicle.Vehicle.from_file("data/vehicles.csv", 10)
    cyc = cycle.Cycle.from_file("data/cycles/udds.csv")
    
    print("Loading the drive simulator...")
    sim = simdrive.SimDrive(cyc, veh)

    print("Running the simulation...")
    sim.sim_drive()

    fuel_consumption = sim.mpgge
    print(f'Fuel Consumption: {fuel_consumption} mpgge')

