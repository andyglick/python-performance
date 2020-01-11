# import json
import sys

import matplotlib.pyplot as plt
import zarr

sys.path.insert(0, '../shared')


root = zarr.open('db.zarr', mode='r')
positions = root['/chromosome-1/positions']
positions_set = set(positions)

min_position = min(positions)
max_position = max(positions)
middle_location = (max_position + min_position) // 2

print(len(positions))
print(middle_location)
print(positions[len(positions) // 2])


def expected_index(position):
    return (len(positions) * (position - min_position)) // (max_position - min_position)

fig, axs = plt.subplots(nrows=3, sharex=True, squeeze=False)
axs[0, 0].plot([min_position, max_position], [min_position, max_position])
axs[0, 0].plot(positions, positions, '.')
axs[1, 0].plot(positions, [index - expected_index(position) for index, position in enumerate(positions)], '.')
axs[2, 0].hist(positions, bins=50)
fig.show()
input()
