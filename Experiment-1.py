#-----TASK - 1 -----
import matplotlib.pyplot as plt 
import numpy as np
# Hard-coded variables (you can replace these with real data)
a = 0.1	# coefficient for the quadratic term
b = 2.0	# coefficient for the linear term
c = 10.0	# constant term
# Generate time values
time = np.linspace(0, 10, 100)
# Quadratic equation representing temperature over time
temperature = a * time**2 + b * time + c
# Plotting the quadratic function
plt.plot(time, temperature, label='Temperature Model', color='blue') 
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Weather Modeling with Quadratic Solution')
# Keyboard input for additional point
additional_time = 5
additional_temperature = a * additional_time**2 + b * additional_time + c
plt.scatter(additional_time,  additional_temperature,  color='red', 𝗌label='Additional Point') 
plt.legend()
# Display the plot
plt.show()

#-----TASK - 2 -----
import matplotlib.pyplot as plt import numpy as np

# Read input from the user
days = int(input("Enter the number of days: "))
temperature_coefficient = float(input("Enter the quadratic coefficient for 𝗌temperature: "))
rainfall_coefficient = float(input("Enter the quadratic coefficient for 𝗌rainfall: "))
initial_temperature = float(input("Enter the initial temperature: ")) 
initial_rainfall = float(input("Enter the initial rainfall: "))
# Quadratic solutions for temperature and rainfall
days_array = np.arange(1, days + 1)
temperature = initial_temperature - temperature_coefficient * (days_array - 1)** 2
rainfall = initial_rainfall + rainfall_coefficient * (days_array - 1) ** 2
# Plotting the results
plt.plot(days_array, temperature, label='Temperature') plt.plot(days_array, rainfall, label='Rainfall')
# Adding labels and title plt.xlabel('Days') plt.ylabel('Value')
plt.title('Weather Modeling with Quadratic Solution')
# Adding a legend
plt.legend()
# Displaying the plot
plt.show()

#-----TASK - 3 -----
import matplotlib.pyplot as plt 
import numpy as np
file_path = "weather_parameters.txt"
try:
with open(file_path, "r") as file:
days, temp_coeff, rain_coeff, init_temp, init_rain = map(float, file.
𝗌read().splitlines())
except FileNotFoundError:
print(f"File not found: {file_path}")
days, temp_coeff, rain_coeff, init_temp, init_rain = 0, 0, 0, 0, 0
except ValueError as e:
print(f"Error reading values from the file: {e}")
days, temp_coeff, rain_coeff, init_temp, init_rain = 0, 0, 0, 0, 0
days_array = np.arange(1, int(days) + 1)
temperature = init_temp - temp_coeff * (days_array - 1) ** 2 rainfall = init_rain + rain_coeff * (days_array - 1) ** 2
plt.plot(days_array, temperature, label='Temperature') plt.plot(days_array, rainfall, label='Rainfall')
plt.xlabel('Days') plt.ylabel('Value')
plt.title('Weather Modeling with Quadratic Solution')
plt.legend()
plt.show()

#-----TASK - 4 -----
import matplotlib.pyplot as plt 
import numpy as np
# Predefined values as a list
parameters = [10, 2.5, 0.5, 25.0, 5.0]
# Unpack the values from the list
days, temp_coeff, rain_coeff, init_temp, init_rain = parameters
days_array = np.arange(1, int(days) + 1)
temperature = init_temp - temp_coeff * (days_array - 1) ** 2 
rainfall = init_rain + rain_coeff * (days_array - 1) ** 2
plt.plot(days_array, temperature, label='Temperature') 
plt.plot(days_array, rainfall, label='Rainfall')
plt.xlabel('Days') plt.ylabel('Value')
plt.title('Weather Modeling with Quadratic Solution') 
plt.legend()
plt.show()

#-----TASK - 5 -----
import matplotlib.pyplot as 
plt import numpy as np
# Predefined sets of values as a list of lists
parameter_sets = [
[10, 2.5, 0.5, 25.0, 5.0],
[15, 3.0, 0.6, 22.0, 7.0],
# Add more sets as needed
]
# Process each set of parameters
for parameters in parameter_sets:
days, temp_coeff, rain_coeff, init_temp, init_rain = parameters
days_array = np.arange(1, int(days) + 1)
temperature = init_temp - temp_coeff * (days_array - 1) ** 2 rainfall = init_rain + rain_coeff * (days_array - 1) ** 2
plt.plot(days_array, temperature, label=f'Temperature (Set {parameter_sets.
𝗌index(parameters) + 1})')
plt.plot(days_array, rainfall, label=f'Rainfall (Set {parameter_sets.
𝗌index(parameters) + 1})')
# Adding labels and title plt.xlabel('Days') plt.ylabel('Value')
plt.title('Weather Modeling with Quadratic Solution') plt.legend()
# Displaying the plot
plt.show()
