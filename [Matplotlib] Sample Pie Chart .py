# Sample Pie Chart- Generates A Pie Chart Of Sample Data

import matplotlib.pyplot as plt # Import Matplotlib
plt.rcParams ['font.size'] = 8.5

# Plotting Data
ice_crm_flvrs = ['Chocolate', 'Strawberry', 'Oatmeal', 'Coconut', 'Mint', 'Grape']
week_sales = [36, 47, 18, 63, 132, 23]
clr = ['#9f6060', '#c63939', '#bc8f8f', '#704343', '#609f8f', '#8f609f']

def pie_chart (): # Generates a pie chart of sample data
    plt.title ("Ice Cream Flavour Sales This Week") # Sets Title
    plt.pie (week_sales, labels = ice_crm_flvrs, colors = clr, autopct = '%1.1f%%') # autopct - display % value
    plt.legend(ice_crm_flvrs, loc = 'lower right') # Creates Legend
    plt.axis ('equal') # Sets axis
    plt.show()

pie_chart ()
