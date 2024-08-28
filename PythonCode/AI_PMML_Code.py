from pypmml import Model
from timeit import default_timer as timer

# Load the PMML model
model = Model.fromFile("classifier11.pmml")

# Define the input parameters for prediction
input_params = {
    "HR": 124,
    "Pulse": 76,
    "SpO2": 100,
    "etCO2": 10,
    "NBP (Sys)": 100,
    "NBP (Dia)": 61,
    "ART (Sys)": 124,
    "ART (Dia)": 76,
    "Temp": 35.9,
    "BIS": 43,
    "Minute Volume Exp (Spiro)": 5,
    "ECG": -0.015
}

# Start timer
start_time = timer()

# Make predictions using the PMML model with the input parameters
predictions = model.predict(input_params)

# Extract the probability of the 'N/A' class from the predictions
probability_na = predictions.get('probability(N/A)', 'N/A')

# End timer
end_time = timer()

# Calculate time difference
execution_time = end_time - start_time

# Print results
print(f"Start Time: {start_time}")
print(f"End Time: {end_time}")
print(f"Execution Time (seconds): {execution_time}")
print(f"Predictions: {predictions}")
print(f"Probability of N/A: {probability_na}")
