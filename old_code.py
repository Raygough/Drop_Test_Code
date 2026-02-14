import matplotlib.pyplot as plt

# parameters
g = 9.81       # acceleration due to gravity (m/s^2)
h0 = 1.8        # initial height (m)
v0 = 0         # initial velocity (m/s)
dt = 0.01      # time step (s)

t, h, v = 0, h0, v0
times, heights = [t], [h]

while h > 0:
    v -= g * dt
    h += v * dt
    if h < 0:
        h = 0
    t += dt
    times.append(t)
    heights.append(h)

plt.plot(times, heights)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Drop Test: Free Fall')
plt.show()
