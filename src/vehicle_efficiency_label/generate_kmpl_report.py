
import argparse
import logging
import pandas as pd
from tqdm import tqdm

from fastsim import cycle, simdrive

from vehicle_efficiency_label.FastSimVehicleList import FastSimVehicleList


# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Log format
)
logger = logging.getLogger(__name__)

def run():
    parser = argparse.ArgumentParser(description="Generate KMPL report for vehicles")
    parser.add_argument("--input", required=True, help="Input CSV file path")
    parser.add_argument("--output", default="data/vehicles_kmpl_report.csv", help="Output CSV file path")
    args = parser.parse_args()

    print("Loading vehicle list and cycle data...")
    veh_list = FastSimVehicleList(args.input)
    cyc = cycle.Cycle.from_file("data/cycles/udds.csv")

    results = []

    for index, veh in enumerate(tqdm(veh_list, desc="Processing vehicles", unit="vehicle")):
        sim = simdrive.SimDrive(cyc, veh)
        sim.sim_drive()

        veh_name = veh.scenario_name
        kmpl = sim.mpgge * 0.425144  # Convert mpgge to kmpl

        results.append({'index': index, 'name': veh_name, 'kmpl': kmpl})

    output_df = pd.DataFrame(results)
    output_df.to_csv(args.output, index=False)
    print(f"Report saved to: {args.output}")


if __name__ == "__main__":
    run()