# Speed data (km/h)
speed = [0, 40, 45, 0, 18, 46, 40, 47, 0, 48, 42, 41, 46, 44, 48, 35, 47, 55, 18, 36, 41]

# Time interval = 1 minute = 1/60 hour
distance_each_min = []

for s in speed:
    distance_each_min.append(s * (1/60))

# Total calculated distance
calculated_distance = sum(distance_each_min)

# Actual distance from Google Maps (ENTER YOUR VALUE HERE)
actual_distance = 10.0   # km

# Percentage error
percentage_error = abs(actual_distance - calculated_distance) / actual_distance * 100

print("Calculated distance (km):", round(calculated_distance, 2))
print("Actual distance (km):", actual_distance)
print("Percentage error (%):", round(percentage_error, 2))