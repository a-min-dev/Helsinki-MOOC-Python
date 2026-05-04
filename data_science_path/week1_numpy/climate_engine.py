import numpy as np

days = np.array([0, 1, 2, 3, 4, 5, 6])
print(f"Days: {days}")

hours = np.arange(24)
print(f"Hours: {hours}")

humidity_scale = np.linspace(0, 100, 5)
print(f"Humidity Scale: {humidity_scale}")

print(hours.dtype)
print(humidity_scale.dtype)

print(humidity_scale.size)

print(hours.ndim)