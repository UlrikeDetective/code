import matplotlib.pyplot as plt
import numpy as np
import time

def update_donut_chart(ax, total_time, elapsed_time):
    remaining_time = total_time - elapsed_time
    fraction = remaining_time / total_time
    
    # Donut chart parameters
    size = 0.3
    vals = [fraction, 1 - fraction]
    cmap = plt.get_cmap("coolwarm")
    outer_colors = cmap([0.25, 0.75])
    
    ax.clear()
    wedges, _ = ax.pie(vals, radius=1, colors=outer_colors, startangle=90, counterclock=False)
    plt.setp(wedges, width=size, edgecolor='white')

    # Add a circle at the center to make it a donut
    centre_circle = plt.Circle((0, 0), 1 - size, color='white', fc='white', linewidth=0)
    ax.add_artist(centre_circle)
    
    # Add the countdown text
    ax.text(0, 0, f'{int(remaining_time)}s', ha='center', va='center', fontsize=24, color='black')
    
    # Remove axis
    ax.axis('equal')

def countdown_timer(total_time):
    fig, ax = plt.subplots()
    plt.ion()  # Enable interactive mode
    start_time = time.time()
    
    while True:
        elapsed_time = time.time() - start_time
        
        if elapsed_time >= total_time:
            break
            
        update_donut_chart(ax, total_time, elapsed_time)
        plt.draw()
        plt.pause(1)  # Pause to allow GUI update
        
    # Ensure the final state shows 0 seconds remaining
    update_donut_chart(ax, total_time, total_time)
    plt.draw()
    plt.pause(1)

    plt.ioff()  # Disable interactive mode
    plt.show()

# Set the countdown timer for 30 seconds
countdown_timer(30)
