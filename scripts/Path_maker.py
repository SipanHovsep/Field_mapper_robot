import csv
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------- parameters ----------
RADIUS_MM = 30           # sphere radius
STEP_MM   = 25            # grid spacing for x, y, z
OUTFILE   = "path.csv"
# ---------------------------------

R2 = RADIUS_MM ** 2
points = []

# Z slices: -30, -25, …, +25, +30
for z in range(-RADIUS_MM, RADIUS_MM + 1, STEP_MM):
    r2_xy = R2 - z**2
    if r2_xy < 0:
        continue  # this slice is outside the sphere

    r_xy = int(sqrt(r2_xy))

    for x in range(-r_xy, r_xy + 1, STEP_MM):
        for y in range(-r_xy, r_xy + 1, STEP_MM):
            if x*x + y*y <= r2_xy:
                points.append((x, y, z, ""))  # empty reading for now

# write to CSV
with open(OUTFILE, "w", newline="") as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerow(["x", "y", "z"])
    writer.writerows([(x, y, z) for (x, y, z, _) in points])

print(f"{len(points)} points written to {OUTFILE}")

# -------- prepare path for animation --------
path = np.array([(x, y, z) for (x, y, z, _) in points])  # (N, 3)

# -------- set up 3-D plot ---------------------
fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
ax.set_title('Robot path (5 mm grid)')

# start with an empty scatter
scatter = ax.scatter([], [], [], s=30, c='tab:blue')

# -------- animation function -----------------
def update(frame):
    current = path[:frame + 1]
    scatter._offsets3d = (current[:, 0], current[:, 1], current[:, 2])
    return scatter,

ani = FuncAnimation(fig,
                    update,
                    frames=len(path),
                    interval=30,
                    blit=False,
                    repeat=False)

plt.show()
