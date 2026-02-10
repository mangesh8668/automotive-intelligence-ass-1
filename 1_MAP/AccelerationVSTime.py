import matplotlib.pyplot as plt
import numpy as np

# Time (minutes)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

# Speed (km/h)
speed = [0, 40, 45, 0, 18, 46, 40, 47, 0, 48, 42, 41, 46, 44, 48, 35, 47, 55, 18, 36, 41, 47, 39, 36, 8, 40, 9, 0, 36, 42, 30, 6, 35, 12, 27, 41, 38, 34, 54, 32, 43, 52, 30, 38, 33, 22, 0]

# Calculate acceleration (km/h per minute)
acceleration = np.diff(speed)  # delta speed
time_acc = time[1:]            # corresponding time values

plt.figure()
plt.plot(time_acc, acceleration, marker='o')
plt.xlabel("Time (minutes)")
plt.ylabel("Acceleration (km/h per minute)")
plt.title("Acceleration vs Time")
plt.grid(True)
plt.show()