import csv
import numpy as np

with open('rate_0.35_record.csv') as f:
    data = list(csv.reader(f))

# we want to find m and b such that: vel = m*freq + b

frequencies = []
velocities = []
for datum in data:
    frequencies.append(datum[0])
    delta_time_s = datum[2]
    displacement_m = datum[3]/100
    velocity_mps = displacement_m / delta_time_s
    velocities.append(velocity_mps)

np.polyfit(np.a
