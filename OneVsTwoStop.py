import matplotlib.pyplot as plt

# Tire definitions
tires = {
    "Soft": {"base_time": 89.0, "deg": 0.08},
    "Medium": {"base_time": 90.0, "deg": 0.05},
    "Hard": {"base_time": 91.0, "deg": 0.03}
}

pit_loss = 22.0


def simulate_stint(laps, tire):
    lap_times = []
    degradation = 0

    base_time = tires[tire]["base_time"]
    deg_rate = tires[tire]["deg"]

    for lap in range(laps):
        lap_time = base_time + degradation
        lap_times.append(lap_time)
        degradation += deg_rate

    return lap_times


# Strategy 1: Soft -> Hard
strategy1 = (
    simulate_stint(30, "Soft")
    + [pit_loss]
    + simulate_stint(30, "Hard")
)

# Strategy 2: Medium -> Hard
strategy2 = (
    simulate_stint(30, "Medium")
    + [pit_loss]
    + simulate_stint(30, "Hard")
)

# Strategy 3: Soft -> Medium -> Hard
strategy3 = (
    simulate_stint(20, "Soft")
    + [pit_loss]
    + simulate_stint(20, "Medium")
    + [pit_loss]
    + simulate_stint(20, "Hard")
)

# Total times
total1 = sum(strategy1)
total2 = sum(strategy2)
total3 = sum(strategy3)

print("\nRace Results")
print("-" * 30)
print(f"Soft -> Hard: {total1:.2f} seconds")
print(f"Medium -> Hard: {total2:.2f} seconds")
print(f"Soft -> Medium -> Hard: {total3:.2f} seconds")

# Determine winner
results = {
    "Soft -> Hard": total1,
    "Medium -> Hard": total2,
    "Soft -> Medium -> Hard": total3
}

winner = min(results, key=results.get)

print("\nWinning Strategy:")
print(f"{winner} wins!")

# Graph
plt.figure(figsize=(10, 6))

plt.plot(strategy1, label="Soft -> Hard")
plt.plot(strategy2, label="Medium -> Hard")
plt.plot(strategy3, label="Soft -> Medium -> Hard")

plt.xlabel("Lap")
plt.ylabel("Lap Time (seconds)")
plt.title("F1 Tire Strategy Comparison")
plt.legend()
plt.grid(True)

plt.show()