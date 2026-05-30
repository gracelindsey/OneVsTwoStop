# F1 One-Stop vs Two-Stop Strategy Simulator

A Python-based Formula 1 race strategy simulator that compares one-stop and two-stop pit strategies using tire degradation and pit stop time loss.

## Project Overview

This project simulates:
- Tire degradation over a 60-lap race
- Lap time increases caused by tire wear
- Pit stop time penalties
- Total race time for different strategies

The program compares:
- A **1-stop strategy**
- A **2-stop strategy**

and visualizes lap times using graphs.

---

## Features

- Simulates lap-by-lap race pace
- Models tire degradation
- Calculates total race times
- Compares strategic outcomes
- Visualizes strategy performance with Matplotlib

---

## Technologies Used

- Python
- NumPy
- Matplotlib

---

## How It Works

### Assumptions
- Total race length: 60 laps
- Base lap time: 90 seconds
- Tire degradation: +0.05 seconds per lap
- Pit stop time loss: 22 seconds

### Strategy Comparison

#### 1-Stop Strategy
- Two 30-lap stints
- One pit stop

#### 2-Stop Strategy
- Three 20-lap stints
- Two pit stops

The simulator calculates cumulative race time for each strategy and plots lap times across the race.

---

## Example Output

```python
1-stop total time: 5435.5 seconds
2-stop total time: 5451.0 seconds