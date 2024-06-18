# Example of how to use the AdmiralWrapper class to run experiments
# with the Admiral potentiostat. This script will run an EIS, CV and CP

# Author: Nis Fisker-Bødker
# Date: 18-06-2024

# Here we define all experiments, get data and then close the connection

from ..src.admiral import AdmiralWrapper

# Initialize the potentiostat
measurement = AdmiralWrapper(port="COM5", instrument_name="Plus1894")

###### Setup EIS potentiostatic experiment ######
measurement.setup_EIS_potentiostatic()
measurement.run_experiment() # Always do this after setup of one or more experiments
ac_data_eis, dc_data_eis = measurement.get_data() # Get data
measurement.clear_data() # Clear data before next experiment

###### Setup CV experiment ######
measurement.setup_cyclic_voltammetry(
    startVoltage=0,
    firstVoltageLimit=0.3,
    secondVoltageLimit=0,
    endVoltage=0,
    scanRate=0.1,
    samplingInterval=0.1,
    cycles=1,
)
measurement.run_experiment()
ac_data_cv, dc_data_cv = measurement.get_data() # Get data

###### Setup CP (constant current) experiment ######
measurement.setup_constant_current(
    holdAtCurrent=0.1, # Amps
    samplingInterval=0.1, # Measurement interval in seconds
    duration=10, # Duration of the experiment in seconds
)
measurement.run_experiment()
ac_data_cp, dc_data_cp = measurement.get_data() # Get data

###### Close connection to potentiostat ######
measurement.close_experiment()

###### Print data ######
print("\n\nEIS data:")
print(ac_data_eis)
print(dc_data_eis) # DC data is not available for EIS

print("\n\nCV data:")
print(ac_data_cv) # AC data is not available for CV
print(dc_data_cv)

print("\n\nCP data:")
print(ac_data_cp) # AC data is not available for CP
print(dc_data_cp)