import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CONSTANTS
# -------------------------------------------------
g = 9.81
rho = 1.225
Cd = 0.47
h0 = 3.8989
v0 = 0


# -------------------------------------------------
# DROP SIMULATION (WITH DRAG)
# -------------------------------------------------
def drop_simulation(dt, A, m):

    t = 0
    h = h0
    v = v0

    times = [t]
    heights = [h]

    while h > 0:

        drag = 0.5 * rho * Cd * A * v * abs(v)
        a = g - drag/m

        # Explicit Euler update
        v += a * dt
        h -= v * dt
        t += dt

        times.append(t)
        heights.append(max(h, 0))

    return t, np.array(times), np.array(heights)


# -------------------------------------------------
# OBJECT PARAMETERS
# -------------------------------------------------

# Sewing cushion
d_cushion = 0.0059
A_cushion = np.pi * (d_cushion/2)**2
m_cushion = 0.002

# Thimble
d_thimble = 0.0016
A_thimble = np.pi * (d_thimble/2)**2
m_thimble = 0.001


# -------------------------------------------------
# 1. TIME STEP ANALYSIS (SEWING CUSHION)
# -------------------------------------------------

dt_reference = 0.01
dt_values = np.array([0.1, 0.05, 0.02, 0.01, 0.005, 0.001])

reference_time, _, _ = drop_simulation(dt_reference, A_cushion, m_cushion)

times_vs_dt = []
percent_diff = []

for dt in dt_values:
    t_val, _, _ = drop_simulation(dt, A_cushion, m_cushion)
    times_vs_dt.append(t_val)
    percent_diff.append(100 * abs(t_val - reference_time) / reference_time)

print("Time Step Analysis (Reference dt = 0.01) – Sewing Cushion")
print("------------------------------------------------------------")
for i in range(len(dt_values)):
    print(f"dt = {dt_values[i]:.4f} | Drop Time = {times_vs_dt[i]:.5f} s | % Difference = {percent_diff[i]:.3f}%")

plt.figure()
plt.plot(dt_values, times_vs_dt, marker='o')
plt.xlabel("Time Step (s)")
plt.ylabel("Computed Drop Time (s)")
plt.title("Time Step Convergence (Sewing Cushion)")
plt.gca().invert_xaxis()
plt.show()


# -------------------------------------------------
# 2. FINAL DROP TEST GRAPH (BOTH OBJECTS)
# -------------------------------------------------

dt_final = 0.001

t_cushion, times_c, heights_c = drop_simulation(dt_final, A_cushion, m_cushion)
t_thimble, times_t, heights_t = drop_simulation(dt_final, A_thimble, m_thimble)

print("\nFinal Fall Time (dt = 0.001):")
print("Sewing Cushion:", round(t_cushion, 5), "s")
print("Thimble:", round(t_thimble, 5), "s")

plt.figure()
plt.plot(times_c, heights_c, label="Sewing Cushion")
plt.plot(times_t, heights_t, label="Thimble")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Drop Test With Air Resistance")
plt.legend()
plt.show()