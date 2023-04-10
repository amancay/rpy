import matplotlib.pyplot as plt
import numpy as np
import math

rmax = 36

rarr = [36,35,32,27,20,11]

td = 0.0
pi2 = 6.28
center = np.array([0, 0])

# Create a figure and axes object
fig, ax = plt.subplots()

# Run the animation loop
while True:
    # Clear the axes
    ax.clear()

    # Draw the coordinate lines
    for radius in rarr:
        circle = plt.Circle(center, radius, fill=False, color='lightgrey')
        ax.add_artist(circle)

    for ri in range(12):
        rix = rmax*math.sin(pi2*ri/12)
        riy = rmax*math.cos(pi2*ri/12)
        ax.plot([0,rix], [0,riy], color='lightgrey')
        
    arx = 15*math.sin(pi2*td)
    ary = 15*math.cos(pi2*td)
    ardx = 8*math.cos(pi2*td)
    ardy = -8*math.sin(pi2*td)
    ax.arrow(arx, ary, ardx, ardy, width=0.01, head_width=0.5, head_length=0.5, length_includes_head=True, color='red')
    
    mass = plt.Circle([arx,ary], 1, color='lightblue')
    ax.add_artist(mass)
    
    sun = plt.Circle([0,0], 2, color='yellow',zorder=10)
    ax.add_artist(sun)
    
    for i in range(len(rarr)):
        rarr[i] = rmax - (i + td)**2
        
    td += 0.02
    if td >= 1.0:
        td = 0

    # Set the limits of the axes
    ax.set_xlim([-25, 25])
    ax.set_ylim([-25, 25])

    # Update the plot
    plt.pause(0.01)
