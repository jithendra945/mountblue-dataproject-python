"""
Total SAARC population vs year
"""
# importing the required libraries
import csv
from collections import defaultdict
import matplotlib.pyplot as plt

years = [
         "2005", "2006", "2007", "2008",
         "2009", "2010", "2011", "2012",
         "2013", "2014", "2015"
         ]
year = []
population = []
saarc = defaultdict(int)


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
    with open('datasets/saarc_countries.csv', 'r') as saarc_countries:
        saarc_data = list(csv.reader(saarc_countries, delimiter='\n'))
        saarc_list = []
        for i in range(1, len(saarc_data)):
            saarc_list.append(saarc_data[i][0])
        for row in population_data:
            if row[region_index] in saarc_list:
                if row[year_index] in years:
                    saarc[row[year_index]] += int(float(row[population_index]))
        saarc_countries.close()
    population_estimate.close()

# Passing the parameters to the bar function,
# this is the main function which creates the bar plot
plt.bar(saarc.keys(), saarc.values())
x = list(saarc.keys())
y = list(saarc.values())
addlabels(x, y)

plt.title('Total SAARC population vs year')
plt.xlabel('Years')
plt.ylabel('Population')
plt.xticks(rotation=25)

# Displaying the bar plot
plt.show()
