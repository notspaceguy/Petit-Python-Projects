# Sample Line Graph- Generates A Line Graph Of Sample Data

import matplotlib.pyplot as plt # Import Matplotlib

# Plotting Data
time = [t for t in range(0, 61, 10)] # Seconds = 10 - 60 in intervals of 10
vol = [v for v in range(300, 59, -40)] # Seconds = 300 - 60 in intervals of -40


def line_graph (): # Generates a line graph of sample data
    plt.title ("Volume Against Time \n") # Sets Title
    plt.plot (time, vol, linewidth = 2, color = '#000000')
    plt.xlabel = ('Time')
    plt.ylabel = ('Volume')
    plt.show()

line_graph ()
