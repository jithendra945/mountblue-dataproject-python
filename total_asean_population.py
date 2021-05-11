"""
total ASEAN countries population for the years 2005 to 2014
"""
# importing the required libraries
import csv
import numpy as np
import matplotlib.pyplot as plt

years = [
         "2005", "2006", "2007",
         "2008", "2009", "2010",
         "2011", "2012", "2013", "2014"
        ]
country = []
population = []


def addlabels(x_value, y_value):
    """
    Adding labels on top of bar plot
    """
    for j in range(len(x_value)):
        plt.text(j, y_value[j], y_value[j], ha="center")


with open('datasets/population_estimates_csv.csv', 'r') as population_estimate:
    population_data = list(csv.reader(population_estimate, delimiter=','))
    region_index = population_data[0].index('Region')
    year_index = population_data[0].index('Year')
    population_index = population_data[0].index('Population')
    with open('datasets/asean_countries.csv', 'r') as asean_countries:
        asean_data = list(csv.reader(asean_countries, delimiter='\n'))
        asean_list = []
        for i in range(1, len(asean_data)):
            asean_list.append(asean_data[i][0])
        population = []
        for l in asean_list:
            country.append(l)
            temp = []
            for y in years:
                for row in population_data:
                    if row[region_index] == l and row[year_index] == y:
                        temp.append(int(float(row[population_index])))
            population.append(temp)
        asean_countries.close()
    population_estimate.close()

x = np.arange(len(country))
WIDTH = 0.075  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 0.3, population[0], WIDTH, label='Brunei')
rects2 = ax.bar(x - 0.225, population[1], WIDTH, label='Cambodia')
rects3 = ax.bar(x - 0.15, population[2], WIDTH, label='Indonesia')
rects4 = ax.bar(x - 0.075, population[3], WIDTH, label='Loas')
rects5 = ax.bar(x, population[4], WIDTH, label='Malaysia')
rects6 = ax.bar(x + 0.075, population[5], WIDTH, label='Myanmar')
rects7 = ax.bar(x + 0.15, population[6], WIDTH, label='Philippines')
rects8 = ax.bar(x + 0.225, population[7], WIDTH, label='Singapore')
rects9 = ax.bar(x + 0.3, population[8], WIDTH, label='Thailand')
rects10 = ax.bar(x + 0.375, population[9], WIDTH, label='Vietnam')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Years')
ax.set_ylabel('Population')
ax.set_title('Total ASEAN countries population for the year 2005-2014')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
# to see the values on top of bar, enable the below code
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
# ax.bar_label(rects4, padding=3)
# ax.bar_label(rects5, padding=3)
# ax.bar_label(rects6, padding=3)
# ax.bar_label(rects7, padding=3)
# ax.bar_label(rects8, padding=3)
# ax.bar_label(rects9, padding=3)
# ax.bar_label(rects10, padding=3)
fig.tight_layout()
# Displaying the bar plot
plt.show()
