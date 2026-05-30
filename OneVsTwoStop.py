import numpy as np
import matplotlib.pyplot as plt


total_laps = 60
base_lap_time = 90.0
tire_deg_per_lap = 0.05
pit_loss = 22.0


def simulate_stint(laps, starting_deg=0):
    lap_times = []
    degradation = starting_deg

    for lap in range(laps):
        lap_time = base_lap_time + degradation
        lap_times.append(lap_time)
        degradation += tire_deg_per_lap

    return lap_times, degradation


stint1_1stop, deg1 = simulate_stint(30)
stint2_1stop, deg2 = simulate_stint(30)

race_1stop = stint1_1stop + [pit_loss] + stint2_1stop
total_time_1stop = sum(race_1stop)


stint1_2stop, deg1 = simulate_stint(20)
stint2_2stop, deg2 = simulate_stint(20)
stint3_2stop, deg3 = simulate_stint(20)

race_2stop = stint1_2stop + [pit_loss] + stint2_2stop + [pit_loss] + stint3_2stop
total_time_2stop = sum(race_2stop)


print("1-stop total time:", round(total_time_1stop, 2), "seconds")
print("2-stop total time:", round(total_time_2stop, 2), "seconds")


plt.plot(race_1stop, label="1-stop strategy")
plt.plot(race_2stop, label="2-stop strategy")
plt.xlabel("Lap")
plt.ylabel("Lap Time (seconds)")
plt.title("Race Strategy Comparison")
plt.legend()
plt.show()