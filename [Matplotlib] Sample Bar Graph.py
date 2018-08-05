# Sample Bar Graph- Generates A Bar Graph Of Sample Data

import matplotlib.pyplot as plt # Import Matplotlib
import numpy as np # Import Numpy

# Plotting Data
schl_names = ("Ravenna HS", "Theodore Roosevelt HS", "Hoover HS", "McKinley HS", "Stow-Munroe Falls HS")
population = [930, 1300, 1700, 900, 2000] # Population of schools
x_values = np.arange(len(schl_names)) # Arrange - Evenly spaced bars

def bar_graph (): # Generates a line graph of sample data
    plt.bar (x_values, population, align = 'center', color = '#a93226') # Align - Alignment of bars
    plt.xticks (x_values, schl_names, fontsize = 7)
    plt.title ("Population Of Schools") # Sets Title
    plt.show()

bar_graph ()
