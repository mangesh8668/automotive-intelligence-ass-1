import numpy as np

# Speed from Google Maps (km/h)
speed_measured = np.array([
    0, 40, 45, 0, 18, 46, 40, 47, 0, 48, 42, 41, 46, 44, 48, 35, 47, 55, 18, 36, 41, 47, 39, 36, 8, 40, 9, 0, 36, 42, 30, 6, 35, 12, 27, 41, 38, 34, 54, 32, 43, 52, 30, 38, 33, 22, 0

])

# Distance covered each minute (km)
distance_each_min = speed_measured * (1 / 60)

# Speed calculated back from distance
speed_calculated = distance_each_min * 60

# Error calculations
absolute_error = np.abs(speed_measured - speed_calculated)
mean_error = np.mean(absolute_error)
rmse = np.sqrt(np.mean(absolute_error ** 2))

print("Absolute Error (km/h):", absolute_error)
print("Mean Error (km/h):", round(mean_error, 2))
print("RMSE (km/h):", round(rmse, 2))