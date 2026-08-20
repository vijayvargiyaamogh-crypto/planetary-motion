import math
import matplotlib.pyplot as plt

x, y = 1, 0 # Initial coordinates of the planet (star at origin)
vx, vy = 0, 1 # Initial velocity components of the planet (horizontal and vertical)

GM = 1 # Same as gravitational constant times mass of star

T = 8 # Time period of numerical simulation
N = 256 # Number of timesteps in numerical simulation (can increase this parameter for more precision)
dt = T/N # Size of timestep

positions = [(x, y)] # Array to which new coordinates will be appended every dt = T/N

for step in range(1, N+1):
    r3 = math.pow(x*x + y*y, 1.5) # Cube of star-planet distance
    ax, ay = (-GM/r3)*x, (-GM/r3)*y # Acceleration components from inverse-square law of gravitation
    
    x, y = x + vx*dt + 0.5*ax*dt*dt, y + vy*dt + 0.5*ay*dt*dt # Second-order calculation of new position
    vx, vy = vx + ax*dt, vy + ay*dt # First-order calculation of new velocity

    if step % 4 == 0: # Only every fourth position is plotted (to declutter the graph)
        positions.append((x, y))

x_series, y_series = zip(*positions) # Separate x and y coordinates into two arrays for plotting

plt.scatter(x_series, y_series) # Plots the position of the planet over time (dotted path)
plt.show()
        

