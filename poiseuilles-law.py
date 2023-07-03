# Import necessary libraries
import math

# Function to calculate the flow rate in Poiseuille's Law
def calculate_flow_rate(viscosity, pressure_difference, radius, length):
    # Calculate the flow rate using Poiseuille's Law
    flow_rate = (math.pi * pressure_difference * radius**4) / (8 * viscosity * length)
    return flow_rate

# Inputs required:
fluid_viscosity = 0.001  # Viscosity of the fluid in Pa*s
pressure_difference = 1000.0  # Pressure difference across the pipe in Pa
pipe_radius = 0.1  # Radius of the pipe in meters
pipe_length = 10.0  # Length of the pipe in meters

# Calculate the flow rate using Poiseuille's Law
flow_rate = calculate_flow_rate(fluid_viscosity, pressure_difference, pipe_radius, pipe_length)

# Print the result
print("Flow Rate:", flow_rate, "m^3/s")

